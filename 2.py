import json
with open("./data/专业排名.json") as f:
    course_ranking = json.load(f)

for i in range(len(course_ranking)):
    school_name = course_ranking[i]["name"]
    disciplines = course_ranking[i]["ranked-disciplines"]
    cnt = 0
    for j in range(len(disciplines)):
        
