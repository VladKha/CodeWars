class RomanNumerals:
    @staticmethod
    def to_roman(n):
        roman_numbers = ["M", "CMXC", "CM", "D", "CDXC", "CD", "C", "XC", "L", "XL", "X", "IX", "V",
                         "IV", "I"]
        arab = [1000, 990, 900, 500, 490, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ''
        i = 0
        while n > 0 or len(arab) == (i - 1):
            while n - arab[i] >= 0:
                n -= arab[i]
                result += roman_numbers[i]
            i += 1
        return result

    @staticmethod
    def from_roman(roman):
        roman_numbers = {
            'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9,
            'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'D': 500, 'CM': 900, 'M': 1000
        }
        n = 0
        i = len(roman)
        while roman:
            s = roman[:i + 1]
            d = roman_numbers.get(s)
            if d:
                n += d
                roman = roman[i + 1:]
                i = len(roman)
            else:
                i -= 1
        return n
