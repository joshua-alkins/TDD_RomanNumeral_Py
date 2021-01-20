def convertToRomanNumerals(n):
    if type(n) != int:
        raise TypeError("Input must be an integer!")
    
    result=''
    remainder = n

    num_of_100 = remainder//100
    remainder %= 100
    result += 'C'*num_of_100

    if remainder//90 == 1:
        remainder %= 90
        result += 'XL'

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