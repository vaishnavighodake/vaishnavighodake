#wap to manipulate tuple data 
s=("Python",2021,'oop','2003','vaishu',22.7,4000,2506,'v','vsg')
print('extract all list',s)
print('index number 2 to 5',s[2:5])
print('reverse element',s[::-1])
g=list(s)
g.append('vsg')
s=tuple(g)
print("After add an element",s)
g.remove('vsg')
s=tuple(g)
print("After delete an element",s)