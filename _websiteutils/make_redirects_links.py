#!/usr/bin/env python3

import argparse
import functools
import logging
import multiprocessing
import os
import pathlib
import re
import tempfile
import shutil

"""
This script does three things that improve the website organization.

First, we used to host in the root of the webpage, but have now moved to
``/stable/``.  We do not want obsolete links to link to nothing (or that has
been our policy), so we currently just keep the old version at the top level.
Here, instead, we either softlink to the newest version, or replace the file by
an html refresh redirect.

Second, it changes the canonical link in each html file to the newest version
found of the html file (including stable if its in the latest version.)

Third, the script adds a new div to the top of all the old webpages with
tag ``olddocs-message`` to warn users that the page is obsolete.

This script takes a while, and is destructive, so should probably be run on a
branch and pushed as a PR so it can easily be reverted.
"""

_log = logging.getLogger("make_redirect_links")


tocheck = [pathlib.Path("stable")] + [
    pathlib.Path(f"{major}.{minor}.{micro}")
    for major in range(6, -1, -1)
    for minor in range(6, -1, -1)
    for micro in range(6, -1, -1)
]

toignore = tocheck + [pathlib.Path(p) for p in [
    "mpl-probscale",
    "_webpageutils",
    "xkcd",
    "_sitemap",
    "robots.txt",
    "CNAME",
    ".git",
]]

logging.basicConfig(level=logging.DEBUG)


@functools.cache
def findlast(fname, tocheck):
    """
    Check the directories listed in ``tocheck`` to see if they have
    ``fname`` in them.  Return the first one found, or None
    """
    for t in tocheck:
        pnew = t / fname
        if pnew.exists():
            return t
    return None


html_redirect = """<!DOCTYPE HTML>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="refresh" content="0;url={newurl}" />
        <link rel="canonical" href="https://matplotlib.org/{canonical}" />
    </head>
    <body>
        <h1>
            The page been moved <a href="{newurl}">here</a>!
        </h1>
    </body>
</html>
"""

# note these are all one line so they are easy to search and replace in the
# html files (otherwise we need to close tags)
warn_banner_exists = (
    '<div id="unreleased-message"> You are reading an old version of the '
    'documentation (v{version}).  For the latest version see '
    '<a href="{url}">{url}</a></div>\n')


warn_banner_old = (
    '<div id="unreleased-message"> You are reading an old version of the '
    'documentation (v{version}).  For the latest version see '
    '<a href="/stable/">https://matplotlib.org/stable/</a> </div>\n')


def do_links(root0):
    """
    Either soft link a file at the top level to its newest position,
    or make an html redirect if it is an html file.
    """

    _log.info(f"Doing links on {root0}")
    for root, dirs, files in os.walk(root0):
        for name in files:
            fullname = pathlib.Path(root, name)
            last = findlast(fullname, tocheck)
            _log.debug(f"Checking: {fullname} found {last}")
            if last is not None:
                fullname.unlink()
                oldname = last / fullname
                # Need to do these relative to where the final is, but note
                # that `Path.relative_to` does not allow '.' as a common path
                # prefix, so we need to use `os.path.relpath` instead.
                relpath = os.path.relpath(oldname, start=fullname.parent)
                if name.endswith((".htm", ".html")):
                    # make an html redirect.
                    _log.info(f"Rewriting HTML: {fullname} in {last}")
                    with fullname.open("w") as fout:
                        st = html_redirect.format(
                            newurl=relpath,
                            canonical=oldname,
                        )
                        fout.write(st)
                else:
                    # soft link
                    _log.info(f"Linking {fullname} to {oldname}")
                    fullname.symlink_to(relpath)


def do_canonicals(dname):
    """
    For each html file in the versioned docs, make the canonical link point
    to the newest version.
    """
    _log.debug(f"Walking {dname}")
    for fullname in dname.rglob("*.html"):
        _log.debug(f"Checking {fullname}")
        basename = pathlib.Path(*fullname.parts[1:])
        last = findlast(basename, tocheck)
        if last is not None:
            update_canonical(fullname, last, dname == tocheck[1])


def update_canonical(fullname, last, newest):
    """
    Change the canonical link in *fullname* to the same link in the
    version given by *last*.  We do this with a regexp to prevent
    removing any other content on a line that has the canonical link.

    Also add a banner (div) in the body if an old version of the docs.

    Note that if for some reason there are more than one canonical link
    this will change  all of them.
    """
    pre = "https://matplotlib.org/"
    pnew = last.joinpath(*fullname.parts[1:])
    newcanon = f"{pre}{str(pnew)}"
    _log.info(f"{fullname} to {pre}{str(pnew)}")
    rec = re.compile(b'<link rel="canonical" href=".*"')
    with tempfile.NamedTemporaryFile(delete=False) as fout:
        found = False
        with fullname.open("rb") as fin:
            for line in fin:
                if not found and b'<link rel="canonical"' in line:
                    new = f'<link rel="canonical" href="{newcanon}"'
                    ll = rec.sub(new.encode("utf-8"), line)
                    _log.debug(f"new {line}->{ll}")
                    fout.write(ll)
                    found = True
                elif b'<body>' in line and not newest:
                    # add a warning right under:
                    fout.write(line)
                    line = next(fin)
                    if last == tocheck[0]:
                        new = warn_banner_exists.format(
                            version=fullname.parts[0],
                            url=newcanon)
                    else:
                        new = warn_banner_old.format(version=fullname.parts[0])
                    fout.write(new.encode("utf-8"))
                    if b'<div id="olddocs-message">' not in line:
                        # write the line out if it wasn't an olddocs-message:
                        fout.write(line)

                else:
                    fout.write(line)

    shutil.move(fout.name, fullname)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--np", type=int, help="Number of processors to use")
    parser.add_argument("--no-canonicals", help="do not do canonical links",
                        action="store_true")
    parser.add_argument("--no-redirects", help="do not do redirects links",
                        action="store_true")

    args = parser.parse_args()
    if args.np:
        np = args.np
    else:
        np = None

    # figure out the newest version and trim tocheck at the same time:
    tocheck = tuple(p for p in tocheck if p.exists())
    print(tocheck)

    # html redirect or soft link most things in the top-level directory that
    # are not other modules or versioned docs.
    if not args.no_redirects:
        for entry in os.scandir("."):
            fullname = pathlib.Path(entry.name)
            if fullname not in toignore:
                if entry.is_dir():
                    do_links(entry.name)
                elif fullname.suffix == ".html":
                    last = findlast(fullname, tocheck)
                    _log.debug(f"Checking: {fullname} found {last}")
                    if last is not None:
                        fullname.unlink()
                        _log.info(f"Rewriting HTML: {fullname} in {last}")
                        with fullname.open("w") as fout:
                            oldname = last / fullname
                            st = html_redirect.format(newurl=oldname,
                                                      canonical=oldname)
                            fout.write(st)
        _log.info("Done links and redirects")

    # change the canonical url for all html to the newest version in the docs:
    if not args.no_canonicals:
        if np is not None:
            with multiprocessing.Pool(np) as pool:
                pool.map(do_canonicals, tocheck[1:])
        else:
            for t in tocheck[1:]:
                do_canonicals(t)
