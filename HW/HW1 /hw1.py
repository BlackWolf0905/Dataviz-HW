import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 500)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) * np.cos(x)

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(x, y1, label='sin(x)', color='blue', linestyle='-', linewidth=2)
ax.plot(x, y2, label='cos(x)', color='red', linestyle='--', linewidth=2)
ax.plot(x, y3, label='sin(x) * cos(x)', color='green', linestyle='-.', linewidth=2)

ax.fill_between(x, y1, y2, color='purple', alpha=0.2, label='Diện tích giữa sin và cos')

ax.set_title('Biểu đồ lượng giác')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.legend()
ax.grid(True, linestyle='--', alpha=0.5)

plt.show()