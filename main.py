import time
import random
import sys

#function slows down speed that text displays, serves in place of print()
def slow_print(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()
    
#Game State 1
def intro():
    slow_print("You wake up in a dark, eerie forest.")
    slow_print("The moon barely lights the path ahead.")
    slow_print("You hear strange noises all around...")
    slow_print("Will you find a way out, or will the night consume you?")
    slow_print("")
    slow_print("You see two paths ahead:")
    slow_print("1. The narrow path into the dense trees.")
    slow_print("2. The faint trail towards a creepy old cabin.")
    choice = input("Which path do you take? (1 or 2) ")

    #sys.exit() allows for safe ending of program execution
    if choice == "exit":
        sys.exit("Thanks for playing!")

    while choice not in ['1', '2']:
        choice = input("Please choose 1 or 2: ")
    
    if choice == '1':
        forest_path()
    else:
        cabin_path()

#Game State 2A
def forest_path():
    slow_print("\nYou step cautiously into the thick forest.")
    slow_print("The sounds get louder, almost like whispers.")
    slow_print("Suddenly, you reach a fork in the path:")
    slow_print("1. Follow the left path towards an eerie glowing pond.")
    slow_print("2. Follow the right path deeper into the shadowy woods.")
    choice = input("Which way do you go? (1 or 2) ")

     #sys.exit() allows for safe ending of program execution
    if choice == "exit":
        sys.exit("Thanks for playing!")

    while choice not in ['1', '2']:
        choice = input("Please choose 1 or 2: ")

    if choice == '1':
        glowing_pond() #Game State 3AA 
    else:
        deeper_forest() #Game State 3AB

#Game State 3AA
def glowing_pond():
    slow_print("\nYou approach the glowing pond.")
    slow_print("The water shimmers unnaturally with a faint blue light.")
    slow_print("You notice something shiny at the bottom.")
    slow_print("Do you try to reach into the water to grab it? (y/n)")
    choice = input("> ").lower()

    #sys.exit() allows for safe ending of program execution
    if choice == "exit":
        sys.exit("Thanks for playing!")

    while choice not in ['y', 'n']:
        choice = input("Please enter y or n: ").lower()

    #Here we do not invoke a new game state; rather we just have different dialogue based on the y/n choice. We enter mysterious_ruins() regardless of player choice
    if choice == 'y': 
        slow_print("You dip your hand into the cold water...")
        slow_print("Suddenly, hands grab your wrist from below!")
        slow_print("You struggle and break free, but the pond's glow dims.")
        slow_print("In your hand, you clutch an ancient rusty key.")
        slow_print("You pocket the key and move on.")
        mysterious_ruins()
    else:
        slow_print("You decide not to risk it and step back.")
        slow_print("As you turn away, you hear a splash behind you...")
        slow_print("You run before seeing what it was.")
        mysterious_ruins()

#Game State 3AB
def deeper_forest():
    slow_print("\nYou walk deeper into the shadows.")
    slow_print("The trees seem to close in around you.")
    slow_print("Suddenly, a large wolf blocks your path, eyes glowing!")
    choice = input("Do you fight (f) or flee (l)? ")

    #sys.exit() allows for safe ending of program execution
    if choice == "exit":
        sys.exit("Thanks for playing!")

    while choice.lower() not in ['f', 'l']:
        choice = input("Please choose f or l: ")

    if choice.lower() == 'f':
        slow_print("You ready yourself to fight the wolf.")
        if random.random() < 0.7:
            slow_print("You scare the wolf away with a loud shout!")
            mysterious_ruins()
        else:
            slow_print("The wolf attacks and you fall to the ground.")
            slow_print("Your vision fades as the wolf closes in...")
            slow_print("You died. Game Over.")
            return
    else:
        slow_print("You run as fast as you can, but your foot catches on a root.")
        slow_print("You fall and the wolf is upon you.")
        slow_print("You died. Game Over.")
        return

#Game State 4ABA
def mysterious_ruins():
    slow_print("\nYou come upon ancient ruins covered in moss.")
    slow_print("There’s an old stone door with a keyhole.")
    slow_print("Do you try to use the rusty key you found? (y/n)")
    choice = input("> ").lower()
    #sys.exit() allows for safe ending of program execution
    if choice == "exit":
        sys.exit("Thanks for playing!")
    while choice not in ['y', 'n']:
        choice = input("Please enter y or n: ").lower()

    if choice == 'y':
        slow_print("You insert the key and turn it with effort.")
        slow_print("The door grinds open to reveal a dark staircase leading down.")
        basement()
    else:
        slow_print("You decide not to try the door.")
        slow_print("Suddenly, the ground trembles and the ruins collapse!")
        slow_print("You run and barely escape back to the forest edge.")
        slow_print("You are safe... for now.")
        slow_print("Thanks for playing!")

#Game State 5ABAA
def basement():
    slow_print("\nYou descend into the cold basement.")
    slow_print("A faint light flickers at the far end.")
    slow_print("You find a dusty journal on a pedestal.")
    slow_print("Do you read the journal? (y/n)")
    choice = input("> ").lower()
    #sys.exit() allows for safe ending of program execution
    if choice == "exit":
        sys.exit("Thanks for playing!")
    while choice not in ['y', 'n']:
        choice = input("Please enter y or n: ").lower()

    if choice == 'y':
        slow_print("The journal tells of a curse on this place.")
        slow_print("You realize the shadow that haunts the forest is trapped here.")
        slow_print("You must find a way to break the curse.")
        puzzle_room()
    else:
        slow_print("You leave the journal alone.")
        slow_print("Suddenly, the door slams shut above you.")
        slow_print("You are trapped with the darkness.")
        slow_print("You died. Game Over.")

#Game State 6ABAAA
def puzzle_room():
    slow_print("\nAt the end of the basement, you find a locked box.")
    slow_print("There is a riddle inscribed on it:")
    slow_print("'I speak without a mouth and hear without ears. I have nobody, but I come alive with the wind. What am I?'")
    answer = input("Your answer: ").lower().strip()

    if "echo" in answer:
        slow_print("The box clicks open!")
        slow_print("Inside, you find a glowing amulet.")
        slow_print("You wear it, and feel a wave of warmth and safety.")
        slow_print("The curse is lifted, and the forest lightens.")
        slow_print("You walk out of the ruins, free at last.")
        slow_print("Congratulations, you survived!")
    else:
        slow_print("Nothing happens. The room grows colder.")
        slow_print("The shadows close in around you.")
        slow_print("You died. Game Over.")


#Game State 2B
def cabin_path():
    slow_print("\nYou approach the creepy old cabin.")
    slow_print("The door creaks open by itself...")
    choice = input("Do you enter? (y/n): ").lower()
    #sys.exit() allows for safe ending of program execution
    if choice == "exit":
        sys.exit("Thanks for playing!")
    while choice not in ['y', 'n']:
        choice = input("Please enter y or n: ").lower()

    if choice == 'y':
        cabin_inside()
    else:
        slow_print("You decide not to enter.")
        slow_print("As you turn away, the ground shakes and the cabin collapses behind you.")
        slow_print("You run and find the edge of the forest. You are safe... for now.")
        slow_print("Thanks for playing!")

#Game State 3BA
def cabin_inside():
    slow_print("Inside, it's cold and dark.")
    slow_print("Suddenly, you hear footsteps behind you!")
    slow_print("You turn and see a shadowy figure.")
    action = input("Do you hide (h), confront (c), or run (r)? ").lower()
    #sys.exit() allows for safe ending of program execution
    if action == "exit":
        sys.exit("Thanks for playing!")
    while action not in ['h', 'c', 'r']:
        action = input("Please choose h, c, or r: ").lower()

    if action == 'h':
        slow_print("You hide behind some old furniture.")
        if random.random() < 0.6:
            slow_print("The figure passes by without noticing you. You find a hidden door behind the wall.")
            secret_room()
        else:
            slow_print("The figure spots you and drags you into darkness.")
            slow_print("You died. Game Over.")
    elif action == 'c':
        slow_print("You stand your ground.")
        if random.random() < 0.3:
            slow_print("The figure disappears—it was just a trick of the light!")
            slow_print("You find a key on the floor that unlocks the door.")
            slow_print("You escape the cabin and the forest beyond.")
            slow_print("Congratulations, you survived!")
        else:
            slow_print("The figure attacks you. You didn't survive.")
            slow_print("Game Over.")
    else:
        slow_print("You try to run but the door slams shut.")
        slow_print("You are trapped inside the cabin.")
        slow_print("You hear whispers growing louder...")
        slow_print("You died. Game Over.")

#Game State 4BAA
def secret_room():
    slow_print("\nYou enter a secret room filled with strange symbols and artifacts.")
    slow_print("On a pedestal lies an old box with a combination lock.")
    slow_print("You notice three symbols on the wall: a crescent moon, a skull, and a raven.")
    slow_print("You need to guess the right sequence of symbols to open the box.")
    slow_print("Options: moon, skull, raven")

    attempts = 3
    correct_code = ['moon', 'raven', 'skull']

    while attempts > 0:
        guess = input("Enter the sequence separated by spaces (e.g., moon skull raven): ").lower().split()
        if guess == correct_code:
            slow_print("The box clicks open revealing a glowing talisman.")
            slow_print("You take it and feel a protective aura surround you.")
            slow_print("You find a back door unlocked and escape the cabin.")
            slow_print("Congratulations, you survived!")
            return
        else:
            attempts -= 1
            slow_print(f"Wrong sequence. {attempts} attempts left.")

    slow_print("The box locks forever, and the room grows cold.")
    slow_print("You are trapped in the cabin forever.")
    slow_print("Game Over.")

#Main function. Prints welcome screen and queues intro() (Game State 1)
def main():
    slow_print("Welcome to Pythonic Horror!")
    slow_print("At any time, type exit to quit.")
    time.sleep(3)
    
    intro()
    

if __name__ == "__main__":
    main()
