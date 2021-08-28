#wap to manipulate list data used in program
x=[10,'PQR',1.5,20,30j,40,50,60,70,80]
print("list x=",x)
print("list index 2 to 5=",x[2:5])
x.append(90)
print("element add at least =",x)
x.pop(2)
print("after pop:",x)
print("reverse elements:",x[::-1])
x.clear()
print("After clear:",x)
