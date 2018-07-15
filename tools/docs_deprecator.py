from bs4 import BeautifulSoup as BS
import os
from pathlib import Path
import re

def adjust(root, file, dry = False):
    '''
    mark an html file deprecated, incl' canonical link for crawlers.
    dry: do not overwrite, but go to temp file.
    '''
    base = Path(root)
    # if (Path(file).suffix != '.html') raise ValueError("Not an html file.")
    if ('.tmp' in Path(file).suffixes): return # prefer to ignore own temp files.
    
    with open(base / file, "rt") as f:
        parse = BS(f, 'lxml')
        for child in parse.html.children: # beautifulsoup likes explicit iteration
            
            if child.name == 'head':
                ver, *rest = base.parts # '/'.join(rest) is our best-guess current version.
                target = os.path.join('https://matplotlib.org', *rest, file)
                    # ADJUST as necessary.
                    # Base path contains version string, so '..' is wrong.
                    
                redirect_bots =                     BS('''<link href="{}" rel="canonical">'''.format(target), 'html.parser')
                    # lxml would wrap this snippet. yuck.
                child.append(redirect_bots)

            elif child.name == 'body':
                banner = BS('''<div id="old-version-banner">
            You are reading documentation for a static version of Matplotlib.
            <a href="{}">This page may have been updated.</a>
            </div>'''.format(target), 'html.parser')
                child.insert(0, banner)

        *name, ext = file.split('.')
        dummy = ('.'.join([*name, 'tmp', ext]))
                # file if (name[-1] == 'tmp') else
        
        with open(base/dummy if dry else base/file, "wt") as g:
            g.write(str(parse))

def process(target, verbose = False, dry = False):
    delve = ''; deeper = ''
    for root, _, files in os.walk(Path(target)):
        path = Path(root)

        # progress meter, inspired loosely by https://stackoverflow.com/a/2165062
        if verbose:
            try:
                s = path.parts[1] # toplevel.index()
                if s != delve:
                    delve = s; print(s)
                else:
                    r = path.parts[2] if s not in ['mpl_examples', 'examples'] else '...'
                    if r != deeper:
                        deeper = r; print('\t' + r)
            except: pass

        for f in files:
            try:
                # expect .pdf, .png, .py files. ignore them.
                if (Path(f).suffix == '.html'):
                    adjust(path, f, False) # time.sleep(.0001)

            except UnicodeDecodeError as e:
                print(f, e)
            except AttributeError as e:
                print(f, e)

if __name__ == "__main__":
    targets = [d for d in os.listdir() if re.match(r'''\d+\.\d+\.\d+''', d)]
    print(targets)
    input("I will mutate all HTML files in the directories listed. Press 'enter' to proceed, 'ctrl-c' to abort.")

    # wait, I need a pristine copy!: svn checkout https://github.com/matplotlib/matplotlib.github.com/trunk/<subdir>
    for t in targets:
        process(t, verbose=False)
        print(t + ' done')
