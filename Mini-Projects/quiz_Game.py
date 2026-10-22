print("Welcome to the quiz !")

while True:
    playing =input("\nDo you want to play ? (Yes/No) \n")

    if playing.lower() != "yes":
        break;
   
    print("\nOkay let's play\n")
    mark = 0
    answer = input("What does CPU stands for? \n")
    if answer.lower() == "central processing unit": 
        print("Correct!")
        mark += 1
    else:
        print("Incorrect!")

    answer = input("\nWhat does GPU stands for? \n")
    if answer.lower() == "graphic processing unit":
        print("Correct!")
        mark += 1
    else:
        print("Incorrect!")

    answer = input("\nWhat does CFA stands for? \n")
    if answer.lower() == "computer fundamental application":
        print("Correct!")
        mark += 1
    else:
        print("Incorrect!")

    answer = input("\nWhat does RAM stands for? \n")
    if answer.lower() == "random access memory":
        print("Correct!")
        mark += 1
    else:
        print("Incorrect!")

    print("\nyour total score is: " ,mark)

print("\nThanks for playing")
    
