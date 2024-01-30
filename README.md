# README: Condições em Python e Orientação a Objetos

Este README destina-se a fornecer uma visão geral das estruturas de controle de fluxo em Python, incluindo instruções `for`, `if`, `while`, e sua aplicação na orientação a objetos.

## Estruturas de Controle de Fluxo em Python

### Instrução `if`

A instrução `if` em Python é usada para executar uma ação condicionalmente, dependendo de se uma condição é avaliada como verdadeira ou falsa.

Exemplo:

```python
if condition:
    # código a ser executado se a condição for verdadeira
else:
    # código a ser executado se a condição for falsa
```

### Instrução `for`

A instrução `for` é utilizada para iterar sobre uma sequência (como uma lista, tupla, dicionário, etc.) e realizar operações em cada elemento.

Exemplo:

```python
for item in sequence:
    # código a ser executado para cada item na sequência
```

### Instrução `while`

A instrução `while` é usada para repetir um bloco de código enquanto uma condição especificada for avaliada como verdadeira.

Exemplo:

```python
while condition:
    # código a ser executado enquanto a condição for verdadeira
```

## Orientação a Objetos em Python

Python é uma linguagem de programação orientada a objetos, o que significa que ela permite a definição e manipulação de classes e objetos.

### Classes e Objetos

Uma classe é uma estrutura que define o comportamento e as propriedades de um objeto. Um objeto é uma instância de uma classe.

Exemplo de definição de classe:

```python
class MyClass:
    def __init__(self, prop1, prop2):
        self.prop1 = prop1
        self.prop2 = prop2

    def my_method(self):
        # código do método
```

Exemplo de criação de objeto:

```python
obj = MyClass(value1, value2)
```

### Métodos de Classe e Métodos Estáticos

- **Métodos de Classe**: Métodos que são chamados na classe em vez de uma instância específica e têm acesso apenas aos atributos da classe.

- **Métodos Estáticos**: Métodos que não recebem uma referência implícita à instância ou à classe e são usados principalmente para utilidades relacionadas à classe.

Exemplo:

```python
class MyClass:
    @classmethod
    \```
    def my_class_method(cls, arg):
        # código do método de classe
    \```

    @staticmethod
    \```
    def my_static_method(arg):
        # código do método estático
    \```
```

### Docstrings

Docstrings são strings de documentação usadas para documentar classes, funções ou módulos em Python. Elas são colocadas logo após a definição de uma classe, função ou módulo e são usadas para descrever seu propósito e comportamento.

Exemplo de docstring em uma função:

```python
def my_function():
    """Esta é uma função de exemplo."""
    # código da função