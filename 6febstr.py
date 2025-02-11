# str1 = 'Anam Sayyed'
# print(str1.index(0,5))

# li=[10,20,30,'Anam',50,30]
# print(id(li))
# print(type(li))
# print(li.index(10,1))

# Dict:

d1={'name':'anam','age':27,'quali':'BCA'}
d2={'name':'anam','age':27,'quali':'MBA'}
# print(max(d1))
# print(len(d1))
# print(min(d1))

# d2=d1.copy()
# print(d1,d2)

# l1=['name','email,','contatct']
# d2=dict.fromkeys(l1)
# print(d2)
# d3=dict.fromkeys(l1,55)

# print(d1.values())
# print(d1.items())

d1.setdefault('name','sayyed')

print(d1)

d1.update(d2)
print(d1)

