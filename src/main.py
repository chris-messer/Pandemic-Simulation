import numpy as np


class Classroom():
    def __init__(self, students, sim_length):
        self.students = students
        self.sim_length = sim_length




class Student():
    def __init__(self, P_v, P_ve, P_m, P_me, infectiousness):
        self.P_m = P_m
        self.P_me = P_me
        self.P_v = P_v
        self.P_ve = P_ve

        self.vaccinated = 1 if np.random.uniform(0, 1) <= self.P_v else 0
        self.masked = 1 if np.random.uniform(0, 1) <= self.P_m else 0
        self.P_io = 0

        self.previously_infected = True
        self.contagious = False
        self.infectiousness = infectiousness
        self.days_infected = 0


    def _go_to_class(self, exposure):
        if self.previously_infected == False:
            P_i = exposure * (1-(self.vaccinated*self.P_ve))
            if np.random.uniform(0, 1) <= P_i:
                self._infect()

        if self.previously_infected and self.days_infected <= 3:
            self.days_infected += 1
            if self.days_infected == 3:
                self.contagious = False
                self.P_io = 0


    def _infect(self):
        self.previously_infected = True
        self.contagious = True
        self.P_io = infectiousness * (1-(self.masked*self.P_me))





if __name__ == '__main__':
    number_of_students = 31

    vaccinated_percentage = .5
    vaccine_efficiency = .8
    masked_percentage = .5
    infectiousness = .2
    Students = [Student(vaccinated_percentage,
                        vaccine_efficiency,
                        masked_percentage,
                        infectiousness)
                for i in range(number_of_students)]

    c = Classroom(Students, sim_length=100)
