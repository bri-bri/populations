from random import random

from models.human import Human
from models.female import Female
import constants


class Population(object):

    people = []

    def __init__(self, pop_count=20):
        count = 0
        while count < pop_count:
            person = Human() if count % 2 == 0 else Female()
            person.age = constants.start_age
            self.people.append(person)
            count += 1

    def agePopulation(self):
        map(lambda p: p.increaseAge(), self.people)
        self.buryDead()

    def buryDead(self):
        for person in self.people:
            if not person.isAlive():
                self.people.remove(person)

    def createBaby(self):
        return Female() if random() <= constants.percent_female else Human()

    def countByGender(self, gender):
        return reduce(lambda x, y: x + 1 if y.gender == gender else x, self.people, 0)

    def countPopulation(self):
        return len(self.people)

    def haveBabies(self):
        for person in self.people:
            if person.gender == "F":
                if person.haveBaby():
                    self.people.append(self.createBaby())

    def step(self):
        self.haveBabies()
        self.agePopulation()

