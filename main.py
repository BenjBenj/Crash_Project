import numpy
import pandas as pd

path_import = "./Input_Files/"

data = pd.read_csv(path_import + "data.csv")
airlines_list = pd.read_csv(path_import + "airlines_list.csv")
countries_list = pd.read_csv(path_import + "countries_list.csv")
types_list = pd.read_csv(path_import + "types_list.csv")

data["Date"] = pd.to_datetime(data["Date"])























#data = data.drop(["Flight #","Route","Registration","Summary","cn/In"], axis=1)


#for i in range(len(airlines_list)):
#	print("###",airlines_list["Airline"][i], data["Operator"].str.contains(airlines_list["Airline"][i],case=False).value_counts())


c_t = types_list.copy(deep=True)
c_t["Count"] = 0


for i in range(len(types_list["Type"])):
	for j in range(len(data["Type"])):
		if (str(types_list["Type"].iloc[i]) in str(data["Type"].iloc[j])):
			c_t["Count"].iat[i] = c_t["Count"][i] + 1


print(c_t)
c_t.to_csv(r'./c_a.csv')



quit()

data["Airline"] = ""
data["Short"] = ""



c_a = airlines_list
c_a["Count"] = 0

#
#for i in range(len(airlines_list["Airline"])):
#	for j in range(len(data["Operator"])):
#		if (str(airlines_list["Airline"].iloc[i]) in str(data["Operator"].iloc[j])):
#			c_a["Count"].iat[i] = c_a["Count"][i] + 1
#
#
#print(c_a)
#c_a.to_csv(r'./c_a.csv')
#
#quit()
#

data["Country_Origin"] = ""

for i in range(len(airlines_list["Airline"])):
	for j in range(len(data["Operator"])):
		if (str(airlines_list["Airline"].iloc[i]) in str(data["Operator"].iloc[j])):
			data["Airline"].iat[j] = airlines_list["Airline"][i]
			data["Country_Origin"].iat[j] = airlines_list["Country"][i]


for i in range(len(countries_list["Short"])):
	for j in range(len(data["Operator"])):
		if (str(countries_list["Short"].iloc[i]) in str(data["Operator"].iloc[j])):
			data["Short"].iat[j] = countries_list["Country"][i]

data[["Airline","Operator","Short","Country_Origin"]].to_csv(r'./check_operators.csv')


print(data["Airline"].loc[data["Airline"] == ""].count())

quit()

data["Country"] = ""
data["Subregion"] = ""
data["Region"] = ""
data["Category"] = ""


for i in range(len(countries_list["Country"])):
	for j in range(len(data["Location"])):
		if (str(countries_list["Country"].iloc[i]) in str(data["Location"].iloc[j])):
			#data["Country"][j] = countries_list["Country"][i]
			data["Country"].iat[j] = countries_list["Country"][i]
			data["Subregion"].iat[j] = countries_list["Subregion"][i]
			data["Region"].iat[j] = countries_list["Region"][i]
			data["Category"].iat[j] = countries_list["Category"][i]


data["Country"].loc[data["Country"] == ""] = "Unknown"
data = data.drop(data["Date"][data["Date"] < "1945-01-01 00:00"].index)
data = data.drop(data["Country"][data["Country"] == "Unknown"].index)
data["Fatalities_Rate"] = data["Fatalities"] / data["Aboard"]
data = data.drop(data["Fatalities_Rate"][data["Fatalities_Rate"].isnull()].index)
print(data["Country"])



data.to_csv(r'./clean_location.csv')

quit()

for i in range(len(france_names)):
	print(data["Location"].str.contains(france_names[i],case=False).value_counts())

