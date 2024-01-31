# Condições em Python e Orientação a Objetos

Este README destina-se a fornecer uma visão geral das estruturas de controle de fluxo em Python, incluindo instruções `for`, `if`, `while`, e sua aplicação na orientação a objetos.

Leia também: [O que é Python? História, Sintaxe e um Guia para iniciar na Linguagem](https://www.alura.com.br/artigos/python)

## Orientação a objetos

Orientação a objetos é um paradigma de programação que organiza o código em unidades chamadas objetos, que representam entidades do mundo real. Esses objetos têm características (atributos) e comportamentos (métodos), e interagem entre si através de mensagens, permitindo a modelagem de sistemas complexos de forma mais modular, flexível e reutilizável.

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
```

### Contrutor

Um construtor em Python é um método especial dentro de uma classe que é automaticamente invocado quando um objeto dessa classe é criado. O objetivo principal de um construtor é inicializar os atributos do objeto com valores específicos. O construtor é declarado usando o método __init__(). Aqui está um exemplo simples de uma classe em Python com um construtor:

```python
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def descricao(self):
        return f"{self.marca} {self.modelo} {self.ano}"

# Criando um objeto Carro usando o construtor
meu_carro = Carro("Toyota", "Corolla", 2020)

# Chamando um método do objeto
print(meu_carro.descricao())  # Saída: Toyota Corolla 2020
```

### Property e classmethod

A função property() em Python é usada para criar propriedades de classe, permitindo que métodos sejam chamados implicitamente ao acessar ou definir atributos de um objeto. Ela permite definir métodos getter, setter e deleter para manipular o acesso, a alteração e a remoção de valores de atributos.

```python
@property
def ativo(self):
    return 'verdadeiro' if self._ativo else 'falso'
```

O classmethod em Python é um decorador usado para definir métodos de classe, que são métodos associados à classe em vez de instâncias individuais. Isso significa que esses métodos têm acesso à classe, não a instâncias específicas, e podem ser chamados usando a própria classe como objeto.

```python
class Matematica:
    @classmethod
    def soma(cls, a, b):
        return a + b

# Uso da classe Matematica
resultado = Matematica.soma(5, 3)
print(resultado)  # Saída: 8
```

### Herança

Em Python, herança é um conceito de programação orientada a objetos onde uma classe pode herdar atributos e métodos de outra classe, conhecida como classe pai ou superclasse. Isso permite a reutilização de código e a criação de hierarquias de classes, onde as subclasses podem estender ou modificar o comportamento da superclasse.