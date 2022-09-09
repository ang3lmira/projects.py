# with open("weather_data.csv") as data_file:
#data = data_file.readlines()
# print(data)

import csv
from traceback import print_list
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    # print(data)

    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))
    # print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

data_dictionary = data.to_dict()
# print(data_dictionary)

temp_list = data["temp"].to_list()
# print(temp_list)
# print(temp_list[1])


# Finding the average of a list
data["temp"].mean()
# or

list_length = len(temp_list)
# print(list_length)
average = round(sum(temp_list)/list_length, 2)
# print(average)


# Maximum number in a series
max_num = data["temp"].max()
# print(max_num)

# Getting data from row
monday = data[data.day == "Monday"]
print(monday.condition)

# Getting the row of the highest temperature
max_temp = data[data.temp == data.temp.max()]

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Erin"],
    "scores": ["90", "82", "71"]
}

some_data = pandas.DataFrame(data_dict)
print(some_data)

some_data.to_csv("new_data.csv")
