#Printing indexes of the prime numbers in a list:

l=[79,97,200,3,5,12,101]

for n in range(len(l)):
    if l[n]<2:
        pass
    else:
        for i in range(2,l[n]):
            if l[n]%i==0:
                break
        else:
            print(n,end=" ")
# OUTPUT:
# 0 1 3 4 6 
 
# given password is strong or not:
# ipper 65-90 lower 97-122 num 48-57

pwd=input("Enter your password:")

if len(pwd)<8:
    print("Not a strong password...")
else:
    upper=lower=num=spl=False
    for i in pwd:
        if ord(i)>=65 and ord(i)<=90:
            upper=True
        elif ord(i)>=97 and ord(i)<=122:
            lower=True
        elif ord(i)>=48 and ord(i)<=57:
            num=True
        else:
            spl=True
    if upper and lower and num and spl:
        print("Strong password...")

# OUTPUT:
# Enter your password:Manjunadh@02
# Strong password...

# right aligned triangle:

n=int(input("Enter n value:"))

for i in range(1,n+1):
    for space in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

# OUTPUT:
# Enter n value:6
#           * 
#         * * 
#       * * * 
#     * * * * 
#   * * * * * 
# * * * * * * 