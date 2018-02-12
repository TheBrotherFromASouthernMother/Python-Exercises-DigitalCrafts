import json

mainMenu = {
    'header' : 'Electronic Phone Book\n=====================',
    "1": "Look up an entry",
    "2": "Set an entry",
    "3": "Delete an entry",
    "4": "List all entries",
    "5": "Quit"
    

}

phonebook_dict = {
    "Chris": {
        "name": "Chris",
        "phone_number": "7"
    }
}

def saveEntry():
    name = str(input("Name? "))
    phone_number = str(input("Phone Number? "))
    phonebook_dict[name] = {
        'name': name,
        "phone_number": phone_number
        }
    print("Added entry:\n \'name: {}\nphone: {}\'\nto phonebook". \
    format(phonebook_dict[name]['name'], phonebook_dict[name]['phone_number']))

def printAllEntries(dictionary):
    for key in dictionary:
        print(key, dictionary[key])

def deleteEntry(dictionary):
    entryToDelete = str(input("Please input the contact name you would like to delete: "))
    if dictionary[entryToDelete]:
        del dictionary[entryToDelete]



def showMenu():
    print(mainMenu['header'])
    for key in mainMenu.keys():
        if key == 'header':
            pass
        else:    
            print(key, mainMenu[key])

def userRoute():
    userCmd = int(input('What would you like to do? (1-5) '))
    while userCmd < 0 or userCmd > 5:
        userCmd = int(input('What would you like to do? (1-5) '))
    if userCmd == 5:
        print('Exiting...')
        return 0
    elif userCmd == 4:
        printAllEntries(phonebook_dict)
    elif userCmd == 3:
        deleteEntry(phonebook_dict)
        print(phonebook_dict)
    elif userCmd == 2:
        saveEntry()
    
        

    



# with open('phonebook.json', 'wb') as fh:


showMenu()
userRoute()