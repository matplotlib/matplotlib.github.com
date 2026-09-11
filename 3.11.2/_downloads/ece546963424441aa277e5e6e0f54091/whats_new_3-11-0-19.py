fig = plt.figure(figsize=(7, 3))

char = '\U00000431'
fig.text(0.5, 0.8, f'\\U{ord(char):08x}', fontsize=40, horizontalalignment='center')
fig.text(0, 0.6, f'Serbian: {char}', fontsize=40, language='sr')
fig.text(1, 0.6, f'Russian: {char}', fontsize=40, language='ru',
         horizontalalignment='right')

char = '\U0000014a'
fig.text(0.5, 0.3, f'\\U{ord(char):08x}', fontsize=40, horizontalalignment='center')
fig.text(0, 0.1, f'Inari Sámi: {char}', fontsize=40, language='smn')
fig.text(1, 0.1, f'English: {char}', fontsize=40, language='en',
         horizontalalignment='right')