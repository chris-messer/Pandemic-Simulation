import numpy as np


class Classroom():
    def __init__(self, students:list, sim_length):
        self.number_of_students = number_of_students
        self.sim_length = sim_length




class Student():
    def __init__(self, Vs, Ve):
        self.Vs = Vs
        self.Ve = Ve
        self.infected = False
        self.days_infected = 0
        self.vaccinated = 1 if np.random.uniform(0, 1) <= self.Vs else 0
        self.immunity = True

    def _go_to_class(self, exposure):
        P_i = exposure * (1-(self.vaccinated*self.Ve))



if __name__ == '__main__':
    c = Classroom(number_of_students=31, sim_length=100, Vs=100, Ve=100)
