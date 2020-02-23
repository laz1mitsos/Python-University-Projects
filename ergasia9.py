x = int(input("Give me a number: "))
while x // 10 != 0:
    f = x
    result = 0
    while x>0 :
        digit = x%10
        result = result + digit
        x = x//10
        
    y = f * 3 + 1 + result
    print (y)
    print (result)
    x = int(input("Give me a number: "))

exit()

