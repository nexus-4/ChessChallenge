# Classes para as peças e seus movimentos basicos e especiais

import chess

class Peca:
    def __init__(self, cor):
        self.cor = cor

    def _dentro_limites_tabuleiro(self, square):
        return 0 <= chess.square_file(square) < 8 and 0 <= chess.square_rank(square) < 8

class Peao(Peca):
    def __init__(self, cor, square):
        super().__init__(cor)
        self.square = square
        self.en_passant_target = None  # Inicialmente, não há possibilidade de captura en passant

    def movimentos_possiveis(self):
        movimentos = []

        # Movimento de uma casa para frente
        if self.cor == chess.WHITE:
            movimento_um_casa = self.square + 8
        else:
            movimento_um_casa = self.square - 8

        # Verifica se a casa à frente está vazia
        if self.square + movimento_um_casa in range(64):  # Verifica se não ultrapassa o limite do tabuleiro
            movimentos.append(movimento_um_casa)

            # Movimento de duas casas para frente no primeiro movimento
            if (
                self.cor == chess.WHITE
                and chess.square_rank(self.square) == 1
                and self.square + movimento_um_casa * 2 in range(64)
            ):
                movimentos.append(movimento_um_casa * 2)
                # Configura o alvo en passant
                self.en_passant_target = self.square + movimento_um_casa

        # Captura diagonalmente
        if (
            self.square + movimento_um_casa + 1 in range(64)
            and chess.square_file(self.square) < 7
        ):
            movimentos.append(movimento_um_casa + 1)
        if (
            self.square + movimento_um_casa - 1 in range(64)
            and chess.square_file(self.square) > 0
        ):
            movimentos.append(movimento_um_casa - 1)

        # Captura en passant
        if self.en_passant_target is not None:
            movimentos.append(self.en_passant_target)

        return movimentos

    def avancar_en_passant(self, square_alvo):
        # Configura o alvo en passant
        self.en_passant_target = square_alvo

    def limpar_en_passant(self):
        # Limpa a possibilidade de captura en passant
        self.en_passant_target = None


class Torre(Peca):
    def __init__(self, cor):
        super().__init__(cor)

    def movimentos_possiveis(self):
        # Implementação básica para uma torre que pode se mover na vertical ou horizontal
        return [self.square + chess.SquareDelta(0, 1), self.square + chess.SquareDelta(0, -1),
                self.square + chess.SquareDelta(1, 0), self.square + chess.SquareDelta(-1, 0)]

class Cavalo(Peca):
    def __init__(self, cor):
        super().__init__(cor)

    def movimentos_possiveis(self):
        # Implementação básica para um cavalo que pode se mover em forma de "L"
        return [self.square + chess.SquareDelta(1, 2), self.square + chess.SquareDelta(-1, 2),
                self.square + chess.SquareDelta(2, 1), self.square + chess.SquareDelta(-2, 1)]

class Bispo(Peca):
    def __init__(self, cor):
        super().__init__(cor)

    def movimentos_possiveis(self):
        # Implementação básica para um bispo que pode se mover na diagonal
        return [self.square + chess.SquareDelta(1, 1), self.square + chess.SquareDelta(-1, 1),
                self.square + chess.SquareDelta(1, -1), self.square + chess.SquareDelta(-1, -1)]

class Rainha(Peca):
    def __init__(self, cor):
        super().__init__(cor)

    def movimentos_possiveis(self):
        # Implementação básica para uma rainha que combina movimentos de torre e bispo
        return [self.square + chess.SquareDelta(0, 1), self.square + chess.SquareDelta(0, -1),
                self.square + chess.SquareDelta(1, 0), self.square + chess.SquareDelta(-1, 0),
                self.square + chess.SquareDelta(1, 1), self.square + chess.SquareDelta(-1, 1),
                self.square + chess.SquareDelta(1, -1), self.square + chess.SquareDelta(-1, -1)]

class Rei(Peca):
    def __init__(self, cor, square):
        super().__init__(cor)
        self.square = square
        self.pode_rocar_curto = True
        self.pode_rocar_longo = True

    def movimentos_possiveis(self):
        movimentos = [
            self.square + chess.SquareDelta(0, 1), self.square + chess.SquareDelta(0, -1),
            self.square + chess.SquareDelta(1, 0), self.square + chess.SquareDelta(-1, 0),
            self.square + chess.SquareDelta(1, 1), self.square + chess.SquareDelta(-1, 1),
            self.square + chess.SquareDelta(1, -1), self.square + chess.SquareDelta(-1, -1)
        ]

        # Filtra os movimentos para garantir que estejam dentro dos limites do tabuleiro
        movimentos_validos = [movimento for movimento in movimentos if chess.square_file(movimento) in range(8) and chess.square_rank(movimento) in range(8)]

        if self.pode_rocar_curto:
            movimentos_validos.append(self.square + chess.SquareDelta(0, 2))
        if self.pode_rocar_longo:
            movimentos_validos.append(self.square + chess.SquareDelta(0, -2))

        return movimentos_validos

    def realizar_roque(self, lado_curto=True):
        # Executa o movimento do rei e da torre no roque
        if lado_curto:
            self.square += chess.SquareDelta(0, 2)
            # Desativa a capacidade de rocar curto após o roque
            self.pode_rocar_curto = False
        else:
            self.square += chess.SquareDelta(0, -2)
            # Desativa a capacidade de rocar longo após o roque
            self.pode_rocar_longo = False

