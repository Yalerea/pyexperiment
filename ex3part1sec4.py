# 4.1
pizzas = ['fruit','chicken','spicy']
for pizza in pizzas:
    print(pizza)
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I really love pizza!")

# 4.2
animals = ['fish','dog','duck']
for animal in animals:
    print(animal)
for animal in animals:
    print(f"A {animal} would make a great pet.")
print("Any of these animals would swim.")

# 4.3
for i in range(1,21):
    print(i)

# 4.4
num = list(range(1,1000001))
# for i in num:
#     print(i)

# 4.5
num = list(range(1,1000001))
print(min(num))
print(max(num))
print(sum(num))

# 4.6
num = list(range(1,20,2))
for i in num:
    print(i)

# 4.7
num7 = list(range(0,31,3))
for i in num7:
    print(i)

# 4.8
cube = []
for i in range(1,11):
    cube.append(i**3)
for j in cube:
    print(j)

# 4.9
cube = [i**3 for i in range(1,11)]
print(cube)

# P56
me = ['aa','cc','ff']
your = me[:]
you = me
me.append('dd')
you.append('oo')
your.append('ii')
print(me)
print(you)
print(your)

# 4.10
cube = [i**3 for i in range(1,11)]
print(cube)
print("The first three items in the list are:")
print(cube[:3])
print("Three items from the middle of the list are:")
print(cube[4:7])
print("The last three items in the list are:")
print(cube[-3:])

# 4.11
pizzas = ['fruit','chicken','spicy']
for pizza in pizzas:
    print(pizza)
for pizza in pizzas:
    print(f"I like {pizza} pizza.")
print("I really love pizza!")  ###
friend_pizza = pizzas[:]
pizzas.append('onion')
friend_pizza.append('cabbage')
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)
print("My friend's favorite pizzas are:")
for pizza in friend_pizza:
    print(pizza)

# 4.12
food = ['pizza','falafel','carrot cake']
friend_food = food[:]
for f in food:
    print(f)
for ff in friend_food:
    print(ff)

# 4.13
food = ('tea','egg','fish','beef','noodle')
for i in food:
    print(i)
# food[0] = 'chinken'
food = ('chicken','egg','fish','rice','noodle')
for i in food:
    print(i)
