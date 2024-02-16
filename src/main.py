import numpy as np
import pandas as pd
import math


class Classroom():
    def __init__(self, students, sim_length, trial):
        self.students = students
        self.sim_length = sim_length
        self.trial = trial
        self.stats = pd.DataFrame(columns=['trial', 'day','masked','vaccinated', 'infected', 'contagious', 'exposure'],
                                  index=range(sim_length + 1))


    def run_simulation(self):
        exposure = self._calc_exposure()
        self.stats.iloc[0] = {'trial': self.trial,
                              'day': 0,
                              'infected': 1,
                              'contagious': 1,
                              'exposure': exposure}

        for i in range(self.sim_length):
            exposure = self._calc_exposure()
            self._log_statisticts(i, exposure)
            self.advance_day(i + 1, exposure)

    def advance_day(self, i, exposure):

        for s in self.students:
            s.go_to_class(exposure)

    def _log_statisticts(self, i, exposure):
        infected = [s for s in self.students if s.previously_infected]
        infected_len = len(infected)
        contagious = [s for s in self.students if s.contagious]
        contagious_len = len(contagious)
        masked = len([s for s in self.students if s.masked ==1])
        vaccinated = len([s for s in self.students if s.vaccinated == 1])

        data = {'trial': self.trial,
                'day': i,
                'infected': infected_len,
                'contagious': contagious_len,
                'masked': masked,
                'vaccinated': vaccinated,
                'exposure': exposure}
        self.stats.iloc[i] = data

    def _calc_exposure(self):
        pios = [1 - s.P_io for s in self.students]
        exposure = 1 - math.prod(pios)
        return exposure


class Student():
    def __init__(self, P_v, P_ve, P_m, P_me, infectiousness):
        self.P_m = P_m
        self.P_me = P_me
        self.P_v = P_v
        self.P_ve = P_ve
        self.infectiousness = infectiousness

        self.vaccinated = 1 if np.random.uniform(0, 1) <= self.P_v else 0
        self.masked = 1 if np.random.uniform(0, 1) <= self.P_m else 0
        self.P_io = 0
        self.previously_infected = False
        self.contagious = False
        self.days_infected = 0

    def go_to_class(self, exposure):
        if self.previously_infected == False:
            P_i = exposure * (1 - (self.vaccinated * self.P_ve))
            if np.random.uniform(0, 1) <= P_i:
                self.infect()

        if self.previously_infected and self.days_infected <= 3:
            self.days_infected += 1
            if self.days_infected == 3:
                self.contagious = False
                self.P_io = 0

    def infect(self):
        self.previously_infected = True
        self.contagious = True
        self.P_io = infectiousness * (1 - (self.masked * self.P_me))


if __name__ == '__main__':
    number_of_students = 200

    vaccinated_percentage = .5
    vaccine_efficiency = .8
    masked_percentage = 1
    mask_effectiveness = .5
    infectiousness = .02

    Students = [Student(vaccinated_percentage,
                        vaccine_efficiency,
                        masked_percentage,
                        mask_effectiveness,
                        infectiousness)
                for i in range(number_of_students)]

    Students[0].vaccinated = 0
    Students[0].infect()

    c = Classroom(Students, sim_length=100, trial=1)
    c.run_simulation()
    stats = c.stats
    print('finished')
