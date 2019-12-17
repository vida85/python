 #! python3
 # Morse Coder by Davi Silveira

morse_code = {' ': ' | ', 'a': '.-', 'b': '-...',
              'c': '-.-.', 'd': '-..', 'e': '.',
              'f': '..-.', 'g': '--.', 'h': '....',
              'i': '..', 'j': '.---', 'k': '-.-',
              'l': '.-..', 'm': '--', 'n': '-.',
              'o': '---', 'p': '.--.', 'q': '--.-',
              'r': '.-.', 's': '...', 't': '-',
              'u': '..-','v': '...-','w': '.--',
              'x': '-..-','y': '-.--','z': '--..'
              }
coded = ''
msg = input('Enter your message: ').lower()

for char in msg:
    for morse in morse_code.keys():
        if char == morse:
            coded += morse_code[morse] + ' '

print(f'Orginal: {msg}\nCoded: {coded}')
