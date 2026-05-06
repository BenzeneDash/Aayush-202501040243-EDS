import math as m
n = int(input())

if(n>0 and n<=9):
    print(f"{int(m.pow(n,2))}\n")
elif(n>=10 and n<=99):
    print(f"{m.sqrt(n):.2f}\n")
elif(n>=100 and n<=999):
    print(f"{m.cbrt(n):.2f}\n")
else:
    print("Invalid")  

