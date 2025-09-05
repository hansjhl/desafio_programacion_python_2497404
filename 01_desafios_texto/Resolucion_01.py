def palindromo(texto):
  texto_minuscula = texto.lower()
  texto_sin_espacios = texto_minuscula.replace(" ","")
  newTexto = texto_sin_espacios[::-1]
  return texto_sin_espacios == newTexto
print (palindromo("hola"))
