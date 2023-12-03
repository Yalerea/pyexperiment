"""
    练习16.3 旧金山
    San Francisco Comparison
"""
from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt


def get_weather_data(path, dates, highs, lows, date_index, high_index,
        low_index):
    """得到文件中最低温度和最高温度"""
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)

    # 提取日期，最高温和最低温
    for row in reader:
        current_date = datetime.strptime(row[date_index], '%Y-%m-%d')
        try:
            high = int(row[high_index])
            low = int(row[low_index])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 获取锡特卡的天气数据。
path = Path('16\sitka_weather_2021_simple.csv')
dates, highs, lows = [], [], []
get_weather_data(path, dates, highs, lows, date_index=2, high_index=4,
        low_index=5)

# 绘制锡特卡的天气数据。
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.3)
ax.plot(dates, lows, color='blue', alpha=0.3)
ax.fill_between(dates, highs, lows, facecolor='red', alpha=0.2)

# 获取死亡谷的天气数据。
path = Path('16\death_valley_2021_simple.csv')
dates, highs, lows = [], [], []
get_weather_data(path, dates, highs, lows, date_index=2, high_index=3,
        low_index=4)

# 将死亡谷天气数据添加到当前绘图中。
ax.plot(dates, highs, color='red', alpha=0.3)
ax.plot(dates, lows, color='blue', alpha=0.3)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)

# 获取旧金山的天气数据。
path = Path('16\san_francisco_2021_simple.csv')
dates, highs, lows = [], [], []
get_weather_data(path, dates, highs, lows, date_index=1, high_index=2,
        low_index=3)

# 将旧金山天气数据添加到当前绘图中。
ax.plot(dates, highs, color='yellow', alpha=0.7)
ax.plot(dates, lows, color='green', alpha=0.6)
ax.fill_between(dates, highs, lows, facecolor='green', alpha=0.3)

# 设置绘图格式。
title = "Daily high and low temperatures - 2021"
title += "\nSitka, AK , Death Valley, CA and San Francisco, CA"
ax.set_title(title, fontsize=20)
ax.set_xlabel('Date', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)
ax.set_ylim(10, 140)

plt.show()