# Representacao e manipulacao do tabuleiro

import chess
import chess.engine
from Pieces import Peca

class Chessboard():
    def __init__(self):
        self.board = chess.Board()
        self.engine = chess.engine.SimpleEngine.popen_uci("/opt/homebrew/bin/stockfish")

    def display(self):
        print(self.board)  # Exibe o estado atual do tabuleiro

    def make_move(self, move_str):  # Executa um movimento no tabuleiro
        try:
            move = chess.Move.from_uci(move_str)  # Universal Chess Interface
        except ValueError as e:
            print(f"Erro no movimento: {e}")
            return False

        if move in self.board.legal_moves:
            self.board.push(move)
            return True
        else:
            print("Movimento invalido. Tente novamente.")
            return False

    def is_game_over(self):  # Verifica se o jogo terminou
        return self.board.is_game_over()

    def get_winner(self):  # Obtem o resultado do jogo
        if self.board.is_checkmate():
            return f"Vitória para {('Brancas' if self.board.turn == chess.WHITE else 'Pretas')}"

        elif self.board.is_stalemate():
            return "Empate por afogamento (stalemate)"

        elif self.board.is_insufficient_material():
            return "Empate por material insuficiente"

        elif self.board.is_seventyfive_moves() or self.board.is_fivefold_repetition():
            return "Empate por regra dos 75 movimentos ou repetição quíntupla"

        elif self.board.is_variant_draw():
            return "Empate por regra da variante"

        else:
            return None

    def is_check(self):
        """Verifica se o jogador atual está em xeque."""
        return self.board.is_check()

    def is_draw_by_repetition(self):
        """Verifica se o jogo terminou por empate devido à repetição."""
        return self.board.is_fivefold_repetition() or self.board.is_seventyfive_moves()

    def get_stockfish_move(self):
        result = self.engine.play(self.board, chess.engine.Limit(time=2.0))
        return result.move

    def play_stockfish_move(self):
        stockfish_move = self.get_stockfish_move()
        self.board.push(stockfish_move)
