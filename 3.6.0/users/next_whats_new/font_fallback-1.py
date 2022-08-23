import matplotlib.pyplot as plt

text = "There are 几个汉字 in between!"

plt.rcParams["font.size"] = 20
fig = plt.figure(figsize=(4.75, 1.85))
fig.text(0.05, 0.85, text, family=["WenQuanYi Zen Hei"])
fig.text(0.05, 0.65, text, family=["Noto Sans CJK JP"])
fig.text(0.05, 0.45, text, family=["DejaVu Sans", "Noto Sans CJK JP"])
fig.text(0.05, 0.25, text, family=["DejaVu Sans", "WenQuanYi Zen Hei"])

plt.show()