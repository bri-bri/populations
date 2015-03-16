from random import random

import constants


class Human(object):
    gender = "M"
    age = 0
    fertile = True
    alive = True

    def __init__(self):
        self.fertile = True if (random() < constants.infertility_factor) else False

    def increaseAge(self):
        if self.alive:
            self.age += 1
            self.checkMortality()

    def isAlive(self):
        return self.alive

    def checkMortality(self):
        if self.alive:
            self.alive = True if self.age <= constants.life_expectancy else False



