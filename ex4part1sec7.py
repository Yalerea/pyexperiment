# 7.1
# message = input("What kind of cars would you like?")
# print(f"Let me see if I can find you a {message}.")

# 7.2
# message = input("How many customers?")
# message = int(message)
# if message >8:
#     print("No seat.")
# else:
#     print("There are seats.")

# 7.3
# num = input("number:")
# num = int(num)
# if num%10==0:
#     print("能被十整除。")
# else:
#     print("不能被十整除。")

# 7.4
# message = ""
# while message != "quit":
#     message = input("Please add:")
#     if message != "quit":
#         print(f"Pizza add {message}")
        
# 7.5
# while True:
#     age = input("How old are you?")
#     age = int(age)
#     if age<3:
#         print("free")
#     elif age<12:
#         print("10 dollars")
#     else:
#         print("15 dollars")

# 7.6
# while True:
#     active = input("What do you want to add?")
#     if active != "quit":
#         print(f"Pizza add {active}")
#     else:
#         break
# message = ""
# while message != "quit":
#     message = input("Please add:")
#     if message != "quit":
#         print(f"Pizza add {message}")
# 7.7
# while 1:
#     print(111111111111111)
    
# 7.8
# sandwich_orders = ['milk','sugar','fruit','egg']
# finished_sandwiches = []
# while sandwich_orders:
#     now = sandwich_orders.pop()
#     print(f"I made you {now} sandwich.")
#     finished_sandwiches.append(now)
# print(finished_sandwiches)

# 7.9
# sandwich_orders = ['milk','pastrami','sugar','pastrami','pastrami','fruit','egg']
# print("The pastrami sandwich has been sold out.")
# while 'pastrami' in sandwich_orders:
#     sandwich_orders.remove('pastrami')
# print(sandwich_orders)

# 7.10
places = []
dream = ""
while True:
    dream = input("If you could visit one place in the world,where would you go?")
    if dream != "quit":
        places.append(dream)
    else:
        break
print(places)
