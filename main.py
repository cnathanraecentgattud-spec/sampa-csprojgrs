["1. "]


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
    print("This game will try its best to determine a stable STEM job for you \n based on your experiences and opinions on things.")
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
    print("WIP")


import json

courses = [
	{ 
    "specialty": "Computer Science",
    "person": “Computer Scientist”,
    "grd11_subj": [“Mathematics 5”, “Computer Science elective”, “Technology elective”]
    "grd12_subj": [“Mathematics 6”, “Computer Science elective”, “Technology elective”]
    "careers": [“Software Developer/Engineer”, “Web Developer”, Cybersecurity Analyst”, “Data Scientist/Engineer”]
    }, 
    {
    "specialty": "Robotics",
    "person": “Robotics Specialist”,
    "grd11_subj": [“Mathematics 5”, “Physics Core (Level 1 or 2)”, “Computer Science elective”, “Technology elective”, “DTech elective”]
    "grd12_subj": [“Mathematics 5”, “Physics Core (Level 1 or 2)”, “Computer Science elective”, “Technology elective”, “DTech elective”]
    "careers": [“Robotics Engineer”, “Robot Developer”, “Data Scientist/Engineer”]
    }, 
    {
    "specialty": "Engineering",
    "person": “Engineer”,
    "grd11_subj": [“Mathematics 5”, “Physics Core (Level 1 or 2)”, “Chemistry Core (Level 1 or 2) - For Chemical Engineering”, “Biophysics Core (Level 1 or 2) - For Biomedical/Environmental Engineering”, “Engineering Science elective”, “Technology elective”, “DTech elective”]
    "grd12_subj": [“Mathematics 5”, “Physics Core (Level 1 or 2)”, “Chemistry Core (Level 1 or 2) - For Chemical Engineering”, “Biophysics Core (Level 1 or 2) - For Biomedical/Environmental Engineering”, “Engineering Science elective”, “Technology elective”]
    "careers": [“Mechanical Engineer (Recommended for Physics Core)”, “Chemical Engineer  (Recommended for Chemistry Core)”, “Electrical Engineer (Recommended for Technology elective)”, “Civil Engineer (Recommended for DTech elective)”, “Environmental engineer (Recommended for Biophysics Core)”]
    }, 
    {
    "specialty": "Environmental Science",
    "person": “Environmental Scientist”,
    "grd11_subj": [“Biology Core (Level 1 or 2)”, “BioChemistry Core (Level 1 or 2)”, “Agriculture elective”, “Technology elective”, “Research 2 (Focus on environmental issues)”]
    "grd12_subj": [“Biology Core (Level 1 or 2)”, “Biochemistry Core (Level 1 or 2)”, “Agriculture elective”, “Technology elective”, “Engineering Science elective”, “Research 3 (Focus on environmental issues)”]
    "careers": [“Environmental Planner”, “Environmental Engineer (Recommended for Engineering Science elective)”, “Environmental Researcher”]
    }, 
    {
    "specialty": "Physics",
    "person": “Physicicst”,
    "grd11_subj": [“Physics Core (Level 1 or 2)”, “BioPhysics Core (Level 1 or 2)”, “ChemPhysics Core (Level 1 or 2)”, “Engineering Science elective”, “Research 2 (Focus on issues related to physics)”]
    "grd12_subj": [“Physics Core (Level 1 or 2)”, “BioPhysics Core (Level 1 or 2)”, “ChemPhysics Core (Level 1 or 2)”, “Engineering Science elective”, “Research 3 (Focus on issues related to physics)”]
    "careers": [“Engineer”, “Astrophysicist”, “Medical Physicist”, “Research Scientist (Physics Specialty)”, “Educator for Physics-Related Subjects (Also Requires Education Degree)”]
    },
    {
    "specialty": "Chemistry",
    "person": “Chemist”,
    "grd11_subj": [“Chemistry Core (Level 1 or 2)”, “BioChem Core (Level 1 or 2)”, “ChemPhysics Core (Level 1 or 2)”, “Engineering Science elective”, “Research 2 (Focus on issues related to chemistry)”]
    "grd12_subj": [“Chemistry Core (Level 1 or 2)”, “BioChem Core (Level 1 or 2)”, “ChemPhysics Core (Level 1 or 2)”, “Engineering Science elective”, “Research 3 (Focus on issues related to chemistry)”]
    "careers": [“General Chemist”, “Forensic Scientist”, “Chemistry Lab Techniciant”, “Chemical Engineer”, “Research Scientist (Chemistry Specialty)”, “Organic Chemist”, “Environmental Chemist”, “Educator for Chemistry-Related Subjects (Also Requires Education Degree)”]
    },
    {
    "specialty": "Biology",
    "person": “Biologist”,
    "grd11_subj": [“Biology Core (Level 1 or 2)”, “BioChem Core (Level 1 or 2)”, “BioPhysics Core (Level 1 or 2)”, “Research 2 (Focus on issues related to biology)”]
    "grd12_subj": [“Biology Core (Level 1 or 2)”, “BioChem Core (Level 1 or 2)”, “BioPhysics Core (Level 1 or 2)”, “Research 3 (Focus on issues related to biology)”]
    "careers": [“General Biologist”, “Pathologist”, “Biomedical Engineer”, “Research Scientist (Biology Specialty)”, “Field Biologist”, “Environmental Engineer”, “Educator for Biology-Related Subjects (Also Requires Education Degree)”]
    },
    {
    "specialty": "Mathematics",
    "person": “Mathematician”,
    "grd11_subj": [“Mathematics 5”, “Physics Core (Level 1 or 2)”, “Engineering Science elective”, “Computer Science elective”]
    "grd12_subj": [“Mathematics 6”, “Physics Core (Level 1 or 2)”, “Engineering Science elective”, “Computer Science elective”]
    "careers": [“Data Scientist”, “Aerospace Engineer”, “Civil Engineer”, “Physicist (Recommended for Physics Core)””, “Researcher & Analyst”, “Educator for Mathematics (Also Requires Education Degree)”]
    }
]


try: 
       filename = "courses.json"
    
       with open(filename, 'w') as file:
        json.dump(courses, file, indent=4)



                        #yoyoyoyoyoyo (comment test for update across device(67))
                        # test comment
if __name__ == "__main__":

    intro()







