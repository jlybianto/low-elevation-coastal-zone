import collections

population_2010_dict = collections.defaultdict(int)
population_2100_dict = collections.defaultdict(int)

with open("lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv", "rU") as inputFile:
	header = next(inputFile)
	
	for line in inputFile:
		line = line.rstrip().split(",")
		line[5] = int(line[5])
		line[6] = float(line[6])
		if line[1] == "Total National Population":
			population_2010_dict[line[0]] += line[5]
			population_2100_dict[line[0]] += line[6]

	population_2100_2010_dict = {key: population_2100_dict[key] - population_2010_dict.get(key, 0) for key in population_2100_dict.keys()}
	population_2100_2010_dict = {key: population_2100_2010_dict[key] / population_2010_dict.get(key, 0) for key in population_2100_2010_dict.keys()}

with open("national_population_change_2010_2100.csv", "w") as outputFile:
	outputFile.write("continent,population_percent_change\n")

	for k, v in population_2100_2010_dict.iteritems():
		outputFile.write(k + "," + str(v) + "\n")