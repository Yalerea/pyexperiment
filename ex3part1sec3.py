# 3.1
names = ['张三','李四','王五']
for name in names:
    print(name)

# 3.2
names = ['张三','李四','王五']
for name in names:
    print(f"{name}，你好！")

# 3.3
commutes = ['Honda motorcycle','walk']
for commute in commutes:
    print(f"I would like to own a {commute}.")

# 3.4
people = ['小a','小b','小c']
print(f"I want to have a dinner with {people[0]}、{people[1]}、{people[2]}.\n")

# 3.5
people = ['小a','小b','小c']
print(f"I want to have a dinner with {people[0]}、{people[1]}、{people[2]}.")
print(f"{people[1]} can not participate in the dinner.")
people[1] = '小h'
print(f"I want to have a dinner with {people[0]}、{people[1]}、{people[2]}.\n")

# 3.6
people = ['小a','小b','小c']
print(f"I want to have a dinner with {people[0]}、{people[1]}、{people[2]}.")
print(f"{people[1]} can not participate in the dinner.")
people[1] = '小h'
print(f"I want to have a dinner with {people[0]}、{people[1]}、{people[2]}.")
print("I have found a larger table to have a dinner.")
people.insert(0,'小s')
people.insert(len(people)//2,'小w')
people.append('小z')
print(f"I want to have a dinner with {people[0]}、{people[1]}、{people[2]}、{people[3]}、{people[4]}、{people[5]}.\n")

# 3.7
people = ['小a','小b','小c']
print(f"I want to have a dinner with {people[0]}、{people[1]}、{people[2]}.")
print(f"{people[1]} can not participate in the dinner.")
people[1] = '小h'
print(f"I want to have a dinner with {people[0]}、{people[1]}、{people[2]}.")
print("I have found a larger table to have a dinner.")
people.insert(0,'小s')
people.insert(len(people)//2,'小w')
people.append('小z')
print(f"I want to have a dinner with {people[0]}、{people[1]}、{people[2]}、{people[3]}、{people[4]}、{people[5]}.\n")
print("I am sorry to inform you that there is only two seats for guests.")
while(len(people)>2):
    h = people.pop()
    print(f"{h},I am sorry that I can not have a dinner with you this time.")
print(f"{people[0]},{people[1]},you are still invited.")
del people[1]
del people[0]
print(f"The content is here,{people}.")

# 3.8
pla = ['Paris','England','US','Australia','Singapore']
print(pla)
print(sorted(pla))
print(pla)
print(sorted(pla,reverse=True))
print(pla)
pla.reverse()
print(pla)
pla.reverse()
print(pla)
pla.sort()
print(pla)
pla.sort(reverse=True)
print(pla)

# 3.9
people = ['小a','小b','小c'] #3.4
print(f"I want to have a dinner with {people[0]}、{people[1]}、{people[2]}.")
print(len(people))

# 3.10
ev = ['mountain','lake','trees','moon','river','city']
print(ev[0])
print(ev[0].title())
print(ev[-1])
print(f"The list is {ev}.")
ev[0] = 'star'
print(ev)
ev.append('bear')
print(ev)
ev.insert(0,'ivy')
print(ev)
del ev[0]
print(ev)
ev.pop(-1)
print(ev)
ev.remove('city')
print(ev)
eve = ev
eve.sort()
print(eve)
eve.sort(reverse=True)
print(eve)
print(sorted(ev,reverse=True))
ev.reverse()
print(ev)
print(len(ev))

# 3.11
# print(ev[5]) # IndexError: list index out of range
print(ev[-1])


