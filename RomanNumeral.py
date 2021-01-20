# I=1, V=5, X=10, L=50, C=100, D=500, M=1000

def convertToRomanNumerals(n):
    if type(n) != int:
        raise TypeError("Input must be an integer!")

    conversions = [(50,'L'),(10,'X'),(5,'V'),(1,'I')]

    result = ''
    carry = n

    for i in range(len(conversions)):
        num = conversions[i][0]
        numeral = conversions[i][1]

        number_of_numerals = carry // num 
        carry = carry%num

        result += numeral * number_of_numerals

        if carry == num-1 and carry != 0 and num <= 10:
            carry = 0
            result += 'I'+numeral


    return result
