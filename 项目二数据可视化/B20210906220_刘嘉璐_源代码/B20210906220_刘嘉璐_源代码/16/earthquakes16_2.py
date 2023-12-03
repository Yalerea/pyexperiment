"""
16.2 制作全球地震散点图
"""
from pathlib import Path
import json
import plotly.express as px

# 将数据作为字符串读取并转换为Python对象
path = Path('16\eq_data_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# 将数据文件转换为更易于阅读的版本
path = Path('16\eq_data_1_day_m1.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)

# 查看数据集中的所有地震
all_eq_dicts = all_eq_data['features']
# print(len(all_eq_dicts))

mags,titles,lons,lats = [],[],[],[]
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)
    
print(mags[:10])  # 震级
print(titles[:2])  # 标题
print(lons[:5])  # 经度
print(lats[:5])  # 纬度


# 以300dpi为例，就是2.54cm*2.54cm的单位面积上有300*300个像素点，
# 把像素当成一个个小点。像素点在图片上是均匀分布的，
# 一寸照的尺寸为2.5cm*3.5cm，
# 在宽度上能放下300*2.5/2.54=295px个像素点，
# 那么长度上像素是300*3.5/2.54=413px，则一寸照的像素是413px*295px。

# 创建fig实例
'''
fig = px.scatter(
    x=lons,   # 经度
    y=lats,   # 纬度
    labels={'x':'经度','y':'纬度'},
    range_x=[-200,200],  # 扩大空间，完整显示+-180附近的地震点
    range_y=[-90,90],
    width=800,  # 宽度800像素
    height=800,  # 高度800像素
    title='全球地震散点图',  # 标题
)
fig.write_html('global_earthquakes.html')
fig.show()
'''

import pandas as pd
data = pd.DataFrame(
    data=zip(lons,lats,titles,mags),columns=['经度','纬度','位置','震级']
)
data.head()
fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200,200],  # 扩大空间，完整显示+-180附近的地震点
    range_y=[-90,90],
    width=800,  # 宽度800像素
    height=800,  # 高度800像素
    title='全球地震散点图',  # 标题
    size='震级',  # data中的'震级'字段提供给size参数指定散点图中每个标记的尺寸
    size_max=10,  # 最大显示尺寸
    color='震级',
    color_continuous_scale='Viridis',  # 设置不同震级的渐变颜色
    hover_name='位置',
)
fig.write_html('global_earthquakes.html')
fig.show()







