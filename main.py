


import time # for timed outputs
def intro():
    print(r"""      
              /||||||||||||\         /|||||||||||||||||||\     |||||||||||||||||\       /||||||||||||\          /||||||||||||\          /||||||||\         /\        /|||||||\   /|||||\  /|||||\   /|||||||\                             .'¯¯'..'¯¯'.                                         /||||||||||||||||||\    |||||||||||||||||||  ||||||||||||||||||\   |||||  /||||||||||||||||||\    ||||||||||||||||||||||||||   ||||||     ||||||    |||||||                                    .'¯¯'..'¯¯'.                                                        
             /||||||||||||||\        |||||||||||||||||||||     ||||||||||||||||||       ||||||||||||||\        /||||||||||||||        /||||/   \||/       /||\       |||   |||   ||       ||        |||   |||                           .'            '.        ,   ,                          |||||||||||||||||||||   |||||||||||||||||||  ||||||||||||||||||||  |||||  |||||||||||||||||||||   ||                      ||   ||  ||     ||  ||    ||   ||                     '   '        .'            '.                                                                               
            /|||||||||||||||||\      |||||||||||||||||||||     ||||            \|       |||||||||||||||\      /|||||||||||||||        |||||              /|/\|\      ||||||||/   |||||    |||||     ||||||||/                         .'     ;;     ;; '.     ..'..''.   .                     ||||||/        \|||||   ||||||               ||||||/      \||||||  |||||  ||||||/        \|||||   |||||||||||    |||||||||||   ||  ||     ||  ||    ||   ||                .   .''..'..     .' ;;     ;;     '.                                           
            |||||||||||||||||||\     |/   |||||||||||   \|     ||||                     ||||||||||||||||\    /||||||||||||||||        \||||\   /||\     /||||||\     ||   \\\    ||       ||        ||   \\\                         .'     ;     ;      '...'      ;  '.''                    ||||||          |||||   ||||||               ||||||        ||||||  |||||  ||||||          |||||            ||    ||            ||  ||     ||  ||    ||   ||               ''.'  ;     '...'     ;      ;       '.                                                                                                                                                 
             \|||||||/        |/          |||||||||||          ||||                     |||||||||||||||||\__/|||||||||||||||||          \||||||||/     ///    \\\    ||    \\\   ||||||/  ||||||/   ||    \\\                       .'                           ; ;   :                       ||||||\        /|||||   ||||||               ||||||        ||||||  |||||  ||||||\        /|||||            ||    ||            ||  ||     ||  ||    ||   ||                  :   ; ;                           '.                           ; ;   :                                                     
               \|||||\                    |||||||||||          ||||    //|              ||||||||||||||||||||||||||||||||||||||                                                                                          _______    ,'       ;           ;         ;  .,`                       |||||||||||||||||||||   ||||||               ||||||||||||||||||||  |||||  |||||||||||||||||||||            ||    ||            ||  |||||||||  ||    ||   ||       _______                        
                \|||||\                   |||||||||||          |||||||||||              ||||||||||||/|||||||||||\|||||||||||||        -------------------------------------------------------------------------         _______    ':      ;;          ;;         .```                         ||||||||||||||||||||/   ||||||||||||||       |||||||||||||||||/    |||||  ||||||||||||||||||||/            ||    ||            ||  ||     ||  ||    ||   ||       _______                                                                                            
                 \||||||\                 |||||||||||          ||||    \\|              |||||||||||/  \|||||||/  \||||||||||||                                                                                          _______     :     ;;         ;;         ;``.                           |||||||/ \\\\\\\        ||||||               |||||||||||||||||\    |||||  |||||||/ \\\\\\\                 ||    ||            ||  |||||||||  ||    ||   ||       _______                                                                                               
                /|||||||||\               |||||||||||          ||||                     |||||||||||    \|||||/    ||||||||||||            /||||||\  \||/     /||||||||\    |||   ///  /|||||\   /|||||||\                          ,:    ;         ;          .```                             |||||||   \\\\\\\       ||||||               ||||||/      \||||\   |||||  |||||||   \\\\\\\                ||    ||            ||  ||     ||  ||    |||||||                                                               
         |\    /||||||||||||              |||||||||||          ||||                     |||||||||||     \|||/     ||||||||||||            |||  |||   ||    /||||/   \||/   |||  ///   ||        |||   |||                            :      ;   ;   ;     ,,..;`                               |||||||    \\\\\\\      ||||||               ||||||        ||||||  |||||  |||||||    \\\\\\\               ||    ||            ||  ||     ||  ||                                                                                                
         \||||||||||||||||||              |||||||||||          ||||           /|        |||||||||||      \|/      ||||||||||||            |||||||/   ||    |||||           |||||||    |||||     ||||||||/                            ,;    :;   ;   ;''. ,'                                    |||||||     \\\\\\\     ||||||               ||||||        ||||||  |||||  |||||||     \\\\\\\              ||    ||            ||  ||     ||  ||     //¯¯\\                                                                                      
          \|||||||||||||||/              /|||||||||||\         |||||||||||||||||        |||||||||||               ||||||||||||            ||         ||    \||||\   /||\   |||  \\\   ||        ||   \\\                              ;   ;  ; ; ; ;    '`                                     |||||||      \\\\\\\    |||||||||||||||||||  ||||||\      /||||||  |||||  |||||||      \\\\\\\             ||    ||            ||  ||     ||  ||    ||    ||                                                                          
           \|||||||||||||/     O        |||||||||||||||   O    ||||||||||||||||/   o    |||||||||||               ||||||||||||  O         ||        /||\     \||||||||/    |||   \\\  ||||||/   ||    \\\                            ;   ;  ; ;   ;;                                           |||||||       \\\\\\\   |||||||||||||||||||  |||||||||||||||||||/  |||||  |||||||       \\\\\\\            ||||||||            ||||||     ||||||     \\__//
                                                                                                                                                                                                                                    ;  ;     ;
                                                                                                                                                                                                                                    ; ;    
                                                                                                                                                                                                                                    ;;      
                                                                                                                                                                                                                                    ;
                                                                                                                                                                                                                                   
    """)


    print("Welcome to STEM Career Picker: Rebirth!")
    print("This game will try its best to determine a stable STEM job for you \n based on your experiences and opinions on things.")
    time.sleep(1)
    print("The gist of this fun test is that you'll be answering multiple questions \n with either the first or second prompt \n using 1 and 2 as responses")    # main intro and explanation w/ purpose
    time.sleep(3)
    print("Now, let us start with the first fundamental question of the test.. being....!!!!")  # last of bait and switch print statements
    time.sleep(1)
    name = input("What is your name? ")
    time.sleep(2)
    print(f"{name}..")   # name inputting
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
    print("ENTER 1 TO BE ENLIGHTENED")    # choice displays for the user
    time.sleep(1)
    print("ENTER 2 TO REMINISCE")
    time.sleep(1)    # pauses for effect
    print("ENTER 3 TO BOARD")
    time.sleep(1)
    choice = input("remember, time waits for no one..!")
    if choice == "1":
        game()
    elif choice == "2":
        background(name) # main fork to the three options
    elif choice == "3":
        end()
    else:
        print("either you have grown sick of knowledge or...\n you truly did not realize your error")




def game():
    time.sleep(2)
    print("a free reading i see..")
    time.sleep(2)
    print("the divination of ■■■■ tells me to get to know you a bit more.")
    time.sleep(1)
    print("-"*50)   # separator for readability
    print("PRESS 1 TO 'AGREE'")
    print("PRESS 2 TO DISAGREE")
    time.sleep(2)
    print("-" * 50)                    # constant directory to prevent any losses due to not knowing controls
    num = input("do you enjoy the process of problem solving?")
    if num == "1":
        print("-" * 50)
        print("PRESS 1 FOR 'THROUGH CREATING' ")
        print("PRESS 2 FOR 'BY THINKING' ")
        time.sleep(2)
        print("-" * 50)
        num = input("problem solving through creating or thinking?")
        if num == "1":
            print("-" * 50)
            print("PRESS 1 FOR 'CODING' ")
            print("PRESS 2 FOR 'BUILDING' ")
            time.sleep(2)
            print("-" * 50)
            num = input("rather coding or building?")
            if num == "1":
                print("-" * 50)
                print("the STEM aligned course you could have been in your premature mortal life would be..")
                print(courses[0]["specialty"])
                print("You could have learned so much... \n Perhaps through these electives:")
                print(f"Grade 11: {(courses[0]["grd11_subj"])}")
                print(f"Grade 12: {(courses[0]["grd12_subj"])}")
                print(f"You could have given back to society so much... \n There were opportunities a plenty:")
                print(f"Careers: {(courses[0]["careers"])}")
                print(" ")
                print(
                    "It certainly is a wither... \n Your mortal self truly was a special one... \n So many possibilities...wasted")

                # result of test based on the list of dictionaries at the bottom
            elif num == "2":
                print("-" * 50)
                print("PRESS 1 FOR 'SPECIFIC' ")
                print("PRESS 2 FOR 'GENERAL' ")
                time.sleep(2)
                print("-" * 50)
                num = input("a specific or general field?")
                if num == "1":
                    print("-" * 50)
                    print("the STEM aligned course you could have been in your premature mortal life would be..")
                    print(courses[1]["specialty"])
                    print("You could have learned so much... \n Perhaps through these electives:")
                    print(f"Grade 11: {(courses[1]["grd11_subj"])}")
                    print(f"Grade 12: {(courses[1]["grd12_subj"])}")
                    print(f"You could have given back to society so much... \n There were opportunities a plenty:")
                    print(f"Careers: {(courses[1]["careers"])}")
                    print(" ")
                    print(
                        "It certainly is a wither... \n Your mortal self truly was a special one... \n So many possibilities...wasted")

                elif num == "2":
                    print("-" * 50)
                    print("the STEM aligned course you could have been in your premature mortal life would be..")
                    print(courses[2]["specialty"])
                    print("You could have learned so much... \n Perhaps through these electives:")
                    print(f"Grade 11: {(courses[2]["grd11_subj"])}")
                    print(f"Grade 12: {(courses[2]["grd12_subj"])}")
                    print(f"You could have given back to society so much... \n There were opportunities a plenty:")
                    print(f"Careers: {(courses[2]["careers"])}")
                    print(" ")
                    print(
                        "It certainly is a wither... \n Your mortal self truly was a special one... \n So many possibilities...wasted")

                else:
                    print("Invalid input \n Enlightenment unsuccessful")
            else:
                print("Invalid input \n Enlightenment unsuccessful")

        elif num == "2":
            print("-" * 50)
            print("PRESS 1 FOR 'NATURE' ")
            print("PRESS 2 FOR 'NUMBERS' ")
            time.sleep(2)
            print("-" * 50)
            num = input("working with nature or with numbers?")
            if num == "1":
                print("-" * 50)
                print("PRESS 1 FOR 'OUT IN THE OPEN' ")
                print("PRESS 2 FOR 'IN A LAB' ")
                time.sleep(2)

                print("-" * 50)
                num = input("outside world, or in a laboratory?")
                if num == "1":
                    print("-" * 50)
                    print("the STEM aligned course you could have been in your premature mortal life would be..")   # data curator
                    print(courses[3]["specialty"])
                    print("You could have learned so much... \n Perhaps through these electives:")
                    print(f"Grade 11: {(courses[3]["grd11_subj"])}")
                    print(f"Grade 12: {(courses[3]["grd12_subj"])}")
                    print(f"You could have given back to society so much... \n There were opportunities a plenty:")
                    print(f"Careers: {(courses[3]["careers"])}")
                    print(" ")
                    print(
                        "It certainly is a wither... \n Your mortal self truly was a special one... \n So many possibilities...wasted")

                elif num == "2":
                    print("-" * 50)
                    print("the STEM aligned course you could have been in your premature mortal life would be..")
                    print(courses[6]["specialty"])
                    print("You could have learned so much... \n Perhaps through these electives:")
                    print(f"Grade 11: {(courses[6]["grd11_subj"])}")
                    print(f"Grade 12: {(courses[6]["grd12_subj"])}")
                    print(f"You could have given back to society so much... \n There were opportunities a plenty:")
                    print(f"Careers: {(courses[6]["careers"])}")
                    print(" ")
                    print(
                        "It certainly is a wither... \n Your mortal self truly was a special one... \n So many possibilities...wasted")
                else:
                    print("Invalid input \n Enlightenment unsuccessful")

            elif num == "2":
                print("-" * 50)
                print("PRESS 1 FOR ")
                print("PRESS 2 FOR SECOND OPTION")
                print("do you en■■■ ■■ ■■■■■■■ ■■■ ■■■■■■")    # area to snap back to lore | as much as possible pls don't remove w/o direction from nathan - tnx
                time.sleep(2)
                print("...")
                time.sleep(1)
                print("sorry, the ■■■■■ malfunctioned.")
                num = input("do you prefer familiarization or active memorization and application?")
                if num == "1":
                    print("-" * 50)
                    print("PRESS 1 TO AGREE")
                    print("PRESS 2 TO DISAGREE")
                    num = input("identifying structures or understanding & predicting?")
                    if num == "1":
                        print("-" * 50)
                        print("the STEM aligned course you could have been in your premature mortal life would be..")
                        print(courses[7]["specialty"])
                        print("You could have learned so much... \n Perhaps through these electives:")
                        print(f"Grade 11: {(courses[7]["grd11_subj"])}")
                        print(f"Grade 12: {(courses[7]["grd12_subj"])}")
                        print(f"You could have given back to society so much... \n There were opportunities a plenty:")
                        print(f"Careers: {(courses[7]["careers"])}")
                        print(" ")
                        print(
                            "It certainly is a wither... \n Your mortal self truly was a special one... \n So many possibilities...wasted")

                    elif num == "2":
                        print("-" * 50)
                        print("the STEM aligned course you could have been in your premature mortal life would be..")
                        print(courses[4]["specialty"])
                        print("You could have learned so much... \n Perhaps through these electives:")
                        print(f"Grade 11: {(courses[4]["grd11_subj"])}")
                        print(f"Grade 12: {(courses[4]["grd12_subj"])}")
                        print(f"You could have given back to society so much... \n There were opportunities a plenty:")
                        print(f"Careers: {(courses[4]["careers"])}")
                        print(" ")
                        print(
                            "It certainly is a wither... \n Your mortal self truly was a special one... \n So many possibilities...wasted")

                    else:
                        print("Invalid input \n Enlightenment unsuccessful")

                elif num == "2":
                    print("-" * 50)
                    print("the STEM aligned course you could have been in your premature mortal life would be..")  # database administrator
                    print(courses[5]["specialty"])
                    print("You could have learned so much... \n Perhaps through these electives:")
                    print(f"Grade 11: {(courses[5]["grd11_subj"])}")
                    print(f"Grade 12: {(courses[5]["grd12_subj"])}")
                    print(f"You could have given back to society so much... \n There were opportunities a plenty:")
                    print(f"Careers: {(courses[5]["careers"])}")
                    print(" ")
                    print(
                        "It certainly is a wither... \n Your mortal self truly was a special one... \n So many possibilities...wasted")

                else:
                    print("Invalid input \n Enlightenment unsuccessful")

            else:
                print("Invalid input \n Enlightenment unsuccessful")

        else:
            print("Invalid input \n Enlightenment unsuccessful")

    elif num == "2":
        print("-" * 50)
        print("PRESS 1 FOR APPLICATION ")
        print("PRESS 2 FOR DERIVATION ")
        time.sleep(2)
        num = input("real world and direct application or direct application in terms of analytics?")
        if num == "1":
            print("-" * 50)
            print("PRESS 1 FOR APPLICATION ")
            print("PRESS 2 FOR DERIVATION ")
            time.sleep(2)
            num = input("digital or outside work?")
            if num == "1":
                print("-" * 50)
                print("PRESS 1 FOR QUALITY ")
                print("PRESS 2 FOR PERFORMANCE ")
                time.sleep(2)
                num = input("quality control or performance overseer?")
                if num == "1":
                    print("-" * 50)
                    print("the STEM aligned course you could have been in your premature mortal life would be..") # aligned for a DATA CURATOR
                    print(courses[8]["specialty"])
                    print("You could have learned so much... \n Perhaps through these electives:")
                    print(f"Grade 11: {(courses[8]["grd11_subj"])}")
                    print(f"Grade 12: {(courses[8]["grd12_subj"])}")
                    print(f"You could have given back to society so much... \n There were opportunities a plenty:")
                    print(f"Careers: {(courses[8]["careers"])}")
                    print(" ")
                    print(
                        "It certainly is a wither... \n Your mortal self truly was a special one... \n So many possibilities...wasted")
                elif num == "2":
                    print("-" * 50)
                    print("the STEM aligned course you could have been in your premature mortal life would be..") # aligned for a DATABASE ADMINISTRATOR
                    print(courses[9]["specialty"])
                    print("You could have learned so much... \n Perhaps through these electives:")
                    print(f"Grade 11: {(courses[9]["grd11_subj"])}")
                    print(f"Grade 12: {(courses[9]["grd12_subj"])}")
                    print(f"You could have given back to society so much... \n There were opportunities a plenty:")
                    print(f"Careers: {(courses[9]["careers"])}")
                    print(" ")
                    print(
                        "It certainly is a wither... \n Your mortal self truly was a special one... \n So many possibilities...wasted")

                else:
                    print("Invalid input \n Enlightenment unsuccessful")

            elif num == "2":
                print("-" * 50)
                print("PRESS 1 FOR LARGE-SCALE ")
                print("PRESS 2 FOR HIGH-VALUE ")
                time.sleep(2)
                num = input("large-scale or high-value planting?")
                if num == "1":
                    print("-" * 50)
                    print("the STEM aligned course you could have been in your premature mortal life would be..")  # aligned for a AGRICULTURE
                    print(courses[10]["specialty"])
                    print("You could have learned so much... \n Perhaps through these electives:")
                    print(f"Grade 11: {(courses[10]["grd11_subj"])}")
                    print(f"Grade 12: {(courses[10]["grd12_subj"])}")
                    print(f"You could have given back to society so much... \n There were opportunities a plenty:")
                    print(f"Careers: {(courses[10]["careers"])}")
                    print(" ")
                    print(
                        "It certainly is a wither... \n Your mortal self truly was a special one... \n So many possibilities...wasted")
                elif num == "2":
                    print("-" * 50)
                    print("the STEM aligned course you could have been in your premature mortal life would be..")  # aligned for a HORTICULTURE
                    print(courses[11]["specialty"])
                    print("You could have learned so much... \n Perhaps through these electives:")
                    print(f"Grade 11: {(courses[11]["grd11_subj"])}")
                    print(f"Grade 12: {(courses[11]["grd12_subj"])}")
                    print(f"You could have given back to society so much... \n There were opportunities a plenty:")
                    print(f"Careers: {(courses[11]["careers"])}")
                    print(" ")
                    print(
                        "It certainly is a wither... \n Your mortal self truly was a special one... \n So many possibilities...wasted")

                else:
                    print("Invalid input \n Enlightenment unsuccessful")

            else:
                print("Invalid input \n Enlightenment unsuccessful")

        elif num =="2":
            print("-" * 50)
            print("PRESS 1 FOR THEORETICAL ")
            print("PRESS 2 FOR APPLIED ")
            time.sleep(2)
            num = input("theoretical investigation or applied knowledge?")
            if num == "1":
                print("-" * 50)
                print("the STEM aligned course you could have been in your premature mortal life would be..")  # aligned for a THEORETICAL RESEARCHER
                print(courses[12]["specialty"])
                print("You could have learned so much... \n Perhaps through these electives:")
                print(f"Grade 11: {(courses[12]["grd11_subj"])}")
                print(f"Grade 12: {(courses[12]["grd12_subj"])}")
                print(f"You could have given back to society so much... \n There were opportunities a plenty:")
                print(f"Careers: {(courses[12]["careers"])}")
                print(" ")
                print("It certainly is a wither... \n Your mortal self truly was a special one... \n So many possibilities...wasted")
            elif num == "2":
                print("-" * 50)
                print("the STEM aligned course you could have been in your premature mortal life would be..")  # aligned for a APPLIED SCIENTIST
                print(courses[13]["specialty"])
                print("You could have learned so much... \n Perhaps through these electives:")
                print(f"Grade 11: {(courses[13]["grd11_subj"])}")
                print(f"Grade 12: {(courses[13]["grd12_subj"])}")
                print(f"You could have given back to society so much... \n There were opportunities a plenty:")
                print(f"Careers: {(courses[13]["careers"])}")
                print(" ")
                print("It certainly is a wither... \n Your mortal self truly was a special one... \n So many possibilities...wasted")

            else:
                print("Invalid input \n Enlightenment unsuccessful")

        else:
            print("Invalid input \n Enlightenment unsuccessful")

    else:
        print("Invalid input \n Enlightenment unsuccessful")







def background(name):  # settings function
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
    print("which of the ■■■'s rays shall i shine upon you?") # direction for each input number
    print("the wake of DAWN (1)")
    print("the bask of NOON (2)")
    print("the last of DUSK (3)")
    time.sleep(1)
    print("")
    print(f"DAWN: is {name} really my name?") # name changer
    time.sleep(1)
    print(f"NOON: what put me in this mortal position?") # lore story (WIP)
    time.sleep(1)
    print(f"DUSK: how did i end up here?") # origin story (WIP)
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("STYGIAN: who are you?") # more lore (WIP) | consult nathan on this - tnx
    time.sleep(2)
    ray = input("go on..")
    if ray == "1":
        time.sleep(1)
        name_change = input("then shall you wish to change it then?")
        if name_change == "1":
            name = input("then by virtue of ■■■■, state your desired name: ")      # elif == 2 is within nathan's email, pls refer to him for direction - tnx
            print(f"welcome to the fork again, {name}.")

    elif ray == "2":
        print("...")
        time.sleep(1)
        print("You have had quite the reputation in your lifespan \n Though ■■■■ did not reveal such to be a positive or negative reputation...")
        print("Most just go straight to purgatory...but some sneaky souls go through enough for this kind of reading")
        print("Unfortunately, to find just this knowledge out was an unwise choice")
        print("You could have learned much more \n But of course I won't say what...")

    elif ray == "3":
        time.sleep(1)
        origin_change = input("shall you wish to generate your new origin story then?")
        print("PRESS 1 TO AGREE")
        print("PRESS 2 TO GO BACK")
        if origin_change == "1":
            rebirth = input("select from the options given by the order.")
            print("the archives can't hold infinite documentation of every source ■■■■■■.")
            print("OPTION 1. 'i'm just commuting to work. nothing much.")
            print("OPTION 2. 'just taking a walk along the avenue.")
            print("OPTION 3. 'i was reminded of my jog through the bus stop.")
            print("OPTION ■. 'i was given the opportunity to ■■■■■■ by the ■■■■■■■.")
            if rebirth == "1":
                time.sleep(1)
                print("Admirable...your willingness to work everyday. Very well, this day consisted of a commute to work...")
            elif rebirth == "2":
                time.sleep(1)
                print("I have heard walks are peaceful...you were a peaceful person then\nInteresting...")
            elif rebirth == "3":
                time.sleep(1)
                print("Exercise makes a person well-rounded, they say\nYou truly are interesting...")
            elif rebirth == "4":
                print("--error--")
            else:
                print("Origin story generation unsuccessful")
    else:
        print("Invalid input \n Reminiscence unsuccessful")



def end():
    print("I do not usually encounter people like you \nWho refuse a reading")
    print(f"Very well...en route to purgatory in 3...")
    time.sleep(2)
    print("...")
    print("Oh? We may have gotten an alert...")
    print("The negative effects of humanity are severe, as you may know")
    print("■■■■■■ believes it necessary to purge purgatory \nForgiveness hath been fortaken")
    print("One question shall be to decide for you Eternal Paradise or Eternal Conscious Suffering")
    time.sleep(2)
    print("Dear user, as a respectable person of STEM...\nIs science an infinite source of knowledge, a life's journey, a mere tool for phenomena, or life itself?")
    print("1. Infinite source knowledge")
    print("2. Life's journey")
    print("3. Tool for phenomena")
    print("4. Understanding of the world")
    print("5. No answer")
    final_fate = input("For the final time...go on")
    if final_fate == "1" or final_fate == "2" or final_fate == "3" or final_fate == "4":
        time.sleep(2)
        print("It is surprising that I say I am relieved")
        time.sleep(1)
        print("The answer would actually be all of the above with the exception of number 5 \n Science in itself is unexplainable, but as a person of STEM, \n Having an answer is already science \n Whether that be an educate guess or analytical decision \n ")
        print("your fate shall be...")
        time.sleep(2)
        print("The eternal blessing of the pursuit of knowledge in everything STEM")
        print("Being human may have ended for you, but your intellectual journey shall not. ")
    elif final_fate == "5":
        print("You dare to call yourself a person of STEM? \n How science ends is with a proper conclusion \n Conclusions are interpretations, and if you have none...\n there is no place for you \n In the eternal pursuit of knowledge")
    else:
        print("No answer...something ■■■■■■ truly despises")
        print("My command is to leave you to wallow in the eternal knowledge \n of sacrificing your final fate.")
import json  # the list of dictionaries that'll be transposed into a separate json file later on | to be coordinated with venize for more info - tnx

courses = [
	{ 
    "specialty": "Computer Science",
    "person": "Computer Scientist",
    "grd11_subj": ["Mathematics 6 (Core Subject)", "Computer Science elective", "Technology elective"],
    "grd12_subj": ["Mathematics 7 (Core Subject)", "Computer Science elective", "Technology elective"],
    "careers": ["Software Developer/Engineer", "Web Developer", "Cybersecurity Analyst", "Data Scientist/Engineer"]
    }, 
    {
    "specialty": "Robotics",
    "person": "Robotics Specialist",
    "grd11_subj": ["Mathematics 6 (Core Subject)", "Physics Science Specialization (Level 1 or 2)", "Computer Science elective", "Technology elective", "DTech elective"],
    "grd12_subj": ["Mathematics 7 (Core Subject)", "Physics Science Specialization (Level 1 or 2)", "Computer Science elective", "Technology elective", "DTech elective"],
    "careers": ["Robotics Engineer", "Robot Developer", "Data Scientist/Engineer"]
    }, 
    {
    "specialty": "Engineering",
    "person": "Engineer",
    "grd11_subj": ["Mathematics 6 (Core Subject)", "Physics Science Specialization (Level 1 or 2)", "Chemistry Science Specialization (Level 1 or 2) - For Chemical Engineering", "Engineering Science elective", "Technology elective", "DTech elective"],
    "grd12_subj": ["Mathematics 7 (Core Subject)", "Physics Science Specialization (Level 1 or 2)", "Chemistry Science Specialization (Level 1 or 2) - For Chemical Engineering", "Engineering Science elective", "Technology elective", "Mathematics 8 elective"],
    "careers": ["Mechanical Engineer (Recommended for Physics Core)", "Chemical Engineer  (Recommended for Chemistry Core)", "Electrical Engineer (Recommended for Technology elective)", "Civil Engineer (Recommended for DTech elective)", "Environmental engineer (Recommended for Biophysics Core)"]
    }, 
    {
    "specialty": "Environmental Science",
    "person": "Environmental Scientist",
    "grd11_subj": ["Biology Science Specialization (Level 1 or 2)", "Agriculture elective", "Technology elective", "Research 1 (Focus on environmental issues)"],
    "grd12_subj": ["Biology Science Specialization (Level 1 or 2)", "Agriculture elective", "Technology elective", "Engineering Science elective", "Research 2 (Focus on environmental issues)"],
    "careers": ["Environmental Planner", "Environmental Engineer (Recommended for Engineering Science elective)", "Environmental Researcher"]
    }, 
    {
    "specialty": "Physics",
    "person": "Physicist",
    "grd11_subj": ["Physics Science Specialization (Level 1 or 2)", "Engineering Science elective", "Research 1 (Focus on issues related to physics)"],
    "grd12_subj": ["Physics Science Specialization (Level 1 or 2)", "Engineering Science elective", "Mathematics 8 elective", "Research 2 (Focus on issues related to physics)"],
    "careers": ["Engineer", "Astrophysicist", "Medical Physicist", "Research Scientist (Physics Specialty)", "Educator for Physics-Related Subjects (Also Requires Education Degree)"]
    },
    {
    "specialty": "Chemistry",
    "person": "Chemist",
    "grd11_subj": ["Chemistry Science Specialization (Level 1 or 2)", "Engineering Science elective", "Research 1 (Focus on issues related to chemistry)"],
    "grd12_subj": ["Chemistry Science Specialization (Level 1 or 2)", "Engineering Science elective", "Research 2 (Focus on issues related to chemistry)"],
    "careers": ["General Chemist", "Forensic Scientist", "Chemistry Lab Technician", "Chemical Engineer", "Research Scientist (Chemistry Specialty)", "Organic Chemist", "Environmental Chemist", "Educator for Chemistry-Related Subjects (Also Requires Education Degree)"]
    },
    {
    "specialty": "Biology",
    "person": "Biologist",
    "grd11_subj": ["Biology Science Specialization (Level 1 or 2)", "Research 1 (Focus on issues related to biology)"],
    "grd12_subj": ["Biology Science Specialization (Level 1 or 2)", "Research 2 (Focus on issues related to biology)"],
    "careers": ["General Biologist", "Pathologist", "Biomedical Engineer", "Research Scientist (Biology Specialty)", "Field Biologist", "Environmental Engineer", "Educator for Biology-Related Subjects (Also Requires Education Degree)"]
    },
    {
    "specialty": "Mathematics",
    "person": "Mathematician",
    "grd11_subj": ["Mathematics 6 (Core Subject)", "Physics Science Specialization (Level 1 or 2)", "Engineering Science elective", "Computer Science elective"],
    "grd12_subj": ["Mathematics 7 (Core Subject)", "Physics Science Specialization (Level 1 or 2)", "Engineering Science elective", "Computer Science elective", "Mathematics 8 elective"],
    "careers": ["Data Scientist", "Aerospace Engineer", "Civil Engineer", "Physicist (Recommended for Physics Core)", "Researcher & Analyst", "Educator for Mathematics (Also Requires Education Degree)"]
    },
	{
    "specialty": "Data Curation",
    "person": "Data Curator",
	"grd11_subj": ["Mathematics 6 (Core Subject)", "Computer Science elective"],
    "grd12_subj": ["Mathematics 7 (Core Subject)", "Computer Science elective", "Mathematics 8 elective"],
	"careers": ["AI/Machine Programmer", "Analytical Data Curator", "Code Proofreader", "Medical Data Manager", "Digital Content Manager"]
    },
    {
    "specialty": "Database Administration",
    "person": "Database Administrator",
    "grd11_subj": ["Mathematics 6 (Core Subject)", "Engineering elective", "Computer Science elective"],
    "grd12_subj": ["Mathematics 7 (Core Subject)", "Engineering elective", "Computer Science elective", "Mathematics 8 elective"],
    "careers": ["Database Manager", "Cloud Manager", "Database Security and Maintenance"]
    },
    {
    "specialty": "Horticulture",
    "person": "Horticulturist",
    "grd11_subj": ["Biology Science Specialization (Level 1 or 2)", "Agriculture elective"],
    "grd12_subj": ["Biology Science Specialization (Level 1 or 2)", "Agriculture elective"],
    "careers": ["Greenhouse Manager", "Farm Technician", "Crop Production Specialist", "Research Horticulturist"]
    },
    {
    "specialty": "Agriculture",
    "person": "Agriculturist",
    "grd11_subj": ["Biology Science Specialization (Level 1 or 2)", "Agriculture elective", "Climate Science elective"],
    "grd12_subj": ["Biology Science Specialization (Level 1 or 2)", "Agriculture elective", "Climate Science elective"],
    "careers": ["Field Agronomist", "Plant Doctor", "Farm Technician", "Zoology Researcher", "Botany Researcher"]
    },
    {
    "specialty": "Theoretical Research",
    "person": "Theoretical Researcher",
    "grd11_subj": ["Research 1", "English 5 (Core Subject) - For Oral and Written Communication"],
    "grd12_subj": ["Research 2", "English 6 (Core Subject) - For Science Communication"],
    "careers": ["General Scientific Theorist", "Theoretical Physicist", "Theoretical Chemist", "Quantum Researcher", "Quantitative Analyst", "Theoretical Scientific Framework Professor"]
    },
    {
    "specialty": "Applied Science",
    "person": "Applied Scientist",
    "grd11_subj": ["Research 1", "Engineering elective", "Any Science Subject of your interest with laboratory activities"],
    "grd12_subj": ["Research 2", "Engineering elective", "Any Science Subject of your interest with laboratory activities"],
    "careers": ["Applied AI Researcher", "Biomedical Engineer", "Experimental Physicist ", "Aerospace Engineer", "Agricultural Scientist"]
    },
]


try: 
       filename = "courses.json"
    
       with open(filename, 'w') as file:
        json.dump(courses, file, indent=4)    # to be used for the later json transfer

        # error handling
except FileNotFoundError:
    print("Error: The file 'data.json' was not found.")
except json.JSONDecodeError as e:
    print(f"Failed to decode JSON: {e}")



                        #yoyoyoyoyoyo (comment test for update across device(67))
                        # test comment
if __name__ == "__main__": # safeguard for the forks mentioned earlier (the functions)

    intro()







