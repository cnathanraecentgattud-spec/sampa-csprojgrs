import time # for timed outputs
def intro():
    print("    _------------_      ")
    print("   /||||||||||||||\                    ")
    print("  /|||||||||||||||||\               ")
    print("  |||||||||||||||||||\                   ")
    print("   \|||||||/                  ")
    print("     \|||||\                  ")
    print("       \|||||\             ")
    print("         \||||||\       ")
    print("         /|||||||||\         " )
    print("        /||||||||||||                 ")
    print("  |||||||||||||||||||                    ")
    print("  |||||||||||||||||/                         ")
    print("  |||||||||||||                          ")

    print("Welcome to (insert game name)!")
    name = input("What is your name? ")
    time.sleep(2)
    print(f"{name}..")   # name input
    print("...")
    time.sleep(2)
    print("born april 11, 1954..")
    print("designated for the earliest bus en route to purgatory..")
    time.sleep(1)
    print("based on your credentials, you are eligible for a free reading on your mortal life.")
    time.sleep(1)
    print("now, where would we like to begin?")
    time.sleep(1)
    print()
    print("ENTER 1 TO BE ENLIGHTENED")    # choice display
    time.sleep(1)
    print("ENTER 2 TO REMINISCE")
    time.sleep(1)
    print("ENTER 3 TO BOARD")
    time.sleep(1)
    choice = input("remember, time waits for no one..!")
    if choice == "1":
            game()
    elif choice == "2":
            background(name)
    elif choice == "3":
            end()


def game():
    print("WIP")

def background(name):
    time.sleep(2)
    print("i see..")
    time.sleep(1)
    print("you forgot your origins?")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("no matter, i shall grant what is due of me..")
    time.sleep(2)
    print("...")
    time.sleep(1)
    print("which of the ■■■'s rays shall i shine upon you?")
    print("the wake of DAWN (1)")
    print("the bask of NOON (2)")
    print("the last of DUSK (3)")
    time.sleep(1)
    print("")
    print(f"DAWN: is {name} really my name?")
    time.sleep(1)
    print(f"NOON: what put me in that mortal position?")
    time.sleep(1)
    print(f"DUSK: how did i end up here?")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("STYGIAN: who are you?")
    time.sleep(2)
    ray = input("go on..")
    if ray == "1":
        time.sleep(1)
        name_change = input("then shall you wish to change it then?")
        if name_change == "1":
            name = input("then by virtue of ■■■■, state your desired name: ")
            print(f"welcome to the fork again, {name}.")



def end():
    print("WIP")



                        #yoyoyoyoyoyo (comment test for update across device(67))
                        # test comment
if __name__ == "__main__":

    intro()







