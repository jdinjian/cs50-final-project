import random
import sys
import tabulate

#inverse, increase growth speed = lower growth ! bit weird honestly
growth_speed = 2

all_locations = {

"ocean" : [
    {"fish": "Shark", "expected": 3, "population": 3},
    {"fish": "Tuna", "expected": 9, "population": 9},
    {"fish": "Mackerel", "expected": 27, "population": 27},
    {"fish": "Anchovy", "expected": 81, "population": 81},
    ],

"lake" : [
    {"fish":"Walleye", "expected":3, "population":3},
    {"fish":"Pike", "expected":9, "population":9},
    {"fish":"Perch", "expected":27, "population":27},
    {"fish":"Bluegill", "expected":81, "population":81}
    ],

"river" : [
    {"fish": "Bass", "expected": 3, "population": 3},
    {"fish": "Perch", "expected": 9, "population": 9},
    {"fish": "Sunfish", "expected": 27, "population": 27},
    {"fish": "Chub", "expected": 81, "population": 81},
]
}

help = [
    {"action": "Nighttime", "input":"night"},
    {"action": "Check Population", "input":"pop"},
    {"action": "Fish", "input":"fish"},
    {"action": "Ecosystem Health", "input":"health"},
    {"action": "Total population", "input":"total"},
    {"action": "Location", "input":"location"},
    {"action": "Reset populations", "input":"reset"},
    {"action": "Exit", "input":"exit"}
]


def change_location(location_input):
    if location_input == "lake" or location_input == "l":
        return "lake"
    elif location_input == "ocean" or location_input == "o":
        return "ocean"
    elif location_input == "river" or location_input == "r":
        return "river"
    elif location_input == "exit" or location_input == "e":
        sys.exit()
    return None


def choose_location():
    while True:
        location_input = input("| Lake | Ocean | River | \nWhere would you like to fish? ").strip().lower()
        pop_key = change_location(location_input)
        if pop_key is not None:
            night = Night(all_locations, pop_key, growth_speed)
            night.print_population()
            return pop_key
        else:
            continue


def main():
    chosen_location = choose_location()
    while True:
        prompt = input("What would you like to do? : ").lower().strip()
        night = Night(all_locations, chosen_location, growth_speed)

        if prompt == "help":
            help_data = [[row["action"], row["input"]] for row in help]
            print(tabulate.tabulate(help_data, headers = ["Action:", "Input:"], tablefmt = "rounded_grid", stralign = "left"))
        if prompt == "night" or prompt == "n":
            night.reproduce()
        elif prompt == "fish" or prompt == "f":
            try:
                fish, number_of_fish = input("What fish and how many?: ").split(" ")
                night.fished(fish, number_of_fish)
            except ValueError:
                continue
        elif prompt == "pop" or prompt == "p":
            night.print_population()

        elif prompt == "reset" or prompt == "r":
            for species_list in all_locations.values():
                for row in species_list:
                    row["population"] = row["expected"]
            print("Populations reset")
        elif prompt == "health" or prompt == "h":
            print(night.ecosystem_health())
        elif prompt in [ "location", "loc", "l"]:
            chosen_location = choose_location()
        elif prompt in [ "total pop", "total population", "tp", "total"]:
            night.print_all_population()
        elif prompt == "exit" or prompt == "e":
            sys.exit()
        else:
            continue


class Night:
    def __init__(self, all_locations, active_location, growth_speed):
        self.active_location = active_location
        self.all_locations = all_locations
        self.growth_speed = growth_speed

    def reproduce(self):
        for location_name, species_list in self.all_locations.items():
            pops = []
            for row in species_list:
                if row["population"] <= 0:
                    sys.exit(f"A species in the {location_name} went extinct!")
                if row["population"] > row["expected"] * 3:
                    night = Night(all_locations, self.active_location, growth_speed)
                    print("\n Final Pop: \n")
                    night.print_population()
                    sys.exit(f"The {location_name} overpopulated!")

            for i, current_fish in enumerate(species_list):
                pop_value = get_pop_value(i, species_list)
                new_pop = self.new_population(pop_value, current_fish["population"])
                pops.append(new_pop)

            for i, population in enumerate(pops):
                if abs(population) >= (species_list[i]["population"]/2) and i > 0:
                    species_list[i]["population"] += round((species_list[i]["population"]/4))
                else:
                    species_list[i]["population"] += int(population)



    def new_population(self, pop_value, current_pop):
        random1 = (random.randint(-1,1) * (.1))
        added_pop = (((pop_value) + random1)*(current_pop/self.growth_speed))
        return round(added_pop, 0)

    def fished(self, fish, number_of_fish):
        active_list = self.all_locations[self.active_location]
        found = False
        for row in active_list:
            if row["fish"].lower() == fish.lower():
                found = True
                amount = int(number_of_fish)
                if row["population"] >= amount:
                    row["population"] -= amount
                else:
                    print("Aren't enough fish")
                break
        if not found:
            print("Fish not found")


    def print_population(self):
        species_list = self.all_locations[self.active_location]
        print_data = [[row["fish"], row["population"]] for row in species_list]
        print(tabulate.tabulate(print_data, headers = ["Fish", "Population"], tablefmt = "rounded_grid", stralign = "left", numalign = "center"))


    def ecosystem_health(self):
        active_list = self.all_locations[self.active_location]
        return f"The {self.active_location} is " + calculate_health(active_list)


    def print_all_population(self):
        header = ["Ocean Fish", "Ocean Pop", "Lake Fish ", "Lake Pop ", "River Fish", "River Pop"]
        combined_populations = []
        ocean, lake, river = self.all_locations["ocean"], self.all_locations["lake"], self.all_locations["river"]
        for i in range(4):
            combined_populations.append([
                ocean[i]["fish"],
                ocean[i]["population"],
                lake[i]["fish"],
                lake[i]["population"],
                river[i]["fish"],
                river[i]["population"]
            ])
        print(tabulate.tabulate(combined_populations, headers = header, tablefmt = "rounded_grid", stralign = "left", numalign = "center"))


def calculate_health(pop):
    pop_dif = 0
    for row in pop:
        difference = row["expected"] - row["population"]
        pop_dif += abs(difference)
    if pop_dif <= 10:
        return "healthy"
    elif pop_dif < 17:
        return "almost healthy"
    elif pop_dif < 25:
        return "almost unhealthy"
    elif pop_dif < 50:
        return "unhealthy"
    elif pop_dif > 50:
        return "extremely unhealthy"


def get_pop_value(i, pop):
    if i == 0:
        pop_value = (( (pop[i+1]["population"]) / (pop[i+1]["expected"]) * 1.05 +
                        (pop[i]["expected"]) / (pop[i]["population"])) -2)

    elif 0 < i < 3:
        pop_value = ( ((pop[i-1]["expected"]) / (pop[i-1]["population"]))  +
                        ((pop[i+1]["population"]) / (pop[i+1]["expected"])) +
                        ((pop[i]["expected"]) / (pop[i]["population"])) -3)
    elif i == 3:
        pop_value = ( ((pop[i-1]["expected"]) / (pop[i-1]["population"])) +
                        ((pop[i]["expected"]) / (pop[i]["population"])) -2)
    return pop_value


if __name__ == "__main__":
    main()
