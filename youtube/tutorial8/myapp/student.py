from datetime import datetime


class Student:
    def __init__(self, name, dob, branch, credits, params):
        self.name = name
        self.dob = dob
        self.branch = branch
        self.credits = credits
        self.params = params

    def get_age(self):
        return (datetime.now() - self.dob).days // 365

    def add_credits(self, value):
        self.credits += value

    def get_credits(self):
        return self.credits


def is_eligible_for_degree(student):
    return student.get_credits() >= 20
