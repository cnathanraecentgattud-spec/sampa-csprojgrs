import time
def intro():
    print("Welcome to (insert game name)!")
    name = input("What is your name? ")
    time.sleep(2)
    print(f"{name.upper()}?!")
    print("...")
    time.sleep(2)
    print(f"oh how i've long foreseen your arrival here, {name}..")
    print("now, where would we like to begin?")

intro()



