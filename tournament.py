import tournamentFunctions

try:
    print("Welcome to the Tournament")
    print('=========================')
    numPart = input("Enter the number of participants: ")
    access = True
    participants = dict.fromkeys((range(int(numPart))))
    print(f'{numPart} participant slots created.')

    while access == True:
        temp = 0
        
        print('Participant Menu')
        print('=================')
        print('1. Sign Up')
        print('2. Cancel Sign Up')
        print('3. View Participants')
        print('4. Exit')

        temp = input('Chose an action: (1-4) ')

        if temp == '1':
            tournamentFunctions.addParts(participants, numPart)

        elif temp == '2':
            tournamentFunctions.removeParts(participants, numPart)

        elif temp == '3':
            tournamentFunctions.viewParts(participants, numPart)

        elif temp == '4':
            access = tournamentFunctions.quitParts(access)

except:
    print('ERROR: Invalid Entry')