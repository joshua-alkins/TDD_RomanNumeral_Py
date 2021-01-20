def convertToRomanNumerals(n):
    if type(n) != int:
        raise TypeError("Input must be an integer!")
    
    result=''
    remainder = n

    num_of_1000 = remainder//1000
    remainder %= 1000
    result += 'M'*num_of_1000

    if remainder//900 == 1:
        remainder %= 900
        result += 'CM'

    num_of_500 = remainder//500
    remainder %= 500
    result += 'D'*num_of_500

    num_of_100 = remainder//100
    remainder %= 100

    if num_of_100 == 4:
        result += 'CD'
    else:
        result += 'C'*num_of_100

    if remainder//90 == 1:
        remainder %= 90
        result += 'XC'

    num_of_50 = remainder//50
    remainder %= 50
    result += 'L'*num_of_50

    num_of_10 = remainder//10
    remainder %= 10
    if num_of_10 == 4:
        result += 'XL'
    else:
        result += 'X'*num_of_10

    if remainder == 9:
        remainder = 0
        result += 'IX'

    num_of_5 = remainder//5
    remainder %= 5
    result += 'V'*num_of_5

    if remainder == 4:
        result += 'IV'
    else:
        result += 'I'*remainder

    return result