import unittest



def count_words(frase):
    diccionario = {}
    palabras = frase.split(' ')  # Separa el texto en palabras
    for palabra in palabras:
      if palabra in diccionario:
        diccionario[palabra.lower()] += 1
      else:
        diccionario[palabra.lower()] = 1
    return(diccionario)


if __name__ == '__main__':
    unittest.main()