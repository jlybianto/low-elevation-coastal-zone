import collections

population_2010_dict = collections.defaultdict(int)
land_area_dict = collections.defaultdict(int)

with open("lecz-urban-rural-population-land-area-estimates-v2-csv/lecz-urban-rural-population-land-area-estimates_continent-90m.csv", "rU") as inputFile:
	header = next(inputFile)
	
	for line in inputFile:
		line = line.rstrip().split(",")
		line[5] = int(line[5])
		line[7] = float(line[7])
		if line[1] == "Total National Population":
			population_2010_dict[line[0]] += line[5]
			land_area_dict[line[0]] += line[7]

	population_density_2010_dict = {key: population_2010_dict[key] / land_area_dict.get(key, 0) for key in population_2010_dict.keys()}

with open("national_population_density_2010.csv", "w") as outputFile:
	outputFile.write("continent,population_density_2010\n")

	for k, v in population_density_2010_dict.iteritems():
		outputFile.write(k + "," + str(v) + "\n")