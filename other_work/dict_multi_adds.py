
scores ={
"bernie": 0,
"biden" : 0,
"tulsi" : 0
}

print("bernie {}".format(scores["bernie"]))
print("biden {}".format(scores["biden"]))
print("tulsi {}".format(scores["tulsi"]))

q_1 ={
    "A" : "social justice",
    "B" : "economy",
    "A_add": ["bernie","biden"],
    "B_add": ["tulsi"]
    }

for x in q_1["A_add"]:
    scores[x] += 1
for x in q_1["A_add"]:
    scores[x] += 1
for x in q_1["B_add"]:
    scores[x] += 1

print("bernie {}".format(scores["bernie"]))
print("biden {}".format(scores["biden"]))
print("tulsi {}".format(scores["tulsi"]))
    
