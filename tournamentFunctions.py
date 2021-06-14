def addParts(participants, numPart):
    print('Participant Sign Up')
    print('====================')
    tempName = input("Participant Name: ")
    loop = True
    while loop is True:
        tempNum = input(f"Desired slot #(1-{numPart})(-1 to exit): ")
        if tempNum == '-1':
            loop = False
            break
        tempNum = int(tempNum) - 1
        if participants.get(tempNum) == None and tempNum <= int(numPart):
            participants.update({int(tempNum): tempName})
            loop = False
        else:
            print('Error: Invalid slot, try again.')
    return participants

def removeParts(participants, numPart):
    print('Participant Cancellation')
    print('========================')
    loop = True
    while loop is True:
        tempNum = input(f"Desired slot #(1-{numPart}) (-1 to exit): ")
        if tempNum == '-1':
            loop = False
            break
        tempNum = int(tempNum) - 1
        tempName = input("Participant Name: ")
        if participants.get(tempNum) == tempName:
            participants.update({int(tempNum): None})
            print(f'Success:\n{tempName} has been removed from slot {(tempNum + 1)}')
            loop = False
        else:
            print('Error: Name in slot does not match. Try again.')
    return participants

def viewParts(participants, numPart):
    print('View Participants')
    print('====================')
    tempNum = input(f"Desired starting slot #(1-{numPart}) (-1 to exit): ")
    if tempNum == '-1':
        loop = False
    tempNum = int(tempNum) - 1
    for key in participants.keys():
        if int(key) >= int(tempNum):
            print(f'{(int(key)+1)} : {participants[key]}')
    return participants


def quitParts(acess):
    print('Exit')
    print('=====')
    leave = input('Are you sure you want to exit? (y/n)')
    if leave.lower() == 'yes' or leave.lower() == 'y':
        print('Goodbye!')
        return False
    else:
        print('Returning to Menu\n')
        return True