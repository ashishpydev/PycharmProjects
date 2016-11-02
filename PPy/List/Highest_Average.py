# This string encodes a list of cricket scores of a particular cricket batsman various matches.
# Each element of the list is a itself a list of two elements - the first is the name of the country
# against which the match was held, and the second is the score of the batsman.
#
# Write a python function called highest_avg that takes such a string as a parameter, and
# returns the country against which this batsman has the highest average. Average score against a
# country is defined as the sum of all the scores this batsman scored in matches against that country,
# divided by the number of matches played against that country
from collections import Counter

# 1. Get Unique Countries.
# 2. If the Unique country is equal to the countries in  the list in list
# 3. Add the score for the country


def get_count(l):
	count = Counter()
	for v in l:
		count[v[0]] += 1
	get_highest_avg(count, l)


def get_highest_avg(count, l):
	len_count = len(count)
	max_avg = {}
	for c in range(len(count):
		if count.pop(c) ==  l[][]
l = [["Pakistan", 23], ["Pakistan", 127], ["India", 3], ["India", 71], ["Australia", 31], ["India", 22], ["Pakistan", 81]]
get_count(l)
