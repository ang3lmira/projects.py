import pandas

all_data = pandas.read_csv("project/central_park_census.csv")

gray_s = all_data[all_data["Primary Fur Color"] == "Gray"]
gray_s_count = len(gray_s)
# print(gray_s)
# print(gray_s_count)


red_s = all_data[all_data["Primary Fur Color"] == "Cinnamon"]
red_s_count = len(red_s)
# print(red_s)
# print(red_s_count)


black_s = all_data[all_data["Primary Fur Color"] == "Black"]
black_s_count = len(black_s)
# print(black_s)
# print(black_s_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_s_count, red_s_count, black_s_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
