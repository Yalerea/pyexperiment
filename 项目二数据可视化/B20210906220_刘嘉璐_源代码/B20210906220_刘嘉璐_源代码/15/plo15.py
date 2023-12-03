# 1
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
    
'''
# 创建一个D6
die = Die()

# 掷几次骰子并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# print(results)

# 分析结果
frequencies = []
poss_results = range(1,die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
    
print(frequencies)
'''


import plotly.express as px

# from die import Die

# 创建一个D6
die = Die()

# 掷几次骰子并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
poss_results = range(1,die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
title = "Results of rolling one D6 1000 times."
labels = {'x':'Result','y':'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies,title = title,labels = labels) # px.bar()直方图
# fig = px.scatter(x=poss_results, y=frequencies) # px.scatter()散点图
# fig = px.line(x=poss_results, y=frequencies) # px.line()折线图

fig.show()                              
"""





#2 两个骰子
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
# from die import Die

# 创建两个骰子
# die_1 = Die()
# die_2 = Die()

# 创建一个D6和一个D10
die_1 = Die()
die_2 = Die(10)

# 掷骰子多次，并将结果存储到一个列表中
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
    
# 可视化结果
# title = "Results of Rolling Two D6 Dice 1,000 Times."
title = "Results of Rolling a D6 and a D10 50,000 Times."
labels = {'x':'Result','y':'Frequency of Result'}
fig = px.bar(x=poss_results,y=frequencies,title=title,labels=labels)

# 进一步定制图形
# xaxis_dtick指定x轴上刻度标记的间距，此处设置为1
fig.update_layout(xaxis_dtick=1)

fig.show()
fig.write_html('dice_visual_d6d10.html')

