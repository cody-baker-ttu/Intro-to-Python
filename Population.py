years=input("How many years have passed? ")
years_int=int(years)
seconds=years_int*365*24*60*60
births=seconds/7
deaths=seconds/13
immigrants=seconds/35
current_population=307357870
new_population=current_population + births + immigrants - deaths
population=int(new_population)
print("The population is: ",population)
