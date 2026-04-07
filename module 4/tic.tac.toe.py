Board = {'7': '', '8': '', '9': '',
         '4': '', "5": '', '6': '',
         '1': '', '2': '', '3': ''}

Board_keys = []

for key in Board:
    Board_keys.append(key)


def printboard(board):
    print(board['7']+'|'+board['8']+'|'+board['9'])
    print('-----')
    print(board['4']+'|'+board['5']+'|'+board['6'])
    print('-----')
    print(board['1']+'|'+board['2']+'|'+board['3'])


def game():
    turn = 'x'
    count = 0

    for i in range(10):
        printboard(Board)
        print("its your turn ," + turn + ".Move to which place?")
        move = input()
        if Board[move] == '':
            Board[move] = turn
            count += 1

        else:
            print("the slot is already taken Which to move")
            continue

        if count >= 5:
            if Board['7'] == Board['8'] == Board['9'] != '':
                printboard(Board)
                print("Game over")
                print("****"+turn+"won.****")
                break

            elif Board['4'] == Board['5'] == Board['6'] != '':
                printboard(Board)
                print("Game over")
                print("****"+turn+"won.****")
                break

            elif Board['1'] == Board['2'] == Board['3'] != '':
                printboard(Board)
                print("Game over")
                print("****"+turn+"won.****")
                break

            elif Board['1'] == Board['4'] == Board['7'] != '':
                printboard(Board)
                print("Game over")
                print("****"+turn+"won.****")
                break

            elif Board['2'] == Board['5'] == Board['8'] != '':
                printboard(Board)
                print("Game over")
                print("****"+turn+"won.****")
                break

            elif Board['3'] == Board['6'] == Board['9'] != '':
                printboard(Board)
                print("Game over")
                print("****"+turn+"won.****")
                break

            elif Board['7'] == Board['5'] == Board['3'] != '':
                printboard(Board)
                print("Game over")
                print("****"+turn+"won.****")
                break

            elif Board['1'] == Board['5'] == Board['7'] != '':
                printboard(Board)
                print("Game over")
                print("****"+turn+"won.****")
                break

        if count == 9:
            print("game over")
            print("its a tie")
            break

        if turn == 'x':
            turn = 'O'

        else:
            turn = 'x'

    restart = input("do you want to play again y/n")
    if restart == "y" or restart == "Y":
        for key in Board_keys:
            Board[key] = ""

        game()


if __name__ == "__main__":
    game()
