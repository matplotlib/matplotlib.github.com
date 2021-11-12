
from pathlib import Path
import logging 

import matplotlib
matplotlib.use('Agg')

_log = logging.getLogger(__name__)
# start to make info.js

stout = 'var images_rotate = [\n'
# assumes that your directory structure has matplotlib/ and mpl-brochure-site/ 
# at the same level relative each other.  
home = Path('../../../../matplotlib/')
dirs = ['plot_types/arrays/', 'plot_types/basic/', 'plot_types/stats/']
for d in dirs:
    _log.info('working on: %s', d)
    for fn in (home / d).glob('*.py'):
        _log.info('               %s', fn)
        name = fn.stem
        exec(fn.read_text())
        fig.savefig(f'{name}300.png', dpi=300)
        # fig.savefig(f'{name}150.png', dpi=150)
        stop = False
        for line in open(fn):
            if stop:
                cap = line[:-1]
                break
            if line[:3] == '===':
                stop = True            
        stout += '    {' + f'"image": "{name}300.png", "caption": "{cap}", "link": "{d}{name}.html"' + '},\n'

stout +=  '];'

open('../images-rotate-info.js', 'w').write(stout)