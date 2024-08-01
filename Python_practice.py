counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Pasp is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")

for county in counties:
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}


voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)        
           
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

for county_dict in voting_data:
    print(county_dict['county'])

for county, voters in counties_dict.items():
    print(county + " county has " +str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")    

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,} registered voters.")  

voting_data = (
    f"{county} county has {voters:,} registered voters."
)