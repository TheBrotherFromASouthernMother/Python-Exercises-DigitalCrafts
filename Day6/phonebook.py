import json
import os.path

mainMenu = {
    'header' : 'Electronic Phone Book\n=====================',
    "1": "Look up an entry",
    "2": "Set an entry",
    "3": "Delete an entry",
    "4": "List all entries",
    "5": "Quit"  
}



def showMenu():
    print(mainMenu['header'])
    for key in mainMenu.keys():
        if key == 'header':
            pass
        else:    
            print(key, mainMenu[key])
    print("\n")


def lookUpEntry(dictionary):
    contactToLookUp = str(input("Please input a name you would like to find: "))
    if dictionary[contactToLookUp]:
        print(dictionary[contactToLookUp]['name'])
        print(dictionary[contactToLookUp]['phone_number'])


def saveEntry(dictionary):
    name = str(input("Name? "))
    phone_number = str(input("Phone Number? "))
    dictionary[name] = {
        'name': name,
        "phone_number": phone_number
        }
    print("Added entry:\n \'name: {}\nphone: {}\'\nto phonebook". \
    format(dictionary[name]['name'], dictionary[name]['phone_number']), "\n\n")


def deleteEntry(dictionary):
    entryToDelete = str(input("Please input the contact name you would like to delete: "))
    if dictionary[entryToDelete]:
        del dictionary[entryToDelete]



def printAllEntries(dictionary):
    for key in dictionary:
        print(key, dictionary[key], "\n")


def saveEntriesToFile():
    with open('phonebook.json', 'w') as myFile:
        json.dump(phonebook_dict, myFile)


def userRoute():
    userCmd = int(input('What would you like to do? (1-5) '))
    while userCmd < 0 or userCmd > 5:
        userCmd = int(input('What would you like to do? (1-5) '))
    if userCmd == 5:
        print('Exiting... \n')
        saveEntriesToFile()
        return 0
    elif userCmd == 4:
        printAllEntries(phonebook_dict)
    elif userCmd == 3:
        deleteEntry(phonebook_dict)
        print(phonebook_dict)
    elif userCmd == 2:
        saveEntry(phonebook_dict)
    elif userCmd == 1:
        lookUpEntry(phonebook_dict)
    
        

    

def initializePhoneBook():
    global phonebook_dict
    if os.path.isfile('phonebook.json'):
        with open('phonebook.json', 'r') as myFile:
            phonebook_dict = json.load(myFile)
    else:
        phonebook_dict = {
                "Chris": {
                    "name": "Chris",
                    "phone_number": "7"
                }
            }

    while True:
        showMenu()
        if userRoute() == 0:
            break




if __name__ == "__main__":
    initializePhoneBook()