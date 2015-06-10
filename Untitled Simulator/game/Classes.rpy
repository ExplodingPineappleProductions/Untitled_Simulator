init:
    python:
        import random
        
        class Person:
            def __init__(self,someName):
                self.name = person
                self.intelligence = random.randint(0,101)
                self.strength = random.randint(0,101)
                
            def getIntelligence(self):
                return self.intelligence
        
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