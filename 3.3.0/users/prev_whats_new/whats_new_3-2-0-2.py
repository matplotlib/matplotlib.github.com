import matplotlib.pyplot as plt

# Use new kerning values:
plt.rcParams['text.kerning_factor'] = 0
fig, ax = plt.subplots()
ax.text(0.0, 0.05, 'BRAVO\nAWKWARD\nVAT\nW.Test', fontsize=56)
ax.set_title('After (text.kerning_factor = 0)')