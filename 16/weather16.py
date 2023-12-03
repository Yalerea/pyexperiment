"""
CSV文件格式，绘制天气数据的折线图
"""
from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('16\san_francisco_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# 提取日期和最高温度
dates,highs,lows = [],[],[]
for row in reader:
    current_date = datetime.strptime(row[1],'%Y-%m-%d')
    try:
        high = int(row[2])
        low = int(row[3])
    except ValueError:
        print(f"Missing data of {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# 根据最高温度绘图
plt.style.use('seaborn-v0_8')
fig,ax = plt.subplots()
ax.plot(dates,highs,color='red',alpha = 0.5)
ax.plot(dates,lows,color='blue',alpha = 0.5)
ax.fill_between(dates,highs,lows,facecolor='blue',alpha=0.1)

# 设置绘图格式
title = "Daily High and Low Temperatures, 2021\nSan Francisco"
ax.set_title(title,fontsize=20)
ax.set_xlabel('Date',fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)",fontsize=16)
ax.tick_params(labelsize=16)

plt.show()







