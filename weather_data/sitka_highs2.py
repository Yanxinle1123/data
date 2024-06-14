import csv
from datetime import datetime
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

path = Path('weather_data_csv/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# 提取日期和最高温度
dates, highs = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    dates.append(current_date)
    highs.append(high)

# 根据最高温度绘图
plt.style.use('Solarize_Light2')
fig, ax = plt.subplots(figsize=(15, 10))

# 插值并绘制曲线
date_nums = mdates.date2num(dates)
f = interp1d(date_nums, highs, kind='cubic')
date_nums_interp = np.linspace(date_nums.min(), date_nums.max(), len(dates) * 10)
highs_interp = f(date_nums_interp)
ax.plot(mdates.num2date(date_nums_interp), highs_interp, color='red')

# 设置绘制的格式
ax.set_title("Daily High Temperatures, July 2021", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature(F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.savefig('sitka_highs2')
