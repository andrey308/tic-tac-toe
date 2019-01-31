"""This is game - "tic-toc-toe" classic text realization.
   May be in future I will spend more time to make an app
   but not now.  Game rules are easy - you choose tic or tac 
   to play and next - choose the place on field to tic or tac."""
import random

human = ''
AI = ''

def winning(field, player):
    if (
        (field[0] == player and field[1] == player and field[2] == player) or
        (field[3] == player and field[4] == player and field[5] == player) or
        (field[6] == player and field[7] == player and field[8] == player) or
        (field[0] == player and field[3] == player and field[6] == player) or
        (field[1] == player and field[4] == player and field[7] == player) or
        (field[2] == player and field[5] == player and field[8] == player) or
        (field[0] == player and field[4] == player and field[8] == player) or
        (field[2] == player and field[4] == player and field[6] == player) 
        ):
        return True
    else:
        return False

def ending(field):
    if winning(field, AI):
        print("You lose, sorry((")
    elif winning(field, human):
        print("You never win, fucking human")
    elif len(emptyPlace(field)) == 0:
        print("Tie, but in future, you lose")
    else: 
        return False
    return True

def emptyPlace(field):
    empty = list()
    for i in field:
        if i != "x" and i != "o":
            empty.append(int(i))
    return empty


class Move:
 
    def __init__(self, index=None, score=None):
        try:
            self.index = int(index)
        except TypeError:
            self.index = index
        try:
            self.score = int(score)
        except TypeError:
            self.score = score


def main():

    field = ["0", "1", "2",
             "3", "4", "5",
             "6", "7", "8"]

    end_of_game = False

    print("Choose your fighter: \"x\" or \"o\"")
    print("The one who chooses the cross walks first")
    
    global AI
    global human

    human = input("Your fighter: ")

    if human == "x":
        AI = "o"
        while not end_of_game:
            field_map(field)
            first_move = int(input("Ok. You move: "))
            field[first_move] = human
            
            end_of_game = ending(field)
            
            if end_of_game == True:
                break

            result = minimax(field, AI)        
            field[int(result.index)] = AI
            
            end_of_game = ending(field)
            
    elif human == "o":
        AI = "x"
        print("Ok. Commputer moves first.")
        while not end_of_game:
            result = minimax(field, AI)
            field[int(result.index)] = AI
            
            end_of_game = ending(field)
            if end_of_game == True:
                break

            field_map(field)
            first_move = int(input("Ok. You move: "))
            field[first_move] = human

            end_of_game = ending(field)
    else:
        print("Wrong symbol: please choose \"x\" or \"o\"")


def minimax(field, player, index=None):
    global human
    global AI
    moves = list()

    empty = emptyPlace(field)

    if winning(field, AI):
        return Move(index, 10)
    elif winning(field, human):
        return Move(index, -10)
    elif len(empty) == 0:
        return Move(index, 0)

    for i in empty:
        move = Move()
        move.index = field[i]
        field[i] = player

        if player == AI:
            result = minimax(field, human, move.index)
        else:
            result = minimax(field, AI, move.index)
        
        move.score = result.score
        field[i] = move.index
        moves.append(move)
    
    
    bestMove = 0
    if player == AI:
        bestScore = -10000;
        for i in moves:
            if i.score > bestScore:
                bestScore = int(i.score)
                bestMove = moves.index(i)
    else:
        bestScore = 10000;
        for i in moves:
            if i.score < bestScore:
                bestScore = int(i.score)
                bestMove = moves.index(i)
    
    return moves[bestMove]

def field_map(field):
    count = 1
    for i in range(9):
        print("|{0}|".format(field[i]), end='')
        if count%3 == 0:
            print('')
        count += 1
    print('')


if __name__ == "__main__":
    main()
