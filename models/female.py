from random import random

from models.human import Human
import constants


class Female(Human):

    pregnant = False
    postpartum = False

    def __init__(self):
        super(Female, self).__init__()
        self.gender = "F"

    def updatePregnancy(self):
        if self.alive:
            if self.fertile and self.age >= constants.fertility_start_age and self.age < constants.fertility_end_age:
                self.postpartum = self.pregnant
                self.pregnant = not self.postpartum

    def haveBaby(self):
        had_baby = self.pregnant
        if had_baby:
            had_baby = True if (random() < constants.infant_mortality_rate * constants.miscarriage_rate) else False
            self.alive = True if (random() < constants.maternal_mortality_rate) else False
        self.updatePregnancy()
        return had_baby




