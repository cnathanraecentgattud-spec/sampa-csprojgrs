


import time # for timed outputs
def intro():
	print(r"""     
              /||||||||||||\         /|||||||||||||||||||\     |||||||||||||||||\       /||||||||||||\          /||||||||||||\          /||||||||\         /\        /|||||||\   /|||||\  /|||||\   /|||||||\                       /||||||||||||||||||\    |||||||||||||||||||  ||||||||||||||||||\   |||||  /||||||||||||||||||\    ||||||||||||||||||||||||||   |||||     |||||                                                                                       
             /||||||||||||||\        |||||||||||||||||||||     ||||||||||||||||||       ||||||||||||||\        /||||||||||||||        /||||/   \||/       /||\       |||   |||   ||       ||        |||   |||                       |||||||||||||||||||||   |||||||||||||||||||  ||||||||||||||||||||  |||||  |||||||||||||||||||||   ||||||||||||||||||||||||||   |||||     |||||                                                                                                                
            /|||||||||||||||||\      |||||||||||||||||||||     ||||            \|       |||||||||||||||\      /|||||||||||||||        |||||              /|/\|\      ||||||||/   |||||    |||||     ||||||||/                       ||||||/        \|||||   ||||||               ||||||/      \||||||  |||||  ||||||/        \|||||   ||||||||||||||||||||||||||   |||||     |||||                                                                                  
            |||||||||||||||||||\     |/   |||||||||||   \|     ||||                     ||||||||||||||||\    /||||||||||||||||        \||||\   /||\     /||||||\     ||   \\\    ||       ||        ||   \\\                        ||||||          |||||   ||||||               ||||||        ||||||  |||||  ||||||          |||||            ||||||||            |||||     |||||                                                                                 
             \|||||||/        |/          |||||||||||          ||||                     |||||||||||||||||\__/|||||||||||||||||          \||||||||/     ///    \\\    ||    \\\   ||||||/  ||||||/   ||    \\\                       ||||||\        /|||||   ||||||               ||||||        ||||||  |||||  ||||||\        /|||||            ||||||||            |||||     |||||                                                                         
               \|||||\                    |||||||||||          ||||    //|              ||||||||||||||||||||||||||||||||||||||                                                                                          __________  |||||||||||||||||||||   ||||||               ||||||\      /|||||/  |||||  |||||||||||||||||||||            ||||||||            |||||     |||||                                                                                  
                \|||||\                   |||||||||||          |||||||||||              ||||||||||||/|||||||||||\|||||||||||||        ---------------------------------------------------------------------------       __________  ||||||||||||||||||||/   ||||||||||||||       |||||||||||||||||/    |||||  ||||||||||||||||||||/            ||||||||            |||||||||||||||                                                                                                 
                 \||||||\                 |||||||||||          ||||    \|               |||||||||||/  \|||||||/  \||||||||||||                                                                                          __________  |||||||/ \\\\\\\        ||||||               |||||||||||||||||\    |||||  |||||||/ \\\\\\\                 ||||||||            |||||     |||||                                                                                                    
                /|||||||||\               |||||||||||          ||||                     |||||||||||    \|||||/    ||||||||||||            /||||||\  \||/     /||||||||\    ||    ///  /|||||\   /|||||||\                           |||||||   \\\\\\\       ||||||               ||||||/      \||||\   |||||  |||||||   \\\\\\\                ||||||||            |||||     |||||                                                                      
         |\    /||||||||||||              |||||||||||          ||||                     |||||||||||     \|||/     ||||||||||||            |||  |||   ||    /||||/   \||/   ||\  ///   ||        |||   |||                           |||||||    \\\\\\\      ||||||               ||||||        ||||||  |||||  |||||||    \\\\\\\               ||||||||            |||||     |||||                                                                                                   
         \||||||||||||||||||              |||||||||||          ||||           /|        |||||||||||      \/       ||||||||||||            |||||||/   ||    |||||           |||||||    |||||     ||||||||/                           |||||||     \\\\\\\     ||||||               ||||||        ||||||  |||||  |||||||     \\\\\\\              ||||||||            |||||     |||||                                                                                           
          \|||||||||||||||/              /|||||||||||\         |||||||||||||||||        |||||||||||               ||||||||||||            ||         ||    \||||\   /||\   |||  \\\   ||        ||   \\\                            |||||||      \\\\\\\    |||||||||||||||||||  ||||||\      /||||||  |||||  |||||||      \\\\\\\             ||||||||            |||||     |||||                                                                                    
           \|||||||||||||/     O        |||||||||||||||   O    ||||||||||||||||/   o    |||||||||||               ||||||||||||  O         ||        /||\     \||||||||/    |||   \\\  ||||||/   ||    \\\                           |||||||       \\\\\\\   |||||||||||||||||||  |||||||||||||||||||/  |||||  |||||||       \\\\\\\            ||||||||            |||||     |||||          
        """)

main_intro = intro()
print(main_intro)

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
        background(name)    # main fork to the three options
elif choice == "3":
        end()


def game():
    print("a free reading i see..")
    print("the divination of ■■■■ tells me to get to know you a bit more.")
    print("-"*50)   # separator for readability
    print("PRESS 1 TO AGREE")
    print("PRESS 2 TO DISAGREE")   # constant directory to prevent any losses due to not knowing controls
    num = input("do you enjoy he process of problem solving?")
    if num == "1":
        print("PRESS 1 FOR FIRST OPTION")
        print("PRESS 2 FOR SECOND OPTION")
        num = input("problem solving through creating or thinking?")
        if num == "1":
            print("PRESS 1 FOR FIRST OPTION")
            print("PRESS 2 FOR SECOND OPTION")
            num = input("rather coding or building?")
            if num == "1":
                print("the STEM aligned course you could have been in your premature mortal life would be..")
                print(courses[0]["specialty"]) # result of test based on the list of dictionaries at the bottom
            else:
                print("PRESS 1 FOR FIRST OPTION")
                print("PRESS 2 FOR SECOND OPTION")
                num = input("a specific or general field?")
                if num == "1":
                    print("the STEM aligned course you could have been in your premature mortal life would be..")
                    print(courses[1]["specialty"])
                else:
                    print("the STEM aligned course you could have been in your premature mortal life would be..")
                    print(courses[2]["specialty"])
        else:
            print("PRESS 1 FOR FIRST OPTION")
            print("PRESS 2 FOR SECOND OPTION")
            num = input("working with nature or with numbers?")
            if num == "1":
                print("PRESS 1 FOR FIRST OPTION")
                print("PRESS 2 FOR SECOND OPTION")
                num = input("outside world, or in a laboratory?")
                if num == "1":
                    print("the STEM aligned course you could have been in your premature mortal life would be..")
                    print(courses[3]["specialty"])
                else:
                    print("the STEM aligned course you could have been in your premature mortal life would be..")
                    print(courses[6]["specialty"])
            else:
                print("PRESS 1 FOR FIRST OPTION")
                print("PRESS 2 FOR SECOND OPTION")
                print("do you en■■■ ■■ ■■■■■■■ ■■■ ■■■■■■")    # area to snap back to lore | as much as possible pls don't remove w/o direction from nathan - tnx
                time.sleep(2)
                print("...")
                time.sleep(1)
                print("sorry, the ■■■■■ malfunctioned.")
                num = input("do you prefer familiarization or active memorization and application?")
                if num == "1":
                    print("PRESS 1 TO AGREE")
                    print("PRESS 2 TO DISAGREE")
                    num = input("identifying structures or understanding & predicting?")
                    if num == "1":
                        print("the STEM aligned course you could have been in your premature mortal life would be..")
                        print(courses[7]["specialty"])
                    else:
                        print("the STEM aligned course you could have been in your premature mortal life would be..")
                        print(courses[4]["specialty"])
                else:
                    print("the STEM aligned course you could have been in your premature mortal life would be..")
                    print(courses[5]["specialty"])










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
    print(f"NOON: what put me in that mortal position?") # lore story (WIP)
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
    elif ray == "3":
        time.sleep(1)
        origin_change = input("shall you wish to generate your new origin story then?")
        print("PRESS 1 TO AGREE")
        print("PRESS 2 TO GO BACK")
        if origin_change == "1":
            rebirth = input("select from the options given by the order.")
            print("the archives can't hold infinite documentation of every source ■■■■■■.")
            print("OPTION A. 'i'm just commuting to work. nothing much.")
            print("OPTION B. 'just taking a walk along the avenue.")
            print("OPTION C. 'i was reminded of my jog through the bus stop.")
            print("OPTION ■. 'i was given the opportunity to ■■■■■ by the ■■■■■■■.")




def end():
    print("WIP")  # quitting mechanism (WIP)


import json  # the list of dictionaries that'll be transposed into a separate json file later on | to be coordinated with venize for more info - tnx

courses = [
	{ 
    "specialty": "Computer Science",
    "person": "Computer Scientist",
    "grd11_subj": ["Mathematics 5", "Computer Science elective", "Technology elective"],
    "grd12_subj": ["Mathematics 6", "Computer Science elective", "Technology elective"],
    "careers": ["Software Developer/Engineer", "Web Developer", "Cybersecurity Analyst", "Data Scientist/Engineer"]
    }, 
    {
    "specialty": "Robotics",
    "person": "Robotics Specialist",
    "grd11_subj": ["Mathematics 5", "Physics Core (Level 1 or 2)", "Computer Science elective", "Technology elective", "DTech elective"],
    "grd12_subj": ["Mathematics 5", "Physics Core (Level 1 or 2)", "Computer Science elective", "Technology elective", "DTech elective"],
    "careers": ["Robotics Engineer", "Robot Developer", "Data Scientist/Engineer"]
    }, 
    {
    "specialty": "Engineering",
    "person": "Engineer",
    "grd11_subj": ["Mathematics 5", "Physics Core (Level 1 or 2)", "Chemistry Core (Level 1 or 2) - For Chemical Engineering", "Engineering Science elective", "Technology elective", "DTech elective"],
    "grd12_subj": ["Mathematics 5", "Physics Core (Level 1 or 2)", "Chemistry Core (Level 1 or 2) - For Chemical Engineering", "Engineering Science elective", "Technology elective"],
    "careers": ["Mechanical Engineer (Recommended for Physics Core)", "Chemical Engineer  (Recommended for Chemistry Core)", "Electrical Engineer (Recommended for Technology elective)", "Civil Engineer (Recommended for DTech elective)", "Environmental engineer (Recommended for Biophysics Core)"]
    }, 
    {
    "specialty": "Environmental Science",
    "person": "Environmental Scientist",
    "grd11_subj": ["Biology Core (Level 1 or 2)", "Agriculture elective", "Technology elective", "Research 2 (Focus on environmental issues)"],
    "grd12_subj": ["Biology Core (Level 1 or 2)", "Agriculture elective", "Technology elective", "Engineering Science elective", "Research 3 (Focus on environmental issues)"],
    "careers": ["Environmental Planner", "Environmental Engineer (Recommended for Engineering Science elective)", "Environmental Researcher"]
    }, 
    {
    "specialty": "Physics",
    "person": "Physicicst",
    "grd11_subj": ["Physics Core (Level 1 or 2)", "Engineering Science elective", "Research 2 (Focus on issues related to physics)"],
    "grd12_subj": ["Physics Core (Level 1 or 2)", "Engineering Science elective", "Research 3 (Focus on issues related to physics)"],
    "careers": ["Engineer", "Astrophysicist", "Medical Physicist", "Research Scientist (Physics Specialty)", "Educator for Physics-Related Subjects (Also Requires Education Degree)"]
    },
    {
    "specialty": "Chemistry",
    "person": "Chemist",
    "grd11_subj": ["Chemistry Core (Level 1 or 2)", "Engineering Science elective", "Research 2 (Focus on issues related to chemistry)"],
    "grd12_subj": ["Chemistry Core (Level 1 or 2)", "Engineering Science elective", "Research 3 (Focus on issues related to chemistry)"],
    "careers": ["General Chemist", "Forensic Scientist", "Chemistry Lab Techniciant", "Chemical Engineer", "Research Scientist (Chemistry Specialty)", "Organic Chemist", "Environmental Chemist", "Educator for Chemistry-Related Subjects (Also Requires Education Degree)"]
    },
    {
    "specialty": "Biology",
    "person": "Biologist",
    "grd11_subj": ["Biology Core (Level 1 or 2)", "Research 2 (Focus on issues related to biology)"],
    "grd12_subj": ["Biology Core (Level 1 or 2)", "Research 3 (Focus on issues related to biology)"],
    "careers": ["General Biologist", "Pathologist", "Biomedical Engineer", "Research Scientist (Biology Specialty)", "Field Biologist", "Environmental Engineer", "Educator for Biology-Related Subjects (Also Requires Education Degree)"]
    },
    {
    "specialty": "Mathematics",
    "person": "Mathematician",
    "grd11_subj": ["Mathematics 5", "Physics Core (Level 1 or 2)", "Engineering Science elective", "Computer Science elective"],
    "grd12_subj": ["Mathematics 6", "Physics Core (Level 1 or 2)", "Engineering Science elective", "Computer Science elective"],
    "careers": ["Data Scientist", "Aerospace Engineer", "Civil Engineer", "Physicist (Recommended for Physics Core)", "Researcher & Analyst", "Educator for Mathematics (Also Requires Education Degree)"]
    }
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







