import time # for timed outputs
def intro():
    choice = 0
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
    input(choice)
    if choice == 1:
        if __name__ == "__main__":   # main menu to respective choices
            game()
    elif choice == 2:
        if __name__ == "__main__":
            background()
    elif choice == 3:
        if __name__ == "__main__":
            end()


def game():
    print("ok")

def background():
    print("i see..")
    time.sleep(1)
    print("you forgot your origins?")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("no matter, i shall grant what is due of me..")
    print("")

def end():
    print("oooooooookkkkk")



                        #yoyoyoyoyoyo (comment test for update across device(67))
                        # test comment

intro()




