mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

total_number_missions = 0
successful_missions = 0

for m in mission_names:
    total_number_missions += 1
print ("Total number of missions:", total_number_missions)

for success in mission_success:
    if success==True:
        successful_missions +=1
print ("Number of successful missions:", successful_missions)

success_rate = successful_missions / total_number_missions * 100
success_rate_rounded=round(success_rate,2)
print ("Success rate:", success_rate_rounded,"%")

for y in range(total_number_missions):
    if mission_years[y] < 2000:
        print("- ", mission_names[y])
