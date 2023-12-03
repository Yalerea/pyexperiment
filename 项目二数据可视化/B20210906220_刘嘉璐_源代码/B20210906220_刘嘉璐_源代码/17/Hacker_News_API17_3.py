"""
Hacker News API
"""

# Hacker News最热门文章
# import requests
# import json

# # 执行API调用并存储响应
# url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
# r = requests.get(url)
# print(f"Status code: {r.status_code}")

# # 搜索数据的结构
# response_dict = r.json()
# response_string = json.dumps(response_dict, indent=4)
# print(response_string)






# Hacker News主页上每篇文章
from operator import itemgetter
import requests

# 执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# 处理有关每篇文章的信息
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    # 对于每篇文章，都执行一个API调用
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()
    # print('keys:', response_dict.keys())

    # 对于每篇文章，都创建一个字典
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'] if 'descendants' in response_dict.keys() else None,
    }

    if submission_dict['comments']:
        submission_dicts.append(submission_dict)

# 根据comments将字典中的值降序排列
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")












