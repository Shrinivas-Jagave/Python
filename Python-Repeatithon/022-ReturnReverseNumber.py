def ReturnReverseNumber(num):
    if num > 0:
        while num != 0:
            r = num % 10
            print(r,end='')
            num = num // 10
    else: 
        print("This is only for positive number please enter a positive number")

num = int(input("Enter a number : "))
ReturnReverseNumber(num)
