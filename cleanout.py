import os
import sys
from bs4 import BeautifulSoup as BS
from pathlib import Path
"""
Display warning banner on latest/'versionless' docs that aren't in current release.

Requires a single commandline argument for the latest version.
"""

# def tempname(file):
    # *name, ext = file.split('.')
    # return ('.'.join([*name, 'tmp', ext])) 

def adjust(root, file, dry = False):
    '''
    mark an html file deprecated
    dry: do not overwrite, but go to temp file.
    '''
    p = Path(root)
    # if ('.tmp' in Path(file).suffixes): return # prefer to ignore own temp files.
                
    with open(p / file, "rt") as f:
        parse = BS(f, 'lxml')
    
        s = ' '.join(file.split('.')[:-1])
        query = ' '.join(s.split('_')) # works well for (mpl_)examples, gallery
        
        if 'index' == s:
            query = parse.find('h1').text[:-1].replace('_', ' ')
            
            # ' '.join(p.parts) if s == 'index'
        search = '''https://matplotlib.org/search.html?q={}'''.format(query)
        
        for child in parse.html.children:
            # accessing children outside of iteration confuses beautifulsoup
            
            # if child.name == 'img':
                # WIP: attempt to deprecate image, if it isn't static
                # if os.path.exists(p / ):
                    # child['src'] = tempname(child['src'])

            if child.name == 'body':
                # id="legacy-docs-banner" class="warning"
                banner = BS('''<div id="unreleased-message"> 
            You are reading documentation that no longer exists in the
            current release of Matplotlib! <a href="{}">Try searching for
            an updated version?</a>
            </div>'''.format(search), 'html.parser')
                child.insert(0, banner)

        if not dry:
            with open(p/file, "wt") as g:
                g.write(str(parse))
        else:
            print( query )

# adjust('examples/images_contours_and_fields', 'contourf_log.html', dry=True)
# adjust('devel', 'index.html', True)
# adjust('api/_as_gen', 'matplotlib.animation.Animation.save.html', True)

if __name__ == "__main__":
    for tree in ('examples', 'mpl_examples', 'plot_directive', # '_images'
                 'devel', 'users', 'api', 'faq', 'glossary'):
        
        for root, dirs, files in os.walk(os.path.join(tree)):
            # FIXME: how to run from another directory without introducing '..' to root?
            
            for file in files:
                if not os.path.exists(os.path.join(latest, root, file)):
                    # if missing from latest release
                    
                    if file.endswith('.html'):
                        adjust(root, file)
                    elif file.endswith('.png'):
                        pass
                        # os.rename(file, tempname(file))
                        
                    elif file.endswith('.py') or file.endswith('.pdf'):
                        os.system('git rm ' + os.path.join(root, file))
                    
                    if verbose: print(os.path.join(root, file))
                        
                # elif verbose:
                    # print('SKIP ' + os.path.join(root, file))
