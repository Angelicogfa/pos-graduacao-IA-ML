# language: pt

Funcionalidade: Testar api Iris

"""
    Teste api Iris
"""

Cenário: Teste metodo predict api Iris
    Quando o usuário informa os dados '5.6' '2.7' '4.2' '1.3'
    Então o valor do metodo predict e o '1'