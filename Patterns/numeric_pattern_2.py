# print left angled traingle 

n = int(input("enter your number: "))

for i in range(1, n+1):
    print(" "*n,end = "")
    n-=1
    print(str(i)*i)
