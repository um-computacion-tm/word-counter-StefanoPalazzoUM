import unittest



def count_words(frase):
    diccionario = {}
    frase = frase.lower()
    palabras = frase.split(' ')  # Separa el texto en palabras
    for palabra in palabras:
      if palabra in diccionario:
        diccionario[palabra] += 1
      else:
        diccionario[palabra] = 1
    return(diccionario)


if __name__ == '__main__':
    unittest.main()