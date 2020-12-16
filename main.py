import numpy
import pandas as pd

# Import input files
path_import = "./Input_Files/"
raw_data = pd.read_csv(path_import + "data.csv")
data = raw_data.copy(deep=True)
airlines_list = pd.read_csv(path_import + "airlines_list.csv")
countries_list = pd.read_csv(path_import + "countries_list.csv")
types_list = pd.read_csv(path_import + "types_list.csv")

# Transform date into pandas format
data["Date"] = pd.to_datetime(data["Date"])

# Type transformation
data["Model"] = ""
for i in range(len(types_list["Type"])):
	for j in range(len(data["Type"])):
		if (str(types_list["Type"].iloc[i]) in str(data["Type"].iloc[j])):
			data["Model"].iat[j] = types_list["Type"][i]

data["Model"][data["Model"].isnull()] = "Unknown"

# Find operator countries
data["Airline"] = ""
data["Segment"] = ""
data["Country_Airline"] = ""
data["Country_Operator_Guess"] = ""

for i in range(len(airlines_list["Airline"])):
	for j in range(len(data["Operator"])):
		if (str(airlines_list["Airline"].iloc[i]) in str(data["Operator"].iloc[j])):
			data["Airline"].iat[j] = airlines_list["Airline"][i]
			data["Segment"].iat[j] = airlines_list["Segment"][i]
			data["Country_Airline"].iat[j] = airlines_list["Country"][i]

for i in range(len(countries_list["Short"])):
	for j in range(len(data["Operator"])):
		if (str(countries_list["Short"].iloc[i]) in str(data["Operator"].iloc[j])):
			data["Country_Operator_Guess"].iat[j] = countries_list["Country"][i]

data["Country_Operator"] = data["Country_Airline"]
data["Country_Operator"][data["Country_Operator"].isnull()] = data["Country_Operator_Guess"]
data["Country_Operator"][data["Country_Operator"].isnull()] = "Unknown"

#print("Missing Airline: ", data["Airline"].loc[data["Airline"] == ""].count())

# Crash locations cleansing
data["Country"] = ""
data["Subregion"] = ""
data["Region"] = ""
data["Category"] = ""

for i in range(len(countries_list["Country"])):
	for j in range(len(data["Location"])):
		if (str(countries_list["Country"].iloc[i]) in str(data["Location"].iloc[j])):
			data["Country"].iat[j] = countries_list["Country"][i]
			data["Subregion"].iat[j] = countries_list["Subregion"][i]
			data["Region"].iat[j] = countries_list["Region"][i]
			data["Category"].iat[j] = countries_list["Category"][i]

data["Country"].loc[data["Country"] == ""] = "Unknown"

# Fatalities rate & survival rate
data["Fatalities_Rate"] = data["Fatalities"] / data["Aboard"]
data["Survival_Rate"] = 1 - data["Fatalities_Rate"]

# Export cleasned data set
data.to_csv(r'./clean_data_set.csv')

#data = data.drop(data["Date"][data["Date"] < "1945-01-01 00:00"].index)
#data = data.drop(data["Country"][data["Country"] == "Unknown"].index)
#data = data.drop(data["Fatalities_Rate"][data["Fatalities_Rate"].isnull()].index)
#data = data.drop(["Flight #","Route","Registration","Summary","cn/In"], axis=1)
