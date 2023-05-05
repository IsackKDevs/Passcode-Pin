def validate():
    goodnum = ['1234', '4321']
    value = int(input('Enter a pin: '))
    while type(value) == int:
        if value in goodnum:
            print("You can't use that")
        else:
            print("Good pin")
        break

validate()

    
   
    