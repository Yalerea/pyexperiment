# 1
"""
import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
input_values = [1,2,3,4,5]

plt.style.use('seaborn-v0_8')
# plt.style.use('ggplot')
fig, ax = plt.subplots()
ax.plot(input_values,squares,linewidth=3)


# 设置图题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 设置刻度标记的样式
ax.tick_params(labelsize=14)

plt.show()

"""




# 2
"""
import matplotlib.pyplot as plt

# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]
x_values = range(1,1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
# ax.scatter(x_values,y_values,color='red',s=10)
# ax.scatter(x_values,y_values,color=(0,0,0.9),s=10)
ax.scatter(x_values,y_values,c=y_values,cmap=plt.cm.Blues,s=10)
# ax.scatter(x_values,y_values,s=10)


# 设置图题并给坐标轴加上标签
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# 设置每个坐标轴的取值范围
ax.axis([0,1100,0,1_100_000])
ax.ticklabel_format(style='plain')

# 设置刻度标记的样式
# ax.tick_params(labelsize=14)

plt.savefig('squares_plot.png',bbox_inches='tight')
# plt.show()

"""





# 3
"""
from random import choice
class RandomWalk():
        '''一个生成随机游走数据的类'''
    def __init__(self,num_points=5000):
        '''初始化随机游走的数据'''
        self.num_points = num_points
        
        # 所有随机游走都始于(0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''计算随机游走包含的所有点'''
        
        # 不断游走，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            
            # 决定前进的方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            
            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            
            # 计算下一个点的x坐标值和y坐标值
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step
            
            self.x_values.append(x)
            self.y_values.append(y)



import matplotlib.pyplot as plt
# from random_walk import RandomWalk

'''
# 创建一个RandomWalk实例
rw = RandomWalk()
rw.fill_walk()

# 将所有的点都绘制出来
plt.style.use('classic')
fig,ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
ax.set_aspect('equal')  # 指定两条轴上刻度的间距必须相等
plt.show()
'''

# 只要程序处于活动状态，就不断地模拟随机游走
while True:
    # 创建一个RandomWalk实例
    rw = RandomWalk(50_000)
    rw.fill_walk()
    
    # 将所有的点都绘制出来
    plt.style.use('classic')
    # figsize = (15,9) 调整Matplotlib输出的图形尺寸
    fig,ax = plt.subplots(figsize = (15,9))
    point_numbers = range(rw.num_points)
    # 传递实参edgecolors = 'none'以删除每个点的轮廓
    # 最终的随机游走图从浅蓝色渐变为深蓝色，准确地指出从起点游走到终点的路径
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
        edgecolors = 'none', s=1)
    # ax.scatter(rw.x_values, rw.y_values, s=15)
    ax.set_aspect('equal')  # 指定两条轴上刻度的间距必须相等
    
    # 突出起点和重点
    ax.scatter(0, 0, c='green', edgecolors='none', s=10)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
        s=10)
    
    
    # 隐藏坐标轴
    # ax.get_xaxis()/ax.get_yaxis()方法获取每条坐标轴
    # 链式调用：调用完一个函数后还能再继续调用其它函数
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
    
"""









# 4
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









# 5 两个骰子
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

# fig.show()
fig.write_html('dice_visual_d6d10.html')






# 练习15.7
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






