def febList(n):

    if(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return febList(n-1) + febList(n-2)

a = int(input("Enter your number: "))
print(febList(a-1))