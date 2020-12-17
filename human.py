#! /usr/bin/env python
__author__ = "Hunter Fagan"

from datetime import datetime
class Human(object):
    def __init__(self, height, weight, name, hairColor= 'none', eyeColor= 'none'):
        self.name = name
        self.height = height
        self.weight = weight
        self.hairColor = hairColor
        self.eyeColor = eyeColor
        self.phraseList = []
        self.dateOfBirth = datetime.date(datetime.now())
        self.age = datetime.date(datetime.now()) - self.dateOfBirth
    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name
    def getHeight(self):
        return self.height
    def setHeight(self, height):
        self.height = height
    def getWeight(self):
        return self.weight
    def setWeight(self, weight):
        self.weight = weight
    def getHairColor(self):
        return self.hairColor
    def setHairColor(self, hairColor):
        if hairColor != 'blonde' and hairColor != 'brunette' and hairColor != 'red' and hairColor != 'black' and hairColor != 'none':
            raise ValueError('Cannot set hair color.')
        else:
            self.hairColor = hairColor
    def getEyeColor(self):
        return self.eyeColor
    def setEyeColor(self, eyeColor):
        if eyeColor != 'brown' and eyeColor != 'blue' and eyeColor != 'green' and eyeColor != 'hazel' and eyeColor != 'none':
            raise ValueError('Cannot set eye color.')
        else:
            self.eyeColor = eyeColor
    def getDateOfBirth(self):
        return self.dateOfBirth
    def setDateOfBirth(self, dateOfBirth):
        self.dateOfBirth = dateOfBirth
    def getAge(self):
        return self.age
    def speak(self, phrase):
        self.phraseList.append(phrase)
        print(phrase)
    def pastPhrases(self, numberOfSteps= 0):
        if numberOfSteps < 0:
            print('Not a valid number.')
        else:
            print(self.phraseList[len(self.phraseList) - numberOfSteps - 1])
class Person(Human):
    def __init__(self, height, weight, name, hairColor= 'none', eyeColor= 'none', gender='female', pregnant=False):
        Human.gender = gender
        Human.pregnant = pregnant
        Human.__init__(self, height, weight, name, hairColor= 'none', eyeColor= 'none')
    def getGender(Human):
        return Human.gender
    def setGender(Huamn, gender):
        Human.gender = gender
    def getPregnant(Human):
        return Human.pregnant
    def setPregnant(Huamn, pregnant):
        Human.pregnant = pregnant
    def isPregnant(pregnant):
        if pregnant != True:
            raise ValueError('Must be True or False.')
        else:
            return pregnant
class Student(Human):
        def __init__(self, height, weight, name, schoolAttended, subjectStudied, graduated, hairColor='none', eyeColor='none'):
            Human.schoolAttended = schoolAttended
            Human.subjectStudied = subjectStudied
            Human.graduated = graduated
            Human.__init__(self, height, weight, name, schoolAttended, subjectStudied, graduated)
        def getSchoolAttended(Human):
            return Human.schoolAttended
        def setSchoolAttended(Huamn, schoolAttended):
            Human.schoolAttended = schoolAttended
        def getSubjectStudied(Human):
            return Human.subjectStudied
        def setSubjectStudied(Huamn, subjectStudied):
            Human.subjectStudied = subjectStudied
        def getGraduated(Human):
            return Human.graduated
        def setGraduated(Huamn, graduated):
            Human.graduated = graduated

