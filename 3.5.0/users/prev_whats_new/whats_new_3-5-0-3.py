from matplotlib import pyplot as plt
from matplotlib.widgets import TextBox

for i, alignment in enumerate(['left', 'center', 'right']):
        box_input = plt.axes([0.2, 0.7 - i*0.2, 0.6, 0.1])
        text_box = TextBox(ax=box_input, initial=f'{alignment} alignment',
                           label='', textalignment=alignment)