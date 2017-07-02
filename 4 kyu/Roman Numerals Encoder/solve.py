def solution(number):
    roman_numbers = ["M", "CMXC", "CM", "D", "CDXC", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    arab = [1000, 990, 900, 500, 490, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    result = ''
    i = 0
    while number > 0 or len(arab) == (i - 1):
        while (number - arab[i]) >= 0:
            number -= arab[i]
            result += roman_numbers[i]
        i += 1
    return result
