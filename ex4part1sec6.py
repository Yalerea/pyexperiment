# 6.1
people = { 'first_name':'Taylor','last_name':'Swift','age':22,'city':'NewYork'}
print(people)

# 6.2
num={'a':3,'b':4, 'c':5,'d':6, 'e':7}
print(num)

# 6.3
dic = {'code':'代码','dic':'字典','item':'迭代器','algorithmn':'算法','list':'列表'}
print(dic)

# 6.4
dic = {'code':'代码','dic':'字典','item':'迭代器','algorithmn':'算法','list':'列表'}
for key,value in dic.items():
    print(key,value)
dic['sort']='排序'
dic['del']='删除'
dic['add']='添加'
dic['remove']='删除'
dic['append']='添加'
for key,value in dic.items():
    print(key,value)
    
# 6.5
river = {'nile':'egypt','yangtze':'china','mississippi':'usa'}
for k,v in river.items():
    print(f"The {k.title()} runs through {v.title()}.")
    print(k.title())
    print(v.title())
    
# 6.6
visitor = ['jen','sarah','ivy','john']
favorite_language = {'jen':'python','sarah':'c','edward':'rust','phil':'python'}
for k,v in favorite_language.items():
    if k in visitor:
        print(f"{k.title()}, thank you for coming!")
    else:
        print(f"{k.title()}, can you participate in?")
        
# 6.7
people1 = { 'first_name':'Taylor','last_name':'Swift','age':22,'city':'NewYork'}
people2 = { 'first_name':'aa','last_name':'ss','age':12,'city':'London'}
people3 = { 'first_name':'rr','last_name':'ww','age':23,'city':'Beijing'}
people = [people1,people2,people3]
for i in people:
    print(i)
    
# 6.8
a = {'type':'dog','hostname':'June'}
b = {'type':'cat','hostname':'Ivy'}
c = {'type':'fish','hostname':'Jack'}
pets = [a,b,c]
for i in pets:
    print(i)
    
# 6.9
favorite_places = {
    'jen':['san francisco','texas','london'],
    'sarah':['paris','tokyo'],
    'edward':['chicago'],
}
favorite_places['sarah'].append('seattle')
for k,v in favorite_places.items():
    print(f"{k.title()}'s favorite places are:")
    for i in v:
        print(i.title())

# 6.10
num={'a':[3,1,5],'b':[5,6], 'c':[10,4,8],'d':[5], 'e':[22,11,0]}
for k,v in num.items():
    print(f"{k.title()}")
    for i in v:
        print(i)

# 6.11
cities = {
    'NewYork':{'country':'USA','population':10000000,'fact':'New York is the capital of USA'},
    'London':{'country':'UK','population':10000000,'fact':'London is the capital of UK'},
    'Beijing':{'country':'China','population':10000000,'fact':'Beijing is the capital of China'}
}
for k,v in cities.items():
    print(f"{k.title()}")
    print(f"{v['country']}")
    print(f"{v['population']}")
    print(f"{v['fact']}")
    print('\n')
    
# 6.12
num={'a':3,'b':4, 'c':5,'d':6, 'e':7}
print(num)
num['a']=9
num['v']=8
for k,v in num.items():
    print(k.title())
    print(v)