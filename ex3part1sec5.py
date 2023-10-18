# 5.1
car = 'aaa'
print("Is car == 'aa'?False.")
print(car == 'aa')
print("\nIs car == 'aaa'?True")
print(car == 'aaa')
print("\nIs car == 'Aaa'?True")
print(car.title() == 'Aaa')

# 5.2
a = 'aaa'
b = 'bbb'
print(a == b)
print(a != b)

c = 'Aaa'
print(a == c)
print(a.lower() == c)

print(3 == 5)
print(3 != 5)
print(3 > 5)
print(3 < 5)
print(3 >= 5)
print(3 <= 5)

print(3 == 3 and 5 > 3)
print(5 == 3 or 5 < 8)

print('a' in a)
print('b' not in a)
print('A' in c)
print('v' not in c)

# 5.3
alien_color = 'green'
if alien_color == 'green':
    print("5")
if alien_color == 'green':
    pass

# 5.4
alien_color = 'green'
if alien_color == 'green':
    print("5")
else:
    print("10")

# 5.5
alien_color = 'green'
if alien_color == 'green':
    print("5")
elif alien_color == 'yellow':
    print("10")
else:
    print('15')

# 5.10
current_users = ['a', 'C', 'bb', 'cCc', 'ddd']
new_users = ['m', 'n', 'ss', 'a', 'ccc']
user = []
for i in current_users:
    user.append(i.lower())
for j in new_users:
    if j in current_users:
        print("change it.")
    else:
        print("you can use.")

nums = list(range(1, 10))
for num in nums:
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    else:
        print(f"{num}th")
