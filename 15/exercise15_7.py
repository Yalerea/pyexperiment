"""
    练习15.7 同时掷三个骰子
"""
from random import randint

class Die():
    '''表示一个骰子的类'''
    
    def __init__(self, num_sides=6):
        '''骰子默认为6面的'''
        self.num_sides = num_sides
    def roll(self):
        '''返回一个介于1与骰子面数之间的随机值'''
        return randint(1, self.num_sides)


import plotly.express as px

# 创建三个骰子
die_1 = Die()
die_2 = Die()
die_3 = Die()

# 掷骰子多次，并将结果存储到一个列表中
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(3, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
    
# 可视化结果
title = "Results of Rolling Three D6 Dice 1,000 Times."
labels = {'x':'Result','y':'Frequency of Result'}
fig = px.bar(x=poss_results,y=frequencies,title=title,labels=labels)

# 进一步定制图形
# xaxis_dtick指定x轴上刻度标记的间距，此处设置为1
fig.update_layout(xaxis_dtick=1)

fig.show()

# 可截图保存