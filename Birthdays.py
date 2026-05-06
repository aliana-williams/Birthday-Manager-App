birthdays = {}
#add your statements with the correct formating
while True:
    print('1. Look up a birthday ')
    print('2. Add a new birthday')
    print('3. Change a birthday')
    print('4. Delete a birthday')
    print('5. Quit the program')
    print('Please press number 2 to start the program')

#Number 1 question
    number = input("Please select a number:")
    if number == "1":
        name = input("Please enter a name to look up:")
        if name in birthdays:
            print(f'{name} has a birthday of {birthdays[name]}')
        else:
            print(f'{name} does not exist')
#Number 2 question
    elif number == "2":
        name = input("Please enter new name:")
        birthday = input("Please enter a new birthday:")
        birthdays[name] = birthday
        print("Birthday added.")
        if birthday in birthdays:
            print("Birthday already exists.")
#Number 3 question
    elif number == "3":
        name = input("Please enter an existing name:")
        if name in birthdays:
            birthday = input("Enter the new birthday: ")
            birthdays[name] = birthday
            print("Birthday updated.")
        else:
            print('Name not found')
#Number 4 question
    elif number == "4":
        name = input("Please enter an existing name to delete:")
        if name in birthdays:
            del birthdays[name]
            print("You have deleted a birthday")
        else:
            print('Name not found.')
#Number 5 question
    elif number == "5":
            print('program ended')

            break

    else:
        print('Please enter a valid number')
