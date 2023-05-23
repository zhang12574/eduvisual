import json
ranking_data = {}
for year in range(2015, 2020):
    with open("data/{}年高校最好大学排名（空）.json".format(year), "r", encoding="utf-8") as f:
        data = json.load(f)
        for i in range(len(data)):
            if not ranking_data.get(data[i]["name"]):
                ranking_data[data[i]["name"]] = {str(year):data[i]["rank"]}
            else:
                ranking_data[data[i]["name"]][str(year)] = data[i]["rank"]

final_data = []
for each_key in ranking_data.keys():
    each_data = {}
    each_data["name"] = each_key
    for each_year in ranking_data[each_key].keys():
        each_data["rank{}".format(each_year)] = ranking_data[each_key][each_year]
    final_data.append(each_data)

with open("./src/ranking_data.json", "w") as f:
    json.dump(final_data, f)