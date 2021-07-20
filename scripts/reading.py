import pandas as pd

df = pd.read_csv("Tx_County.csv")
formatted_df = pd.melt(df, ["County"],var_name= "Year", value_name="Population")
formatted_df = formatted_df.sort_values(by = ["County"])
output = formatted_df.values

def isnumber(a):
    if a == '0' or a == '1'or a == '2'or a == '3'or a == '4'or a == '5'or a == '6'or a == '7'or a == '8'or a == '9':
        return 1
    else:
        return 0

for county in output:
    county_name = county[0]
    name = ""
    if not pd.isnull(county[0]):
        for i in county_name: #clean up the superscript footnote references in the county names
            if not isnumber(i):
                name = name + i
        county[0] = name
    else:
        county[1] = "" #delete all the rows with null value

formatted_df.to_csv("output.csv",index = False, sep = ",")