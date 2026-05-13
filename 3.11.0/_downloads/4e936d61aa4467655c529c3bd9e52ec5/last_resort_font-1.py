text_raw = r"'\N{Bengali Digit Zero}\N{Hiragana Letter A}\ufdd0'"
text = eval(text_raw)
sizes = [
    (0.85, 8),
    (0.80, 10),
    (0.75, 12),
    (0.70, 16),
    (0.63, 20),
    (0.55, 24),
    (0.45, 32),
    (0.30, 48),
    (0.10, 64),
]

fig = plt.figure()
fig.text(0.01, 0.90, f'Input: {text_raw}')
for y, size in sizes:
    fig.text(0.01, y, f'{size}pt:{text}', fontsize=size)