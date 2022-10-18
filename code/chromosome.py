import datetime
import numpy as np
import random

team_dict_bit = {
    "MECH": "000",
    "PROD": "001",
    "E&I": "010",
    "RES": "011",
    "DECK": "100"
}


def _str_time_prop(start, end, time_format, prop):
    stime = datetime.datetime.strptime(start, time_format)
    etime = datetime.datetime.strptime(end, time_format)
    ptime = stime + prop * (etime - stime)
    ptime = ptime.strftime("%d/%m/%Y")
    return ptime


def random_date(start, end, prop):  # 0001 = current year, 0002 = next year
    # generate date in current data
    sched_start = _str_time_prop(start, end, "%d/%m/%Y", prop)
    date_sched_start = format(int(sched_start[:2]), '05b')
    month_sched_start = format(int(sched_start[3:5]), '04b')
    year_sched_start = format(int(sched_start[6:]), '02b')
    sched_start = ''.join([date_sched_start, month_sched_start, year_sched_start])
    return sched_start


class CHROMOSOME:
    def __init__(self, df):
        self.HC_resource = []
        self.HC_time = []
        self.df = df
        self.chromosome = self._generate_parent()
        
    # Generate random date

    def _generate_parent(self):
        genes = []
        for wonum, tarsd, tared, team in zip(self.df.wonum, self.df.targstartdate, self.df.targcompdate,
                                             self.df.alt_bdpocdiscipline):
            rand_date = random_date(tarsd, tared, random.random())
            shift = random.choice([0, 1])
            team = team.split('|')
            # team_p = team_dict_bit[team[0]] + team_dict_bit[team[1]]
            
            team_gen = random.choice(team)
            team_gen = team_dict_bit[team_gen]
            num_people = ''.join(np.random.choice(['0', '1'], 2))
            # print(shift,rand_date,num_people,team_gen)
            bitstring = ''.join([str(shift), rand_date, num_people, team_gen])
            chromosome = '-'.join([wonum, tarsd, tared, bitstring])
            genes.append(chromosome)
        return np.asarray(genes)
