print(f"Hello! I have a thrilling story to tell you about a mouse!")
print(f"Before the story begins, I have a couple questions for you to answer.")
print(f"After typing your answers, be sure to press the enter key.")
input(f"\nPress the enter key to continue...") 

mouseName = input("\nWhat would you like to name the mouse:  ")
favoriteFood = input("What is your favorite food:  ")
season = input ("What is your favorite season:  ")
favoriteFlower = input("What is your favorite flower:  ")
favoriteColor = input("What is your favorite color:  ") 

print(f"\nReadyyyy LET'S GOOOO!!")
print(f"Once upon a time there was mouse named {mouseName}.")
print(f"{mouseName} lives out in a cornfield in the country.")
print(f"One day {mouseName} decided to go look for {favoriteFood}.") 
print(f"While looking for {favoriteFood} he saw a farm house!") 
print(f"This {favoriteColor} house he had not seen before!")

goTofarmHouse = input (f"\nShould {mouseName} go to the farm house? Type yes or no:  ")
if goTofarmHouse == "yes":
    print(f"{mouseName} heads to the farm house and sees a family and their dog outside on a {season} day.")
    print(f"The family's dog spots {mouseName} and runs after him, chasing him away!")
    print(f"{mouseName} runs as fast as he can to get away.")
    print(f"No luck in getting any {favoriteFood} from there today!")
else:
    print(f"{mouseName} sits on the edge of the cornfiedl and watches the family and their dog.")
    print(f"He watches them enjoy the {season} day!")
    print(f"After watching a while he decides it's time to move on and keep looking for some food.")
    
goTospookyHouse = input(f"n\{mouseName} continues to walk along and sees an abandon SPOOKY house. Should {mouseName} go to the spooky house? Type Yes or no:  ")
while goTospookyHouse.lower() != "yes" and goTospookyHouse.lower != "no":
    goTospookyHouse = input(f"Please type yes or no:  ")
    
if goTospookyHouse == "yes":
    print(f"\nHoping to find some {favoriteFood} at this place, {mouseName} heads on over to the SPOOKY house.")
    print(f"{mouseName} Enters the house and scurries to the kitchen to see what can be scavenged.")
    print(f"Upon entering the kitchen {mouseName} sees a GHOST floating in front of the fridge!!")
    print(f"Scared out of his mind, {mouseName} runs out of the house!!")
else:
    print(f"Too aftaid of the SPOOKY house, {mouseName} heads to the back to seee if any food can be found.")
    print(f"Around the back of the house the overgrown garden looks like a jungle.")
    print(f"Too afraid of the darkness, from what looks like a forbidden forrest, {mouseName} leaves.")