print(f"Hello! I have a thrilling story to tell you about a mouse!")
print(f"Before the story begins, I have a couple questions for you to answer.")
print(f"After typing your answers, be sure to press the enter key.")
input(f"\nPress the enter key to continue...") 

keepPlaying = "yes"
while keepPlaying.lower() == "yes":

    mouseName = input("\nWhat would you like to name the mouse:  ")
    while len(mouseName) == 0:
        mouseName = input(f"Please enter a name:  ")

    favoriteFood = input("What is your favorite food:  ")
    while len(favoriteFood) == 0:
        favoriteFood = input(f"Please enter a food:  ")

    season = input ("What is your favorite season:  ")
    while len(season) == 0:
        season = input(f"Please enter a season:  ")
   

    favoriteFlower = input("What is your favorite flower:  ")
    while len(favoriteFlower) == 0:
        favoriteFlower = input(f"Please enter a flower:  ")

    favoriteColor = input("What is your favorite color:  ") 
    while len(favoriteColor) == 0:
        favoriteColor = input(f"Please enter a color:  ")


    print(f"\nReadyyyy LET'S GOOOO!!")
    print(f"Once upon a time there was mouse named {mouseName}.")
    print(f"{mouseName} lives out in a cornfield in the country.")
    print(f"One day {mouseName} decided to go look for {favoriteFood}.") 
    print(f"While looking for {favoriteFood} he saw a farm house!") 
    print(f"This {favoriteColor} house he had not seen before!")

    goTofarmHouse = input (f"Should {mouseName} go to the farm house? Type yes or no:  ")
    while goTofarmHouse.lower() != "yes" and goTofarmHouse.lower() != "no":
        goTofarmHouse = input(f"Please type yes or no:  ")
    
    if goTofarmHouse == "yes":
        print(f"...")
        print(f"{mouseName} heads to the farm house and sees a family and their dog outside on a {season} day.")
        print(f"The family's dog spots {mouseName} and runs after him, chasing him away!")
        print(f"{mouseName} runs as fast as he can to get away.")
        print(f"No luck in getting any {favoriteFood} from there today!")
    else:
        print(f"...")
        print(f"{mouseName} sits on the edge of the cornfield and watches the family and their dog.")
        print(f"He watches them enjoy the {season} day!")
        print(f"After watching awhile he decides it's time to move on and keep looking for some food.")
    
    goTospookyHouse = input(f"{mouseName} continues to walk along and sees an abandon SPOOKY house. Should {mouseName} go to the spooky house? Type yes or no:  ")
    while goTospookyHouse.lower() != "yes" and goTospookyHouse.lower() != "no":
        goTospookyHouse = input(f"Please type yes or no:  ")
    
    if goTospookyHouse == "yes":
        print(f"...")
        print(f"Hoping to find some {favoriteFood} at this place, {mouseName} heads on over to the SPOOKY house.")
        print(f"{mouseName} Enters the house and scurries to the kitchen to see what can be scavenged.")
        print(f"Upon entering the kitchen {mouseName} sees a GHOST floating in front of the fridge!!")
        print(f"Scared out of his mind, {mouseName} runs out of the house!!")
    else:
        print(f"...")
        print(f"Too afraid of the SPOOKY house, {mouseName} heads to the back to see if any food can be found.")
        print(f"Around the back of the house the overgrown garden looks like a jungle.")
        print(f"Too afraid of the darkness, from what looks like a forbidden forrest, {mouseName} leaves.")
    
    if goTofarmHouse == "yes" and goTospookyHouse == "yes":
        print(f"...")
        print(f"After and exhusting day of running, our mouse heads home.")
        print(f"{mouseName} gets home to find a nice meal on the table from his wife!")
    elif goTofarmHouse == "no" and goTospookyHouse == "no":
        print("...")
        print(f"Defeated with an empty belly, {mouseName} heads home.")
        print(f"On his way home he finds a Happy Meal on the side of the road!!")
        print(f"SCORE ONE FOR THE LITTLE GUY!!")
        print(f"{mouseName} feels great bringing home some chicky nugs.")
    else:
        print(f"...")
        print(f"After an adventurous day, {mouseName} heads home.")
        print(f"On his way he sees a {favoriteColor} {favoriteFlower} and grabs it for his wife.") 
        print(f"He remembers how lucky he is to have her.")
        print(f"Once home, she surprises him with {favoriteFood}!!")
    
    print(f"The end!") 
    keepPlaying =input(f"Do you want to play again? Enter yes or no:  ")
    while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
        keepPlaying = input(f"Please type yes or no:  ")
    
    
    