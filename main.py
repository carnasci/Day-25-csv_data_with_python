# with open("./weather_data.csv") as data_file:
#     data_list = data_file.readlines()
#
# print(data_list)

# import csv
#
# with open("./weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

#data = pandas.read_csv("weather_data.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# #Get data in columns
# print(data["condition"])
# print(data.condition)

#Get data from row
# print(data[data.day == "Monday"])
#
# max_temp = data.temp.max()
# print(data[data.temp == max_temp])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# print(monday.temp * 9/5 + 32)

#Create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65],
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

black_count = len(data[data["Primary Fur Color"] == "Black"])
#print(black)

cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
#print(cinnamon)

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
#print(gray)

data_dict = {
    "Fur Color": ["Black", "Cinnamon", "Gray"],
    "Squirrel count": [103, 392, 2473],
}

squirrel_data = pandas.DataFrame(data_dict)
print(squirrel_data)
squirrel_data.to_csv("squirrel_count.csv")