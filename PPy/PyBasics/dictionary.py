towns = [
	{'name': 'Manchester', 'population': 58241},
	{'name': 'Coventry', 'population': 12435},
	{'name': 'South Windsor', 'population': 25709}]
# Using for loop
# for town in towns:
# 	print("Population of the town {} is: {}".format(town.get('name'), town.get('population')))

# Using lambda function
# town_names = []
# town_names = list(map(lambda town:(town.get('name')), towns))
# print(town_names)

# UnZip function...
town_populations = []
town_names = []
town_names, town_populations = zip(*[(town.get('name'), town.get('population')) for town in towns])
print(town_names)
print(town_populations)

# Given the two lists (names and populations), combine them back into a list of dictionaries using for loops.
# .. using list comprehensions.


townss = []
for index, town_name in enumerate(town_names):
	town = {'name': town_name, 'population': town_populations[index]}
	townss.append(town)
print(townss)

twn = {x: y for x, y in zip(town_names, town_populations)}
print(twn)
