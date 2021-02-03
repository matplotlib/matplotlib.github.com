import argparse
import glob
import logging
import multiprocessing
import os
import pathlib
import re
import subprocess
import sys
import tempfile
import shutil

"""
This script does two things that improve the website organization.

First, we used to host in the root of the webpage, but have now moved to
``/stable/``.  We do not want obsolete links to link to nothing (or that has
been our policy), so we currently just keep the old version at the top level.
Here, instead, we either softlink to the newest version, or replace the file by
an html refresh redirect.

Second, it changes the canonical link in each html file to the newest version
found of the html file (including stable if its in the latest version.)

This script takes a while, and is destructive, so should probably be run on a
branch and pushed as a PR so it can easily be reverted.
"""

_log = logging.getLogger("make_redirect_links")


tocheck = ["stable"] + [
    f"{major}.{minor}.{micro}"
    for major in range(6, -1, -1)
    for minor in range(6, -1, -1)
    for micro in range(6, -1, -1)
    if pathlib.Path(f"{major}.{minor}.{micro}").exists()
]

toignore = tocheck + [
    "mpl-probscale",
    "mpl_examples",
    "mpl_toolkits",
    "_webpageutils",
    "xkcd",
    "sitemap.xml",
    "robots.txt",
    "CNAME",
    ".git",
]

logging.basicConfig(level=logging.DEBUG)


def findlast(fname, tocheck):
    """
    Check the directories listed in ``tocheck`` to see if they have
    ``fname`` in them.  Return the first one found, or None
    """
    p = pathlib.Path(fname)
    for t in tocheck:
        pnew = pathlib.Path(t, p)
        if pnew.exists():
            return t
    else:
        return None


html_redirect = """
<!DOCTYPE HTML>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="refresh" content="0;%s" />
        <link rel="canonical" href="url=https://matplotlib.org%s" />
    </head>
    <body>
        <h1>
            The page been moved to <a href="%s"</a>
        </h1>
    </body>
</html>
"""


def do_links(root0):
    """
    Either soft link a file at the top level to its newest position,
    or make an html redirect if it is an html file.
    """
    _log.info(f'Doing links on {root0}')
    for root, dirs, files in os.walk(root0):
        for name in files:
            fullname = os.path.join(root, name)
            last = findlast(fullname, tocheck)
            _log.debug(f'Checking: {fullname} found {last}')
            if last is not None:
                os.remove(fullname)
                if name.endswith(('.htm', '.html')):
                    # make an html redirect.
                    _log.info(f'Rewriting HTML: {fullname} in {last}')
                    with open(fullname, 'w') as fout:
                        oldname = '/' + os.path.join(last, fullname)
                        st = html_redirect % (oldname, oldname, oldname)
                        fout.write(st)
                else:
                    # soft link
                    # Need to do these relative to where the link is
                    # so if it is a level down `ln -s ../3.1.1/boo/who boo/who`
                    last = os.path.join('..', last)
                    depth = root.count('/')
                    for i in range(depth):
                        last = os.path.join('..', last)
                    oldname = os.path.join(last, fullname)
                    _log.info(f'Linking {fullname} to {oldname}')
                    os.symlink(oldname, fullname)
        for d in dirs:
            do_links(d)


def do_canonicals(dname):
    """
    For each html file in the versioned docs, make the canonical link point
    to the newest version.
    """
    _log.debug(f'Walking {dname}')
    for root, dirs, files in os.walk(dname):
        for name in files:
            fullname = os.path.join(root, name)
            p = pathlib.Path(fullname)
            _log.debug(f'Checking {fullname}')
            if name.endswith(('.htm', '.html')):
                basename = pathlib.Path(*p.parts[1:])
                last = findlast(basename, tocheck)
                if last is not None:
                    update_canonical(fullname, last)

        for d in dirs:
            _log.info(f'DIR: {d}')
            do_canonicals(os.path.join(dname,d))


def update_canonical(fullname, last):
    """
    Change the canonical link in *fullname* to the same link in the
    version given by *last*.  We do this with a regexp to prevent
    removing any other content on a line that has the canonical link.

    Note that if for some reason there are more than one canonical link
    this will change  all of them.
    """
    p = pathlib.Path(fullname)
    pre = 'https://matplotlib.org/'
    pnew = pathlib.Path(last, *p.parts[1:])
    newcanon = f'{pre+str(pnew)}'
    _log.info(f'{p} to {pre+str(pnew)}')
    with tempfile.NamedTemporaryFile(delete=False) as fout:
        with open(fullname, 'rb') as fin:
            for line in fin:
                if b'<link rel="canonical"' in line:
                    new = bytes(f'<link rel="canonical" href="{newcanon}"',
                                encoding='utf-8')
                    ll = re.sub(b'<link rel="canonical" href=".*"', new,
                                line)
                    _log.debug(f'new {line}->{ll}')
                    fout.write(ll)
                else:
                    fout.write(line)
    shutil.move(fout.name, fullname)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Optional app description')

    parser.add_argument('--np', type=int, help='Number of processors to use')
    parser.add_argument('--no_canonicals', help='do not do canonical links',
                        action="store_true")
    parser.add_argument('--no_redirects', help='do not do redirects links',
                        action="store_true")

    args = parser.parse_args()
    if args.np:
        np = args.np
    else:
        np = None

    # html redirect or soft link most things in the top-level directory that
    # are not other modules or versioned docs.
    if not args.no_redirects:
        for entry in os.scandir('./'):
            if not (entry.name in toignore):
                if entry.is_dir():
                    do_links(entry.name)
                elif entry.name.endswith(('.htm', '.html')):
                    fullname = entry.name
                    last = findlast(fullname, tocheck)
                    _log.debug(f'Checking: {fullname} found {last}')
                    if last is not None:
                        os.remove('./'+fullname)
                        _log.info(f'Rewriting HTML: {fullname} in {last}')
                        with open(fullname, 'w') as fout:
                            oldname = '/' + os.path.join(last, fullname)
                            st = html_redirect % (oldname, oldname, oldname)
                            fout.write(st)
        _log.info('Done links and redirects')

    # change the canonical url for all html to the newest version in the docs:
    if not args.no_canonicals:
        if np is not None:
            with multiprocessing.Pool(np) as pool:
                pool.map(do_canonicals, tocheck[1:])
        else:
            for t in tocheck[1:]:
                do_canonicals(t)
