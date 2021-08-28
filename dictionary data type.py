#dictionary data type
d={1:'Banana',2:'Mango'}
print("Dictionary=",d)
print("Dictionary value using key d[1]=",d[1])
print("Dictionary value using get()=",d.get(2))
d[1]="Dragon fruits"
print("Dictionary value update=",d[1])
d[3]="Banana"
print("Dictionary=",d)
print("d.items():",d.items())
print("d.keys():",d.keys())
print("d.values():",d.values())
d.pop(3)
print("Dictionary=",d)
d.clear()
print("Dictionary=",d)
del d