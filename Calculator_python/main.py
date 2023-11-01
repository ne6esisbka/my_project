"""Calculator"""


import random
import time


class Games:
    def __init__(self, x, y=random.randint(4, 6)):
        self.x = x
        self.y = y

    def fight_player(self):
        if (self.x == 6 and self.y == 5) or (self.x == 5 and self.y == 4) or (self.x == 4 and self.y == 6):
            return f"Win Player 1"
        elif self.x == self.y:
            return 'Поздравляю у Вас НИЧЬЯ!!!'
        else:
            return "Win Computer!"

    def fight_two_players(self):
        if (self.x == 6 and self.y == 5) or (self.x == 5 and self.y == 4) or (self.x == 4 and self.y == 6):
            return f"Win Player 1"
        elif self.x == self.y:
            return 'Поздравляю у Вас НИЧЬЯ!!!'
        else:
            return "Win Player 2!"


def main():
    """Start game"""

    def printer_off(user):
        return (f"*********************************************\n"
                f"Попробуй выйграть у {user}\n"
                f"*********************************************\n"
                f"\n"
                f"Для хода выбираем :\n"
                f"{{камень}} = 6 или слово 'камень'\n"
                f"{{ножницы}} = 5 или слово 'ножницы'\n"
                f"{{бумага}} = 4 или слово 'бумага' \n")

    print(f"Добро пожаловать в игру {{камень}} {{ножницы}} {{бумага}} !\n"
          f"Выберите режим игры :\n"
          f" SinglePlay = 1\n"
          f" MultiPlay = 2\n")

    game_selection = int(input("Сделай выбор = "))

    if game_selection == 1:
        print(printer_off('компьютерных мозгов'))
        
        player = Games(x=int(input("Player = ")))
        if 3 < player.x < 7:
            print(f"Hero = {player.x} && Computer = {player.y}\n")
            print(f'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
                  f'{player.fight_player()}!!! \n'
                  f'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
        else:
            print("Жульничаешь? Computer Win!!!!")

    elif game_selection == 2:
        print(printer_off('Товарища'))
        two_players = Games(x=int(input("Player 1 = ")), y=int(input('Player 2 = ')))
        if 3 < two_players.x < 7 and 3 < two_players.y < 7:
            print(f"Player_1 = {two_players.x} && Player_2 = {two_players.y}\n")
            print(f'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n'
                  f'{two_players.fight_two_players()}!!! \n'
                  f'@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n')
        else:
            print("Жульничаете? Computer Win!!!!")

    else:
        return "FATAL ERROR"

    time.sleep(5)
    main()


if __name__ == "__main__":
    main()

