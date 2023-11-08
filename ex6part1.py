# 1
def display_message():
    print("function")
display_message()

# 2
def favorite_book(title):
    print(f"One of my favorite books is {title}.")
favorite_book("Alice in Wonderland")

# 3
def make_shirt(size,message):
    print(f"The size is {size},the message is {message}.")
make_shirt('M','great')
make_shirt(message='great',size='M')

# 4
def make_shirt(size,message="I love Python"):
    print(f"The size is {size},the message is {message}.")
make_shirt('L')
make_shirt(size='M')
make_shirt(message='great',size='L')

# 5
def describe_city(city='Beijing',country='China'):
    print(f"{city} is in {country}.")
describe_city('Beijing')
describe_city('Shanghai')
describe_city('NewYork','USA')

# 6
def city_country(city,country):
    mix=f"\"{city},{country}\""
    return mix

print(city_country('Beijing','China'))
print(city_country('Shanghai','China'))
print(city_country('NewYork','USA'))

# 7
def make_album(singer,album,num=None):
    mix = {'singer':singer,'album':album}
    if num:
        mix['num'] = num
    return mix

mixx1 = make_album('Jay Chou','Fantasy')
print(mixx1)
mixx2 = make_album(album='die young',singer='Beatles')
print(mixx2)
print(make_album('John',album='sing'))
print(make_album('John',album='sing',num=10))

# # 8
# def make_album(singer,album):
#     mix = {'singer':singer,'album':album}
#     return mix

# while True:
#     print("Please tell me the singer and the album.")
#     print("Enter 'q' to quit.")
    
#     mix81 = input("Singer:")
#     if mix81 == 'q':
#         break
#     mix82 = input("Album:")
#     if mix82 == 'q':
#         break
    
#     print(make_album(mix81,mix82))

# 9
def show_message(messages):
    for message in messages:
        print(message)

messages = ['hello','world','python']
show_message(messages)

# 10
def show_message(messages):
    for message in messages:
        print(message)

def send_message(messages):
    sent_messages = []
    while messages:
        sent_messages.append(messages.pop())
    return sent_messages

messages = ['hello','world','python']
show_message(messages)
remessages = send_message(messages)
print(messages)
print(remessages)

# 11
def show_message(messages):
    for message in messages:
        print(message)

def send_message(messages):
    sent_messages = []
    while messages:
        sent_messages.append(messages.pop())
    return sent_messages

messages = ['hello','world','python']
show_message(messages)
remessages = send_message(messages[:])
print(messages)
print(remessages)

# 12
def make_sandwich(*foods):
    print("You ordered:")
    for food in foods:
        print(f"- {food}")

make_sandwich('egg','bread','tomato')
make_sandwich('milk','sugar')
make_sandwich('vegetables')

# 13
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last    
    return user_info

user_profile = build_profile('Jl', 'L', 
                            university='ccsu', 
                            field='cs',
                            sex='female')
print(user_profile)

# 14
def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

car_info = make_car('ford', 'focus', color='blue', tow_package=True)
print(car_info)

# 15
# import printing_functions as pf
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# pf.print_models(unprinted_designs, completed_models)
# pf.show_completed_models(completed_models)

# 16
# import printing_functions
# from printing_functions import make_sandwich
# from printing_functions import make_sandwich as ms
# import printing_functions as pf
from printing_functions import *

make_sandwich('apple','bread')



