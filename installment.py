a=161258
 #installments for 3 years
e3=a/36
#installments for 5 years
e5=a/60
#installments for 3 years with 5% interest
emi3=e3+(0.05*e3)
#installments for 5 years with 5% interest
emi5=e5+(0.05*e5)
print("EMI for 3 years with interest 5%",emi5)
print("EMI for 5 years with interest 5%",emi3)