 #! python3
 # Morse Coder by Davi Silveira

morse_code = {' ': ' | ', 'a': '.-', 'b': '-...', 'c': '-.-.',
              'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
              'h': '....', 'i': '..', 'j': '.---', 'k': '-.-',
              'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
              'p': '.--.', 'q': '--.-','r': '.-.', 's': '...',
              't': '-','u': '..-','v': '...-','w': '.--',
              'x': '-..-', 'y': '-.--','z': '--..'}

coded = ''
msg = input('Enter your message: ').lower()

for char in msg:
    if char in morse_code.keys():
        coded += morse_code[char] + ' '

print(f'Orginal: {msg}\nCoded: {coded}')
