from exercicio import (
    inverter_string, para_maiusculas, contar_ocorrencias,
    para_minusculas, remover_espacos, substituir_substring,
    dividir_string, juntar_lista, encontrar_substring, repetir_string
)

def test_inverter_string():
    assert inverter_string("Python") == "nohtyP", "Deve inverter a string"
    assert inverter_string("abc") == "cba", "Deve inverter a string"
    assert inverter_string("") == "", "Uma string vazia deve retornar uma string vazia"
    assert inverter_string("a") == "a", "Uma string com um único caractere deve retornar a mesma string"

def test_para_maiusculas():
    assert para_maiusculas("python") == "PYTHON", "Deve converter para maiúsculas"
    assert para_maiusculas("Python") == "PYTHON", "Deve converter para maiúsculas"
    assert para_maiusculas("") == "", "Uma string vazia deve retornar uma string vazia"
    assert para_maiusculas(" ") == " ", "Um espaço deve retornar um espaço"

def test_contar_ocorrencias():
    assert contar_ocorrencias("banana", "a") == 3, "Deve contar o número de ocorrências de um caractere"
    assert contar_ocorrencias("banana", "b") == 1, "Deve contar o número de ocorrências de um caractere"
    assert contar_ocorrencias("banana", "n") == 2, "Deve contar o número de ocorrências de um caractere"
    assert contar_ocorrencias("banana", "z") == 0, "Deve retornar 0 se o caractere não estiver na string"
    assert contar_ocorrencias("", "a") == 0, "Uma string vazia deve retornar 0"

def test_para_minusculas():
    assert para_minusculas("PYTHON") == "python", "Deve converter para minúsculas"
    assert para_minusculas("Python") == "python", "Deve converter para minúsculas"
    assert para_minusculas("") == "", "Uma string vazia deve retornar uma string vazia"
    assert para_minusculas(" ") == " ", "Um espaço deve retornar um espaço"

def test_remover_espacos():
    assert remover_espacos("  olá  ") == "olá", "Deve remover espaços em branco no início e no final"
    assert remover_espacos("olá") == "olá", "String sem espaços deve permanecer a mesma"
    assert remover_espacos("  ") == "", "String apenas com espaços deve retornar string vazia"
    assert remover_espacos("") == "", "String vazia deve retornar string vazia"

def test_substituir_substring():
    assert substituir_substring("Olá, mundo!", "mundo", "Python") == "Olá, Python!", "Deve substituir uma substring por outra"
    assert substituir_substring("Olá, mundo!", "Olá", "Oi") == "Oi, mundo!", "Deve substituir uma substring por outra"
    assert substituir_substring("Olá, mundo!", "Python", "Ruby") == "Olá, mundo!", "Se a substring não existir, a string deve permanecer a mesma"
    assert substituir_substring("", "Olá", "Oi") == "", "String vazia deve retornar string vazia"

def test_dividir_string():
    assert dividir_string("maçã pera banana", " ") == ['maçã', 'pera', 'banana'], "Deve dividir a string em uma lista com base em um delimitador"
    assert dividir_string("maçã,pera,banana", ",") == ['maçã', 'pera', 'banana'], "Deve dividir a string em uma lista com base em um delimitador"
    assert dividir_string("maçã", " ") == ['maçã'], "Deve retornar uma lista com um elemento se não houver delimitador"
    assert dividir_string("", " ") == [""], "String vazia deve retornar uma lista com uma string vazia"

def test_juntar_lista():
    assert juntar_lista(['maçã', 'pera', 'banana'], " ") == "maçã pera banana", "Deve juntar os elementos de uma lista em uma string"
    assert juntar_lista(['maçã'], " ") == "maçã", "Deve retornar a mesma string se a lista contiver um único elemento"
    assert juntar_lista([], " ") == "", "Uma lista vazia deve retornar uma string vazia"
    assert juntar_lista(['maçã', 'pera', 'banana'], ", ") == "maçã, pera, banana", "Deve juntar os elementos com um delimitador diferente"

def test_encontrar_substring():
    assert encontrar_substring("Olá, mundo!", "mundo") == 7, "Deve encontrar a posição da primeira ocorrência de uma substring"
    assert encontrar_substring("Olá, mundo!", "Olá") == 0, "Deve encontrar a posição da primeira ocorrência de uma substring no início"
    assert encontrar_substring("Olá, mundo!", "Python") == -1, "Deve retornar -1 se a substring não for encontrada"
    assert encontrar_substring("", "mundo") == -1, "Deve retornar -1 para uma string vazia"

def test_repetir_string():
    assert repetir_string("A", 3) == "AAA", "Deve repetir a string um determinado número de vezes"
    assert repetir_string("A", 0) == "", "Repetir zero vezes deve retornar uma string vazia"
    assert repetir_string("", 3) == "", "Uma string vazia repetida qualquer número de vezes deve retornar uma string vazia"
    assert repetir_string("AB", 2) == "ABAB", "Deve repetir a string completa"

