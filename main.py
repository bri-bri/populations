from models.population import Population

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--population', type=int, default=20)
    parser.add_argument('--years', type=int, default=100)
    args = parser.parse_args()

    pop = Population(args.population)
    years = 0
    while years <= args.years:
        pop.step()
        print("Year: %d, People: %d, Women: %d" % (years, pop.countPopulation(), pop.countByGender("F")))
        years += 1