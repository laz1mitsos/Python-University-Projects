def Sum(string1):

    length = len(string1)
    sum1 = 0
    sum2 = 0

    if (length == 0):
        return 0

    else:
        if (length % 2 == 0):
            last = int(string1[-1])
            sum2 += last
            return sum2 + Sum(string1[:-1])

        else:
            last = int(string1[-1])
            last = 2 * last
            sum3 = last // 10 + last % 10
            sum1 += sum3
            return sum1 + Sum(string1[:-1])

def luhn():
    string1 = input('Enter 16 digit number: ')
    total = Sum(string1)
    if (total % 10 == 0):
        print('valid card')
    else:
        print('invalid card')


def main():
    luhn()

main()

    
            
