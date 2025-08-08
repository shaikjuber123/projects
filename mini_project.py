dictionary={}

while True:
    print('\nDicitionary Management System')
    print('1. Add a word')
    print('2. Search for meaning')
    print('3. Display all words')
    print("4. Update meaning")
    print("5. Delect word")
    print('6.Exit')
    
    choice=input("enter your choice:")

    if choice=='1':
        word=input("enter the word:").lower()
        meaning=input('enter the meaning:').lower()
        dictionary[word]=meaning
        print("word added sucessfully!")

    elif choice=='2':
        word=input("enter the word to search:").lower()
        if word in dictionary:
            print('meaning:',dictionary[word])
        else:
            print("word not found in the dictionary.")
    
    elif choice=='3':
        print(dictionary)

    elif choice=='4':
        word=input("enter the word to update:").lower()
        if word in dictionary:  
            new_meaning=input("enter the new meaning:").lower()
            dictionary[word]=new_meaning
            print('meaning update successfully!')
            print("updated meaning:",new_meaning)
        else:
            print("word not found in the dictionary.")
    
    elif choice=='5':
        word=input("enter the word to delete:").lower()
        if word in dictionary: 
            dictionary.pop(word)
            print("word deleted successfully!")
        
        else:
            print("word not found in the dictionary.")
    
    elif choice=='6':
        print("exiting program...")
        break
    
    else:
        print("invalid input!..")
