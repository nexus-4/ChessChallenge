# Inicia o jogo
if __name__ == "__main__":
    def main():
        print("Escolha o nível de dificuldade do Stockfish:")
        print("1. Aprendizado")
        print("2. Iniciante")
        print("3. Médio")
        print("4. Difícil")
        escolha = input("Digite o número da sua escolha (1-4): ").strip()

        niveis = {
            "1": 0,   # Aprendizado
            "2": 5,   # Iniciante
            "3": 10,  # Médio
            "4": 20   # Difícil
        }

        skill_level = niveis.get(escolha, 20)  # Default para "Difícil" se a entrada for inválida
        time_limit = 0.1  # Ajuste o limite de tempo conforme necessário

        chess_board = Chessboard(skill_level, time_limit)
        jogador_comeca = input("Você deseja começar? (s/n): ").strip().lower() == 's'

        while not chess_board.is_game_over():
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

            from IPython.display import clear_output
            clear_output(wait=True)

        print(chess_board.get_winner())

    main()
