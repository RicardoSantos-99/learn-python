# Exemplos de Manipulação de Strings em Python

# 1. Inverter uma String
# O uso de ::-1 inverte a ordem dos caracteres da string.
exemplo1 = "Python"
resultado1 = exemplo1[::-1]
# Output: "nohtyP"

# 2. Converter para Maiúsculas
# O método .upper() converte todos os caracteres da string para maiúsculas.
exemplo2 = "python"
resultado2 = exemplo2.upper()
# Output: "PYTHON"

# 3. Converter para Minúsculas
# O método .lower() converte todos os caracteres da string para minúsculas.
exemplo3 = "PYTHON"
resultado3 = exemplo3.lower()
# Output: "python"

# 4. Contar Ocorrências de um Caractere
# O método .count() conta o número de ocorrências de um caractere específico na string.
exemplo4 = "banana"
resultado4 = exemplo4.count('a')
# Output: 3

# 5. Verificar se uma String Começa com um Prefixo
# O método .startswith() verifica se a string começa com um determinado prefixo.
exemplo5 = "banana"
resultado5 = exemplo5.startswith("ban")
# Output: True

# 6. Verificar se uma String Termina com um Sufixo
# O método .endswith() verifica se a string termina com um determinado sufixo.
exemplo6 = "banana"
resultado6 = exemplo6.endswith("ana")
# Output: True

# 7. Dividir uma String em uma Lista
# O método .split() divide a string em uma lista de substrings com base em um delimitador.
exemplo7 = "maçã pera banana"
resultado7 = exemplo7.split(" ")
# Output: ['maçã', 'pera', 'banana']

# 8. Juntar uma Lista em uma String
# O método .join() junta os elementos de uma lista em uma string, usando uma string delimitadora.
exemplo8 = ['maçã', 'pera', 'banana']
resultado8 = " ".join(exemplo8)
# Output: "maçã pera banana"


# Exemplos Avançados de Manipulação de Strings em Python

# 9. Remover Espaços em Branco do Início e do Final
# O método .strip() remove os espaços em branco do início e do final da string.
exemplo9 = "   Olá, mundo!   "
resultado9 = exemplo9.strip()
# Output: "Olá, mundo!"

# 10. Substituir Substring
# O método .replace() substitui todas as ocorrências de uma substring por outra.
exemplo10 = "Olá, mundo!"
resultado10 = exemplo10.replace("mundo", "Python")
# Output: "Olá, Python!"

# 11. Encontrar a Posição de uma Substring
# O método .find() retorna a posição da primeira ocorrência de uma substring. Se não encontrar, retorna -1.
exemplo11 = "Olá, mundo!"
resultado11 = exemplo11.find("mundo")
# Output: 7

# 12. Converter String para Lista de Caracteres
# A função list() pode ser usada para converter uma string em uma lista de caracteres.
exemplo12 = "Python"
resultado12 = list(exemplo12)
# Output: ['P', 'y', 't', 'h', 'o', 'n']

# 13. Verificar se Todos os Caracteres São Alfabéticos
# O método .isalpha() verifica se todos os caracteres da string são alfabéticos.
exemplo13 = "Python"
resultado13 = exemplo13.isalpha()
# Output: True

# 14. Concatenar Strings
# O operador + pode ser usado para concatenar duas strings.
exemplo14a = "Olá, "
exemplo14b = "mundo!"
resultado14 = exemplo14a + exemplo14b
# Output: "Olá, mundo!"

# 15. Repetir Strings
# O operador * pode ser usado para repetir uma string um determinado número de vezes.
exemplo15 = "A"
resultado15 = exemplo15 * 3
# Output: "AAA"
