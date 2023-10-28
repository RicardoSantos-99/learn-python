# Exercícios de Python

Este repositório contém uma série de exercícios de Python focados em manipulação de strings, condicionais, loops e outras estruturas básicas da linguagem. Cada exercício vem com testes unitários que você pode executar para verificar se sua solução está correta.

## Configuração

Certifique-se de ter Python 3.x instalado em seu sistema.

(Opcional) Crie um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

### Como resolver os exercícios

- Os exercícios estão organizados em diferentes pastas dentro do diretório src/exe-*. Cada pasta, como lista_1 e lista_2, contém um conjunto de exercícios e seus testes associados.

- Cada função a ser implementada tem um bloco de comentários acima dela, descrevendo o que a função deve fazer.

- Substitua a palavra pass pela sua implementação.

- Dentro de cada pasta de lista (por exemplo, lista_1), você encontrará dois arquivos principais:

  - exercicio.py: contém as funções que você precisa implementar. Cada função tem um bloco de comentários acima dela, descrevendo o que a função deve fazer.
  - test_string.py: contém os testes unitários para as funções em exercicio.py.

- Exemplo de Estrutura de Diretórios:

```bash
src
└── exe-string
    ├── lista_1
    │   ├── exercicio.py
    │   └── test_string.py
    └── lista_2
        ├── exercicio.py
        └── test_string.py
```

Exemplo:

```python
def inverter_string(s):
    pass  # Substitua esta linha pelo seu código
```

### Como executar os testes

Estamos usando pytest para os testes unitários.

- Navegue até o diretório onde o arquivo de teste está localizado. Por exemplo, para executar todos os testes do arquivo test_string.py na pasta lista_1, você faria:

```bash
cd src/exe-string/lista_1
```

- Em seguida, execute o comando pytest seguido do nome do arquivo de teste:

```bash
pytest test_string.py
```

- Para executar um único conjunto de testes

```bash
pytest -k nome_do_teste
```
