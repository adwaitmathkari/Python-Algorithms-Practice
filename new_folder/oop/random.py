class Person:
    people_on_moon = 20
    def __init__(self, name):
        self.name = name
    @staticmethod
    def addToPeopleOnMoon(n):
        Person.people_on_moon+=n
    
    @staticmethod
    def getPeopleOnMoon():
        print(Person.people_on_moon, " is the no of people that have been on moon")

