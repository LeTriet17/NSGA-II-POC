import random

test_str = "H13827744-01/03/0002-31/03/0002-11000100111011011"
test_str2 = "H13834153-01/04/0002-30/04/0002-10001001001011010"
#bitstring = ''.join([str(shift), rand_date, num_people, team_gen])
#shift: 1bit
#rand_date: 11bit 
#num_people: 2bit
#team_gen: 3bit

begin = test_str.rfind('-') + 1

shift = test_str[begin]
rand_date = test_str[begin + 1: begin + 12]
num_people = test_str[begin + 12 : begin + 14]
team_gen = test_str[begin + 14 : begin + 17]

crossover_rand_date = random.sample(range(begin + 1,begin + 12),2)
crossover_num_people = random.sample(range(begin + 12,begin + 14),2)
# crossover_team_gen = random.sample(range(begin + 12,begin + 14),2)

print(test_str[-17:])