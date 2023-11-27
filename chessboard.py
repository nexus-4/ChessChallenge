# Representacao e manipulacao do tabuleiro
import chess
import chess.engine

class Chessboard():
    def __init__(self, time_limit=2.0, num_threads = 5, depth_limit = 20): # 2min por jogada( tempo de reflexao)
        self.board = chess.Board()
        self.engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")
        self.engine.configure({"Skill Level": 20, "Threads": num_threads}) #configuracoes do stockfish
        self.time_limit = time_limit
        self.depth_limit = depth_limit
        self.board_history_svg = []


    def display(self):
        from IPython.display import display, SVG, HTML
        svg = self.board._repr_svg_()
        svg = svg.replace('<svg width="390" height="390"', '<svg width="290" height="290"')
        display(SVG(svg))

        legal_moves = list(self.board.legal_moves)

    def play_stockfish_move(self):
        # Obtém o melhor movimento sugerido pelo Stockfish
        result = self.engine.play(self.board, chess.engine.Limit(time=self.time_limit))
        # Executa o movimento no tabuleiro
        self.board.push(result.move)

    def make_move(self, move_str):
        svg = self.board._repr_svg_()
        self.board_history_svg.append(svg)
        try:
            move = chess.Move.from_uci(move_str)
        except ValueError as e:
            print(f"Erro no movimento: {e}")
            return False

        if move in self.board.legal_moves:
            self.board.push(move)
            return True
        else:
            print("Movimento inválido. Tente novamente.")
            return False
    def evaluate_position(self):
        # Avalia a posição atual e retorna a pontuação.
        result = self.engine.analyse(self.board, chess.engine.Limit(depth=20))
        score = result['score'].white() if self.board.turn == chess.WHITE else result['score'].black()
        return score


    def get_game_result(self):
        # Verifica as condições de término e avalia a posição.
        if self.board.is_checkmate():
            return "Xeque-mate!", None
        elif self.board.is_stalemate():
            return "Empate por afogamento (stalemate).", None
        elif self.board.is_insufficient_material():
            return "Empate por material insuficiente.", None
        elif self.board.is_seventyfive_moves() or self.board.is_fivefold_repetition():
            return "Empate por regra dos 75 movimentos ou repetição quíntupla.", None
        elif self.board.is_variant_draw():
            return "Empate por regra da variante.", None
        else:
            score = self.evaluate_position()
            return "Jogo em andamento.", score

    def is_game_over(self):
        return self.board.is_game_over()

    def calculate_material_score(self):
        # Inicializa as pontuações e as contagens de peças capturadas
        material_score = {'white': 0, 'black': 0}
        captured_pieces = {'white': [], 'black': []}
        piece_values = {'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9}

        # Calcula as pontuações baseadas nas peças restantes no tabuleiro
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece:
                color = 'white' if piece.color == chess.WHITE else 'black'
                material_score[color] += piece_values.get(piece.symbol().upper(), 0)

        # Calcula as peças capturadas subtraindo do total possível
        starting_pieces = {'P': 8, 'N': 2, 'B': 2, 'R': 2, 'Q': 1}
        for symbol, count in starting_pieces.items():
            white_captured = count - sum(1 for p in self.board.pieces(chess.PIECE_SYMBOLS.index(symbol.lower()), chess.WHITE))
            black_captured = count - sum(1 for p in self.board.pieces(chess.PIECE_SYMBOLS.index(symbol.lower()), chess.BLACK))
            if white_captured > 0:
                captured_pieces['black'].extend([symbol] * white_captured)
            if black_captured > 0:
                captured_pieces['white'].extend([symbol] * black_captured)

        return material_score, captured_pieces

    def get_winner(self):
       def get_winner(self):
        if self.board.is_checkmate():
            return f"Xeque-mate! {'Pretas' if self.board.turn == chess.WHITE else 'Brancas'} vencem!"
        elif self.board.is_stalemate():
            return "Empate por afogamento (stalemate)."
        elif self.board.is_insufficient_material():
            return "Empate por material insuficiente."
        elif self.board.is_seventyfive_moves() or self.board.is_fivefold_repetition():
            return "Empate por regra dos 75 movimentos ou repetição quíntupla."
        elif self.board.is_variant_draw():
            return "Empate por regra da variante."
        else:
            return "A partida não terminou."
