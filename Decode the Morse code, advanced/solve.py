import re

MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C',
    '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I',
    '.---': 'G', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U',
    '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z', '-----': '0',
    '.----': '1', '..---': '2', '...--': '3',
    '....-': '4', '.....': '5', '-....': '6',
    '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?',
}


def decodeBits(bits):
    bits = bits.strip('0')
    rate = get_rate(bits)

    morse_code = ''
    for word in bits.split('0'*7*rate):
        for letter in word.split('0'*3*rate):
            for dot in letter.split('0'*rate):
                morse_code += '-' if len(dot) > rate else '.'
            morse_code += ' '
        morse_code += '  '

    return morse_code.strip()


def get_rate(bits):
    regex = re.compile('1+|0+')
    chars = regex.findall(bits)
    rate = len(min(chars, key=len))
    return rate


def decodeMorse(morse_code):
    result = ''
    for word in morse_code.strip().split('   '):
        for letter in word.split(' '):
            result += MORSE_CODE[letter]
        result += ' '
    return result.strip()
