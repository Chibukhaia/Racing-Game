from race import *


introduction = "Welcome to Car Race game! \n " \
               "Enter your answer based on your choice: \n" \
               "start - for starting the game  \n" \
               "Exit - to exit the game \n" \
               "Help _ to check the choice options \n" \
               "Results - to see results \n"

while True:
    print(introduction)

    command = input("> ").lower()
    if command == "start":
        race = do_race()
    elif command == "exit":
        print("Game exit")
        break
    elif command == "help":
        print("""
"start - for starting the game  \n" \
"Exit - to exit the game \n" \
"Help _ to check the choice options \n" \
"Results - to see results \n"
""")
    elif command == "results":
        with open("results.txt", "r") as result:
            print(result.read())
    else:
        print(" Sorry I don't understand, maybe try Help option ")

    play_again = input("Do you want to play again? (Y/N): ").lower()

    if play_again == "n":
        is_playing = False
        print("See you!")
        break

    if play_again == "y":
        continue

    print(f"Invalid option ({play_again}), must be Y/N")

