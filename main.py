def printBoard(board):
    count = 0
    print("-------------------")
    for word in board:
        print("|" + word + "\t", end='')
        count = count + 1
        if count % 3 == 0:
            print("|\n-------------------")

def printAvailablePositions(board):
    print("Available positions")
    count = 0
    for word in board:
        if word == "":
            print(str(count) + " ", end='')
        else:
            print("X ", end='')

        if count == 2 or count == 5 or count == 8 and count != 0:
            print("")
        count = count + 1
    print("")


def chooseWord(words, used, word):
    if (word in words) and (word not in used):
        words.remove(word)
        used.append(word)
        return True
    else:
        print(word + " incorect", end=" ")
        return False


def changePlayer(currentPlayer):
    if currentPlayer == 1:
        return 2
    elif currentPlayer == 2:
        return 1


def insertAtPosition(index, board, word):
    if (not isinstance(index, int)):
        print("Sorry " + index + " is not a number")
        return False
    elif (index not in range(9)):
        print(str(index) + " is not 1-8")
        return False
    elif (not board[index] == ""):
        print("Sorry " + board[index] + " already exists at index " + str(index))
        return False
    else:
        board[index] = word
        return True


def wordsAreEqual(word1, word2, word3):
    if(word1 == "" or word2 == "" or word3 == ""):
        return False

    if (word1[1] == word2[1] and word2[1] == word3[1]):
        return True
    else:
        return False


def checkRows(board):
    for index in range(3):
        if (wordsAreEqual(board[index * 3], board[(index * 3) + 1], board[(index * 3) + 2])):
            return True
    return False

def checkCols(board):
    for index in range(3):
        if (wordsAreEqual(board[index], board[index + 3], board[index + 6])):
            return True
    return False


def checkLeftDiag(board):
    if wordsAreEqual(board[0], board[4], board[8]):
        return True
    else:
        return False


def checkRightDiag(board):
    if wordsAreEqual(board[2], board[4], board[6]):
        return True
    else:
        return False


def main():
    board = ["", "", "",
             "", "", "",
             "", "", ""]
    #         0   1   2
    #         3   4   5
    #         6   7   8

    words = ["hen", "bee", "less", "air", "bits", "lip", "soda", "book", "lot"]
    used = []
    gameOver = False
    player = 1

    print("Starting Tic Tac Toe")
    # printBoard(words)

    while not gameOver:

        printBoard(board)
        print("It is player " + str(player) + "'s turn")
        print("available words to choose from...")
        print(words)
        # player chooses thier work
        wordFound = False
        word = ""
        while not wordFound:
            word = input("Please choose a word ")
            wordFound = chooseWord(words, used, word)

        printAvailablePositions(board)
        validIndex = False
        while not validIndex:
            index = int(input("Please chose a valid number to insert your word "))
            validIndex = insertAtPosition(index, board, word)

        #check win conditions
        if len(words) == 0:
            print("stalemate. Game Over.")
            gameOver = True

        if checkRows(board) or checkCols(board) or checkLeftDiag(board) or checkRightDiag(board):
            gameOver = True

        if gameOver:
            print("Player " + str(player) + " has won!")
        else:
            player = changePlayer(player)


if __name__ == '__main__':
    main()

