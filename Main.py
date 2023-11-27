#inicia o jogo
import chess
from IPython.display import SVG, clear_output

if __name__ == "__main__":
    def main():
        chess_board = Chessboard()

        try:
            jogador_comeca = input("Você deseja começar? (s/n): ").strip().lower() == 's'

            while not chess_board.is_game_over():
                clear_output(wait=True)
                chess_board.display()

                if jogador_comeca:
                    jogador_move = input("Faça seu movimento: ")
                    if not chess_board.make_move(jogador_move):
                        print("Movimento inválido, tente novamente.")
                        continue
                else:
                    print("Stockfish está fazendo um movimento...")
                    chess_board.play_stockfish_move()

                jogador_comeca = not jogador_comeca

            # Exibe os dois últimos tabuleiros apenas se o jogo terminou
            print("\nÚltimos dois tabuleiros antes do final:")
            for svg_str in chess_board.board_history_svg[-2:]:
                display(SVG(svg_str))

            # Obtenha um resultado preciso e informativo
            game_result, score = chess_board.get_game_result()
            print(f"\n{game_result}")
            if score is not None:
                print(f"A pontuação da posição final é: {score}")

        except KeyboardInterrupt:
            print("\nJogo interrompido pelo usuário.")

    main()
