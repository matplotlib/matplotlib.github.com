import pathlib
import tempfile
import shutil

tocheck =  [
    pathlib.Path(f"{major}.{minor}.{micro}")
    for major in range(2, -1, -1)
    for minor in range(6, -1, -1)
    for micro in range(6, -1, -1)
]


to_add = b"""
/* "Go to released version" message. */
#unreleased-message {
  background: #d62728;
  box-sizing: border-box;
  color: #fff;
  font-weight: bold;
  left: 0;
  min-height: 3em;
  padding: 0.7em;
  position: fixed;
  top: 0;
  width: 100%;
  z-index: 10000;
}

#unreleased-message + div {
  margin-top: 3em;
}

#unreleased-message a {
  color: #fff;
  text-decoration:underline;
}
"""

for d in tocheck:

    fname = pathlib.Path(d, '_static', 'mpl.css')
    if fname.is_file():
        print(f'checking {fname}')
        with open(fname) as f:
            if not "#unreleased-message" in f.read():
                doit = True
            else:
                doit = False
        if doit:
            print(f'doing {d}')
            with tempfile.NamedTemporaryFile(delete=False) as fout:
                with open(fname, 'rb') as f:
                    fout.write(f.read())
                fout.write(to_add)
            print(f.name)
            shutil.move(fout.name, f.name)
