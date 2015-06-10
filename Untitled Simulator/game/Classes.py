import random
import datetime

graduated = False
        
class Person:
    def __init__(self,someFirstName,someLastName, someCurrAge,someGender,someBirthYear):
        self.firstName = someFirstName
        self.lastName = someLastName
        self.intelligence = random.randint(0,101)
        self.strength = random.randint(0,101)
        self.age = someCurrAge
        self.grade = int(self.age) - 6
        self.birthYear = someBirthYear
        self.gender = someGender
    
    def getFirstName(self):
        return self.firstName
    
    def getLastName(self):
        return self.lastName
                
    def getIntelligence(self):
        return self.intelligence
    
    def getStrength(self):
        return self.strength
        
    def getAge(self):
        return self.age
    
    def getGrade(self):
        return self.grade
    
    def getBirthYear(self):
        return self.birthYear
    
    def getGender(self):
        return self.gender
    
    def getBio(self):
        return Bio
    
    def creatingBio(self):
         Bio = ""
         if self.age > 0:
             Bio = Bio + str(self.firstName) + " was born in " + str(self.birthYear) + ". "
         else:
             Bio = Bio + str(self.firstName) + " will be born in " + str(self.birthYear) + ". "
         if self.gender == "Male":
             Bio = Bio + "He is " + str(self.age) + " years old. "
             if graduated == False:
                 Bio = Bio + "He is in " + str(self.grade) + "th Grade. "
         elif self.gender == "Female":
             Bio = Bio + "She is " + str(self.age) + " years old. "
             if graduated == False:
                 Bio = Bio + "She is in " + str(self.grade) + "th Grade. "
         elif self.gender == "Other":
             Bio = Bio + "They are " + str(self.age) + " years old. "
             if graduated == false:
                 Bio = Bio + "They are in " + str(self.grade) + "th Grade. "
         return Bio
    
class schoolClass:
    def __init__(self,someName,someNumberGrade):
        self.name = someName
        self.grade = someNumberGrade
        self.maxsize = random.randint(15,25)
        self.testGrades = []
        self.finalGrade = None
                
    def getName(self):
        return self.name
                
    def getGrade(self):
        return self.grade
                
    def getMaxsize(self):
        return self.maxsize
                
    def getTestGrades(self):
        return self.testGrades
                
    def setMaxsize(self,newMaxsize):
        self.maxsize = newMaxsize
                
    def takeExam(self,person):
        examGrade = person.getIntelligence() * random.random()
        self.testGrades.append(examGrade)
        return examGrade
                
    def calculateFinalGrade(self):
        totalGrade = 0
        for item in self.testGrades:
            totalGrade = totalGrade + item
        finalGrade = totalGrade / length(self.testGrades)
        return finalGrade