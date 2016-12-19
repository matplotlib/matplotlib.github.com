import matplotlib.pyplot as plt
import numpy as np

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(5, 5))

def demo(bar_func, bar_kwargs):
    return bar_func([1, 2, 3], [1, 2, 3], tick_label=['a', 'b', 'c'],
                    **bar_kwargs)


ax1.set_title('2.0')

ax2.set_title("classic alignment")

demo(ax1.bar, {})
demo(ax2.bar, {'align': 'edge'})
demo(ax3.barh, {})
demo(ax4.barh, {'align': 'edge'})