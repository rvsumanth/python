#print number pyramid

n = int(input('Enter your number: '))

for i in range(1, n+1):
    print(" "*(n-i),end = " ")
    for j in range(1, i+1):
        print(i, end =" ")
    print()
