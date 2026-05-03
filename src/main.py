from itertools import combinations
from random import sample

class JogoAposta:
    """
    Gerenciador de combinações para jogos de apostas com números e estrelas.

    Esta classe permite gerar combinações aleatórias baseadas em um universo de 
    números e estrelas, simulando jogos como o EuroMillions. As combinações são 
    armazenadas em um histórico interno e podem ser exibidas formatadas.

    Attributes:
        lista (list): Armazena os dicionários de cada jogo gerado.
        numero (list): Universo de números disponíveis para o sorteio.
        jogo (int): Quantidade de números a serem escolhidos por aposta.
        estrela (list): Universo de estrelas disponíveis para o sorteio.
        jogo_estrela (int): Quantidade de estrelas a serem escolhidas por aposta.
        limite (int): Quantidade total de jogos (apostas) a serem gerados.
    """
    def __init__(self, limite, quant_numero = 50, quant_estrela = 12, quant_jogo = 5, quant_jogo_estrela = 2):
        """
        Inicializa a configuração do jogo de aposta.

        Args:
            limite (int): Total de combinações que serão geradas.
            quant_numero (int, optional): Total de números no volante. Defaults to 50.
            quant_estrela (int, optional): Total de estrelas no volante. Defaults to 12.
            quant_jogo (int, optional): Quantos números marcar por jogo. Defaults to 5.
            quant_jogo_estrela (int, optional): Quantas estrelas marcar por jogo. Defaults to 2.
        """
        self.lista = [] #será armazenada um dicionario com os jogos e estrelas
        self.numero = list(range(1, quant_numero + 1))
        self.jogo = quant_jogo
        self.estrela = list(range(1, quant_estrela + 1))
        self.jogo_estrela = quant_jogo_estrela
        self.limite = limite

    def gerar_combinacoes(self):
        """
        Gera as combinações únicas de números e estrelas e as imprime no console.

        O método utiliza amostragem aleatória sobre todas as combinações possíveis
        definidas nos parâmetros da classe. Os resultados são salvos em `self.lista`
        no formato de dicionários.

        Note:
            O limite fornecido não deve exceder o número total de combinações 
            matematicamente possíveis para os conjuntos fornecidos.
        """
        meu_dict = {}
        # Gerar a combinação do jogo e das estrelas
        # Nota: combinations gera os grupos, sample sorteia 'n' grupos sem repetição
        meu_jogo = sample(list(combinations(self.numero, self.jogo)), self.limite)
        minha_estrela = sample(list(combinations(self.estrela, self.jogo_estrela)), self.limite)
    
        for lista, estrela in zip(meu_jogo, minha_estrela):           
            meu_dict['jogo'] = lista
            meu_dict['estrela'] = estrela 
            self.lista.append(meu_dict.copy())
    
        for i, resultado in enumerate(self.lista):
            jogo, star = resultado.values()
            print(f'JOGO Nº {i + 1}: JOGO:', *jogo, 'ESTRELA:', *star)

if __name__ == '__main__':
    # o máximo de combinações possiveis seguindo as estrelas são de 66 combinações posiveis (12, 2)
    jogo = JogoAposta(10) # o limite representa o total de combinações possiveis.
    resultado = jogo.gerar_combinacoes()