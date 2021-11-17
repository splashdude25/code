''' Briggs '''

invalidResponse = True
while invalidResponse:
    player = int(input("Which player wants to start? "))
    if player == 1:
        print("Player 1 will start first.")
        currentPlayer = player
        invalidResponse = False
    elif player == 2:
        print("Player 2 will start first.")
        currentPlayer = player
        invalidResponse = False
    else:
        print("Please assign yourself an integer of 1 or 2")
        invalidResponse = True


def displayGame(listOfBins):
    print(listOfBins)
    return


def removeMatches(binNumber, matchesToRemove, listOfBins):
    for i in range(len(listOfBins)):
        if listOfBins[binNumber] < 0 or listOfBins[binNumber] < matchesToRemove or matchesToRemove == 0:
            print("")
            print("False, "+str(matchesToRemove)+" matches cannot be removed from bin "+str(binNumber)+".")
            print("Please re-enter a valid number of matches to remove from bin "+str(binNumber)+".")
            print("")
            return False
            break
        elif binNumber == i and matchesToRemove <= listOfBins[i]:
            a = listOfBins[i]-matchesToRemove
            listOfBins[i] = a
            display = displayGame(listOfBins)
            return True
        elif sum(listOfBins) == 0:
            return
    return


def checkGameEnd(listOfBins):
    if sum(listOfBins) == 0:
        print("The game is over.")
        return True
    else:
        return False
    return


def playerTurn(listOfBins):
    currentPlayer = player
    while True:
        if currentPlayer == 2:
            binNumber = int(input("Player 2, please choose a bin: "))
            if binNumber < 0 or binNumber >= len(listOfBins):
                print("")
                print("False, "+str(binNumber)+" exceeds the amount of bins available.")
                print("Please select a valid bin number that is less than "+str(len(listOfBins))+".")
                print("")
                continue
            matchesToRemove = int(input("How many matches do you want to remove? "))
            sumOfList = sum(listOfBins)
            p2Turn = removeMatches(binNumber, matchesToRemove, listOfBins)
            if sumOfList == sum(listOfBins):
                continue
            elif sum(listOfBins) == 0:
                p2GameEnd = checkGameEnd(listOfBins)
                print("Player",currentPlayer,"loses the game.")
                return
            currentPlayer = 1
        else:
            binNumber = int(input("Player 1, please choose a bin: "))
            if binNumber < 0 or binNumber >= len(listOfBins):
                print("")
                print("False, "+str(binNumber)+" exceeds the amount of bins available.")
                print("Please select a valid bin number that is less than "+str(len(listOfBins))+".")
                print("")
                continue
            matchesToRemove = int(input("How many matches do you want to remove? "))
            sumOfList = sum(listOfBins)
            p1Turn = removeMatches(binNumber, matchesToRemove, listOfBins)
            if sumOfList == sum(listOfBins):
                continue
            elif sum(listOfBins) == 0:
                p1GameEnd = checkGameEnd(listOfBins)
                print("Player",currentPlayer,"loses the game.")
                return
            currentPlayer = 2


playerTurn([7, 7, 7, 7, 7])
