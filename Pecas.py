import chess

# Classe base para todas as peças de xadrez
class Peca:
    def __init__(self, cor):
        # Inicializa uma peça com a cor especificada (branco ou preto)
        self.cor = cor

    def _dentro_limites_tabuleiro(self, square):
        # Verifica se um quadrado está dentro dos limites do tabuleiro
        return 0 <= chess.square_file(square) < 8 and 0 <= chess.square_rank(square) < 8

# Classe para a peça Peão
class Peao(Peca):
    def __init__(self, cor, square):
        # Inicializa o Peão com cor e posição
        super().__init__(cor)
        self.square = square

    def movimentos_possiveis(self):
        # Gera os movimentos possíveis para um Peão
        movimentos = []
        # ... Lógica para determinar os movimentos do Peão ...
        return movimentos

    def promover(self, nova_classe):
        # Lógica para a promoção do Peão
        nova_peca = nova_classe(self.cor, self.square)
        return nova_peca

# Classe para a peça Torre
class Torre(Peca):
    def __init__(self, cor):
        # Inicializa a Torre com a cor especificada
        super().__init__(cor)

    def movimentos_possiveis(self):
        # Gera os movimentos possíveis para uma Torre
        # ... Lógica para movimentos verticais e horizontais ...

# Classe para a peça Cavalo
class Cavalo(Peca):
    def __init__(self, cor):
        # Inicializa o Cavalo com a cor especificada
        super().__init__(cor)

    def movimentos_possiveis(self):
        # Gera os movimentos possíveis para um Cavalo
        # ... Lógica para movimentos em 'L' ...

# Classe para a peça Bispo
class Bispo(Peca):
    def __init__(self, cor):
        # Inicializa o Bispo com a cor especificada
        super().__init__(cor)

    def movimentos_possiveis(self):
        # Gera os movimentos possíveis para um Bispo
        # ... Lógica para movimentos diagonais ...

# Classe para a peça Rainha
class Rainha(Peca):
    def __init__(self, cor):
        # Inicializa a Rainha com a cor especificada
        super().__init__(cor)

    def movimentos_possiveis(self):
        # Gera os movimentos possíveis para uma Rainha
        # ... Combinação dos movimentos de Torre e Bispo ...

# Classe para a peça Rei
class Rei(Peca):
    def __init__(self, cor, square):
        # Inicializa o Rei com a cor e posição
        super().__init__(cor)
        self.square = square

    def movimentos_possiveis(self):
        # Gera os movimentos possíveis para um Rei
        # ... Lógica para movimentos de uma casa em qualquer direção ...
        return movimentos_validos
