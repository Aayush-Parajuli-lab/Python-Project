import random
while True:
    playing = input("Do You wanna play (yes/no) ")
    if playing.lower() != "yes":
        break
    
    top_of_range = input("\nEnter the number: ")

    if top_of_range.isdigit():
        top_of_range = int(top_of_range)

        if top_of_range <= 0 :
            print("\nPlease enter number greater than 0.")
            continue
    else: 
        print("Please enter number next time.")
        continue

    number = random.randrange(1,top_of_range)
    score = 0
    while True:
        user_number = input("\nEnter the Guess: ")
        if user_number.isdigit():
            user_number = int(user_number) 
        
        else: 
            print("\nPlease enter number next time.")
            continue

        if user_number== number:
            print("\nCongrats you have guessed the correct number")
            break
        else:
            if user_number > number:
                print("The random number is smaller than Guess number")
                continue
        
            else:
                print("\nThe random number is greater than Guess number")
                continue
        print("wanna play again ...")
print("\nThanks for playing")


