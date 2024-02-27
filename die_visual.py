import matplotlib.pyplot as plt

from die import Die

# 创建一个D6
die = Die()

# 掷几次骰子并将结果存储在一个列表里
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
poss_results = range(1, die.num_sides + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# 对结果进行可视化
plt.bar(poss_results, frequencies, edgecolor='black')
plt.show()
