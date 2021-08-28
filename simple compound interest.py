a=161258
r=5
t=1
si=a*r*t*0.01
print("simple interest is:",si)
Amount=a*(pow(1+r/100),t)
ci=Amount-a 
print("compound interest is:",ci)