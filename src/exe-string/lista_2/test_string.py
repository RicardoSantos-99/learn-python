from exercicio import (
    somente_digitos, somente_letras, somente_espacos,
    primeira_palavra, ultima_palavra, contar_palavras,
    capitalizar_palavras, inverter_palavras, substituir_ultima_ocorrencia,
    remover_ocorrencias
)

def test_somente_digitos():
    assert somente_digitos("123"), "Deve retornar True para uma string contendo apenas dígitos"
    assert not somente_digitos("123a"), "Deve retornar False para uma string contendo caracteres não-dígitos"
    assert not somente_digitos(""), "Deve retornar False para uma string vazia"
    assert not somente_digitos(" 123 "), "Deve retornar False para uma string contendo espaços"

def test_somente_letras():
    assert somente_letras("abc"), "Deve retornar True para uma string contendo apenas letras"
    assert not somente_letras("abc1"), "Deve retornar False para uma string contendo caracteres não-alfabéticos"
    assert not somente_letras(""), "Deve retornar False para uma string vazia"
    assert not somente_letras(" abc "), "Deve retornar False para uma string contendo espaços"

def test_somente_espacos():
    assert somente_espacos("   "), "Deve retornar True para uma string contendo apenas espaços"
    assert not somente_espacos(" a "), "Deve retornar False para uma string contendo caracteres além de espaços"
    assert not somente_espacos(""), "Deve retornar False para uma string vazia"
    assert not somente_espacos(" a  "), "Deve retornar False para uma string contendo caracteres além de espaços no meio"

def test_primeira_palavra():
    assert primeira_palavra("Olá mundo") == "Olá", "Deve retornar a primeira palavra da string"
    assert primeira_palavra("mundo") == "mundo", "Deve retornar a única palavra da string"
    assert primeira_palavra("") == "", "Deve retornar uma string vazia se não houver palavras"
    assert primeira_palavra("  Olá mundo  ") == "Olá", "Deve ignorar espaços extras no início e no final"

def test_ultima_palavra():
    assert ultima_palavra("Olá mundo") == "mundo", "Deve retornar a última palavra da string"
    assert ultima_palavra("mundo") == "mundo", "Deve retornar a única palavra da string"
    assert ultima_palavra("") == "", "Deve retornar uma string vazia se não houver palavras"
    assert ultima_palavra("  Olá mundo  ") == "mundo", "Deve ignorar espaços extras no início e no final"

def test_contar_palavras():
    assert contar_palavras("Olá mundo") == 2, "Deve contar o número de palavras na string"
    assert contar_palavras("Olá") == 1, "Deve contar 1 para uma string com uma única palavra"
    assert contar_palavras("") == 0, "Deve contar 0 para uma string vazia"
    assert contar_palavras("   ") == 0, "Deve contar 0 para uma string com apenas espaços"

def test_capitalizar_palavras():
    assert capitalizar_palavras("olá mundo") == "Olá Mundo", "Deve capitalizar a primeira letra de cada palavra"
    assert capitalizar_palavras("oLá MuNdO") == "Olá Mundo", "Deve capitalizar a primeira letra e tornar as outras letras minúsculas"
    assert capitalizar_palavras("") == "", "Deve retornar uma string vazia se não houver palavras"
    assert capitalizar_palavras("  olá mundo  ") == "  Olá Mundo  ", "Deve manter os espaços no início e no final"

def test_inverter_palavras():
    assert inverter_palavras("Olá mundo") == "mundo Olá", "Deve inverter a ordem das palavras na string"
    assert inverter_palavras("mundo") == "mundo", "Deve retornar a única palavra da string"
    assert inverter_palavras("") == "", "Deve retornar uma string vazia se não houver palavras"
    assert inverter_palavras("  Olá mundo  ") == "  mundo Olá  ", "Deve manter os espaços no início e no final"

def test_substituir_ultima_ocorrencia():
    assert substituir_ultima_ocorrencia("a a a", "a", "b") == "a a b", "Deve substituir a última ocorrência de uma substring"
    assert substituir_ultima_ocorrencia("a a a", "b", "c") == "a a a", "Deve manter a string inalterada se a substring não for encontrada"
    assert substituir_ultima_ocorrencia("", "a", "b") == "", "Deve retornar uma string vazia se não houver palavras"
    assert substituir_ultima_ocorrencia("a a a", "a", "") == "a a ", "Deve remover a última ocorrência se a nova substring for vazia"

def test_remover_ocorrencias():
    assert remover_ocorrencias("a a a", "a") == "   ", "Deve remover todas as ocorrências de uma substring"
    assert remover_ocorrencias("a a a", "b") == "a a a", "Deve manter a string inalterada se a substring não for encontrada"
    assert remover_ocorrencias("", "a") == "", "Deve retornar uma string vazia se não houver palavras"
    assert remover_ocorrencias("a a a", "") == "a a a", "Deve manter a string inalterada se a substring for vazia"

