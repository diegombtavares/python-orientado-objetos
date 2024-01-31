from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('praça', 'gourmet')
bebida_suco = Bebida('Suco de melancia', 5.0, 'Grande')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')


def main():
    print(bebida_suco)
    print(prato_paozinho)

if __name__ == '__main__':
    main()