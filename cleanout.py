import os
import sys

"""
Cleans out the top-level (latest) docs from old files.

Requires a single commandline argument for the latest version.
"""

redirect = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <meta http-equiv="refresh" content="0; url=index.html"/>
  </head>
</html>
"""

latest = sys.argv[-1]

for tree in ('examples', '_images', 'mpl_examples', 'plot_directive', 'devel', 'users', 'api', 'faq', 'glossary'):
    for root, dirs, files in os.walk(tree):
        for file in files:
            if not os.path.exists(os.path.join(latest, root, file)):
                print(os.path.join(root, file))

                if file.endswith('.html'):
                    with open(os.path.join(root, file), 'w') as fd:
                        fd.write(redirect.strip())
                elif file.endswith('.py') or file.endswith('.png') or file.endswith('.pdf'):
                    os.system('git rm ' + os.path.join(root, file))
