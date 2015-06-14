# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define mc = Character("[Name]")


# The game starts here.
label start:
    python:
        #initial variables
        import datetime
        Name = renpy.input("What would you like your name to be?", default = "Richard Tweed")
        Name = Name.strip()
        currYear = renpy.input("What year would you like it to be?", default = datetime.date.today().year)
        currMonth = renpy.input("What month would you like it to be?", default = datetime.date.today().month)
        currDay = renpy.input("What day would you like to be?", default = datetime.date.today().day)
        currAge = renpy.input("What age would you like to be?", default = 14)
        currTime = datetime.time(8, 30)
        currDate = datetime.datetime(int(currYear),int(currMonth),int(currDay),currTime.hour,currTime.minute)
        graduated = False
        currGrade = int(currAge) -6
        birthYear = int(currYear) - int(currAge)
        currClass = ""
        Bio = ""
        historyWinterExamScore = -1
        mathWinterExamScore = -1
        scienceWinterExamScore = -1
        historyGradesList = []
        mathGradesList = []
        scienceGradesList = []
        #condition variables
        takenFinalExams = False
        takenWinterExams = False
        historyClassDone = False
        mathClassDone = False
        scienceClassDone = False
        dayDone = False
        #fundamental skills
        intelligence = renpy.random.randint(0,101)
        strength = renpy.random.randint(0,101)
        #knowledge skills
        knowledgeOfHistory = renpy.random.randint(0,101)
        knowledgeOfMath = renpy.random.randint(0,101)
        knowledgeOfScience = renpy.random.randint(0,101)
        if currGrade < 0:
            preSchool = True
        elif currGrade < 6:
            elemenSchool = True
        elif currGrade < 9:
            midSchool = True
        elif currGrade < 13:
            highSchool = True
        elif currGrade < 17:
            uni = True
        else:
            realLife = True
        
    "What is your gender?"
    menu:
        "Male":
           $ gender = "Male"
        "Female":
           $ gender = "Female"
        "Non-Binary/Other":
           $ gender = "Other"
    call main_screen_label
    return
