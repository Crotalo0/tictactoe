# Tic Tac Toe program
from random import randint


# TODO: What to do?
#   - Define 2D array DONE
#   - Fill array with user input DONE
#       - Get user input DONE
#   - Check for rows and diagonals DONE
#   - 2 Player game DONE
#   - Add AI


def has_won(table: list) -> (bool, str):
    """ Check for winners """

    # Row 0, 1 ,2 all equal
    for i1 in range(3):
        if table[i1][0] == table[i1][1] and table[i1][1] == table[i1][2]:
            # Check if character is not starting one
            if not table[i1][0] == "-":
                return True, table[i1][0]
    # Column 0, 1, 2 all equal
    for i2 in range(3):
        if table[0][i2] == table[1][i2] and table[0][i2] == table[2][i2]:
            if not table[0][i2] == "-":
                return True, table[2][i2]
    # Diagonals
    if table[0][0] == table[1][1] and table[1][1] == table[2][2]:
        if not table[0][0] == "-":
                return True, table[0][0]
    elif table[0][2] == table[1][1] and table[1][1] == table[2][0]:
        if not table[2][0] == "-":
                return True, table[2][0]
    return False, "None"


def table_updater(table: list, p: tuple, symbol: str) -> list:
    """ Update board with symbol in p position """
    row, col = int(p[0]) - 1, int(p[1]) - 1
    table[row][col] = symbol
    return table


def table_printer(table: list) -> None:
    """ Board formatter """
    print('\n',table[0],'\n',table[1],'\n',table[2],'\n')


def main():
    # Tris board
    tris = [[ "-", "-", "-"],
            [ "-", "-", "-"],
            [ "-", "-", "-"]]

    possible_moves = [('1','1'),('1','2'),('1','3'),
                      ('2','1'),('2','2'),('2','3'),
                      ('3','1'),('3','2'),('3','3')]


    # Counter to check turn order
    turn = randint(0, 1)
    # Game loop
    going = True
