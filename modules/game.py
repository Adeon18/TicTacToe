"""
Main Game module
"""
from board import Board

boardd = Board()
counter = 1
result = "continue"
while result == "continue":
    for player in [boardd.USR_SYMBOL, boardd.PC_SYMBOL]:
        print(f"Step {counter}")
        if player == boardd.USR_SYMBOL:
            while True:
                inputt = input("Enter first pos,second pos: ").split(',')
                coords = (int(inputt[0]), int(inputt[1]))
                try:
                    boardd.make_move(coords, boardd.USR_SYMBOL)
                    break
                except IndexError:
                    print("Position occupied!")
                    continue
            print(boardd)
        else:
            boardd.make_computer_move()
            print(boardd)
        result = boardd.get_status()
        if result == boardd.USR_SYMBOL:
            print("YOU WON!")
            break
        elif result == boardd.PC_SYMBOL:
            print("BOT WON!")
            break
        elif result == "draw":
            print("DRAW!")
            break
        counter += 1