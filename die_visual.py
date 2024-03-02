import matplotlib.pyplot as plt
from LeleDrawDesigns.line_chart import LineChart

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
plt.bar(poss_results, frequencies)
plt.title('Results of Rolling One D6 1,000 Times', fontsize=20)
plt.xlabel('Result', fontsize=15)
plt.ylabel('Frequency of Result', fontsize=15)
plt.show()

input_values = []
for i in range(len(frequencies)):
    input_values.append(i + 1)
straight_line_chart = LineChart(input_values=input_values, squares=frequencies, style='straight',
                                skin='Solarize_Light2')
curved_line_chart = LineChart(input_values=input_values, squares=frequencies, style='curved', skin='Solarize_Light2')
