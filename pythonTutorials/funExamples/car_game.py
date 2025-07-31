command = ""
state = False
while True:
    command = input("> ").lower()
    if command == "help":
         print("""
start - to start the car
stop - to stop the car
quit - to exit the game""")
         
    elif command == "start":
        if state:
            print("Car already started!")
        else:
            state = True
            print("Car started.")

    elif command == "stop":
        if  not state:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")

    elif command == "quit":
        break
    else:
        print("I don't understand that...")


