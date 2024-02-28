import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# 三次样条插值
cs = CubicSpline(input_values, squares)

# 生成插值数据点
x = np.linspace(min(input_values), max(input_values), num=100)
y = cs(x)

# 设置图的样式
plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()

# 绘制折线图（蓝线）
ax.plot(x, y, linewidth=3)

# 绘制散点图（红点）
ax.scatter(input_values, squares, color='red', marker='o', zorder=3)

# 设置图题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 设置刻度标记的样式
ax.tick_params(labelsize=10)

plt.show()
