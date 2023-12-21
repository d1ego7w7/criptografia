import re
import string
import random

#CIFRADO ATBASH
def atbash_cipher(text):
    result = ''
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(90 - (ord(char) - 65))
            else:
                result += chr(122 - (ord(char) - 97))
        else:
            result += char
    return result

#CIFRADO ROT13            
def rot13_cipher(text):
    result = ''
    for char in text:
        if char.isalpha():
            shift = 13 if char.islower() else 13
            result += chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a' if char.islower() else 'A'))
        else:
            result += char
    return result

#CODIGO VIGENERE
def vigenere_cipher(text, key):
    result = ''
    key_length = len(key)
    for i in range(len(text)):
        char = text[i]
        if char.isalpha():
            key_char = key[i % key_length]
            shift = ord(key_char.lower()) - ord('a')
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char
    return result

#CIFRADO ADFGVX
def generar_matriz_adfgvx():
    letras = list(string.ascii_uppercase)
    random.shuffle(letras)
    matriz_adfgvx = {letras[i]: f"{letras[i // 6]}{letras[i % 6]}" for i in range(len(letras))}
    matriz_adfgvx[' '] = '00'
    return matriz_adfgvx

def cifrar_adfgvx(texto, clave):
    matriz_adfgvx = generar_matriz_adfgvx()
    resultado = ""
    texto = texto.upper()
    texto = re.sub(r'[^A-Z]', '', texto)
    
    for caracter in texto:
        resultado += matriz_adfgvx[caracter] if caracter in matriz_adfgvx else ''
    
    resultado = ''.join(sorted(resultado, key=lambda x: clave.find(x[0])))
    return resultado


# def cifrar_adfgvx(texto, clave):
#     tabla_adfgvx = {
#         'A': 'AD', 'B': 'DF', 'C': 'FG', 'D': 'FX', 'E': 'GA',
#         'F': 'GD', 'G': 'GV', 'H': 'XA', 'I': 'XD', 'J': 'XF',
#         'K': 'XG', 'L': 'XV', 'M': 'AA', 'N': 'AF', 'O': 'AX',
#         'P': 'VA', 'Q': 'VD', 'R': 'VG', 'S': 'VV', 'T': 'DA',
#         'U': 'DF', 'V': 'DG', 'W': 'DV', 'X': 'XX', 'Y': 'XA',
#         'Z': 'XD', ' ': '00'
#     }
#     resultado = ""
#     texto = texto.upper()
#     texto = re.sub(r'[^A-Z]', '', texto)
#     for caracter in texto:
#         resultado += tabla_adfgvx[caracter] if caracter in tabla_adfgvx else ''
#     resultado = ''.join(sorted(resultado, key=lambda x: clave.find(x[0])))
#     return resultado

#CODIGO MORSE
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                  'C': '-.-.', 'D': '-..', 'E': '.',
                  'F': '..-.', 'G': '--.', 'H': '....',
                  'I': '..', 'J': '.---', 'K': '-.-',
                  'L': '.-..', 'M': '--', 'N': '-.',
                  'O': '---', 'P': '.--.', 'Q': '--.-',
                  'R': '.-.', 'S': '...', 'T': '-',
                  'U': '..-', 'V': '...-', 'W': '.--',
                  'X': '-..-', 'Y': '-.--', 'Z': '--..',
                  '1': '.----', '2': '..---', '3': '...--',
                  '4': '....-', '5': '.....', '6': '-....',
                  '7': '--...', '8': '---..', '9': '----.',
                  '0': '-----', ', ': '--..--', '.': '.-.-.-',
                  '?': '..--..', '/': '-..-.', '-': '-....-',
                  '(': '-.--.', ')': '-.--.-', ' ': '|'}
def encrypt(text):
    morse_code = ''
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_code += MORSE_CODE_DICT[char] + ' '
        else:
            morse_code += '| '  # Use '|' to represent space between words
    return morse_code
def decrypt(morse_code):
    morse_code = morse_code.split(' ')
    text = ''
    for code in morse_code:
        for key, value in MORSE_CODE_DICT.items():
            if code == value:
                text += key
    return text

#Polibios

def polibios(text):
  """Cifra el texto utilizando el cifrado de Polibios."""
  cuadrado_polibios = [['a', 'b', 'c', 'd', 'e'], ['f', 'g', 'h', 'i', 'j'], ['k', 'l', 'm', 'n', 'o'], ['p', 'q', 'r', 's', 't'], ['u', 'v', 'w', 'x', 'y', 'z']]
  texto_cifrado = ''
  for i in range(len(text)):
    letra = text[i]
    fila = i // 5
    columna = i % 5
    texto_cifrado += cuadrado_polibios[fila][columna]
  return texto_cifrado



#ROT-MORSE
def rot13(text):
  """Cifra el texto utilizando ROT13."""
  alphabet = string.ascii_lowercase
  shifted_alphabet = alphabet[13:] + alphabet[:13]
  return ''.join(shifted_alphabet[ord(c) - ord('a')] for c in text)

def morse(text):
  """Cifra el texto utilizando código Morse."""
  morse_code = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
  }
  return ' '.join(morse_code[c] for c in text)

def cifrar(palabra):
  """Cifra la palabra en ROT13 y luego la convierte a código Morse."""
  palabra_rot13 = rot13(palabra)
  palabra_morse = morse(palabra_rot13)
  return palabra_morse




def mostrar_menu():
    print("1. Atbash - ROT13")
    print("2. Vigenere")
    print("3. ADFGVX")
    print("4. Codigo Morse")
    print("5. Polibios")
    print("6. Metodo ROT-Morse")
    print("6. Salir")

def opcion1():
    print("Escogiste la criptografia Atbash")

def opcion2():
    print("Escogiste la criptografia Vigenère")

def opcion3():
    print("Escogiste la criptografia ADFGVX")

def opcion4():
    print("Escogiste la criptografia Codigo Morse")

def opcion5():
    print("Escogiste la criptografia Polibios")

def opcion6():
    print("Escogiste la criptografia ROT-Morse")

# Función principal
def main():
    while True:
        mostrar_menu()
        
        opcion = input("Selecciona una de las opciones (1-7): ")

        if opcion == "1":
            opcion1()
            texto_original = input("Ingresa la palabra o frase que quieres cifrar con Atbash y ROT13: ")
            texto_cifrado = atbash_cipher(texto_original)
            print(f'Palabra o frase ingresada: {texto_original}')
            print(f'Cifrado (Atbash): {texto_cifrado}')
            texto_cifrado = rot13_cipher(texto_original)
            print(f'Cifrado (ROT13): {texto_cifrado}')

        elif opcion == "2":
            opcion2()
            texto_original = input("Ingresa la palabra o frase que quieres cifrar con Vigenère: ")
            palabra_clave = input("Ingresa la palabra clave: ")
            texto_cifrado = vigenere_cipher(texto_original, palabra_clave)
            print(f'Palabra o frase ingresada: {texto_original}')
            print(f'Cifrado (Vigenère): {texto_cifrado}')

        elif opcion == "3":
            opcion3()
            texto_original = input("Ingresa la palabra o frase que quieres cifrar con ADFGVX: ")
            clave_adfgvx = input("Ingrese la clave para el cifrado ADFGVX: ")
            resultado = cifrar_adfgvx(texto_original, clave_adfgvx)
            print("Texto cifrado:", resultado)

        elif opcion == "4":
            opcion4()
            mensaje_original = input("Ingrese la palabra o frase a cifrar en código Morse: ")
            mensaje_cifrado = encrypt(mensaje_original)
            mensaje_descifrado = decrypt(mensaje_cifrado)
            print(f'Mensaje original: {mensaje_original}')
            print(f'Mensaje cifrado: {mensaje_cifrado}')
            print(f'Mensaje descifrado: {mensaje_descifrado}')

        elif opcion == "5":
            opcion5()
            if __name__ == "__main__":
                text = input("Ingrese la palabra o frase a cifrar Polibios: ")
                texto_cifrado = polibios(text)
                print(f"El texto original: {text}")
                print(f"El texto cifrado es: {texto_cifrado}")

        elif opcion == "6":
            opcion6()
            if __name__ == "__main__":
                palabra = input("Ingrese la palabra o frase a cifrar ROT-Morse: ")
                palabra_cifrada = cifrar(palabra)
                print(f"La palabra original es: {palabra}")
                print(f"La palabra cifrada es: {palabra_cifrada}")


        elif opcion == "7":
            print("Gracias por utilizar este programa, vuelva pronto :D")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
