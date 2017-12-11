import pandas as pd

#write csv use DataFrame
columns = ["id", "name", "age", "sex", "score"]
data = {"id": [1, 2], "name": ["han", "min"], "age": [18, 20],
        "sex": ['M', 'L'], "score": [101, 99]}
data["id"].append(3)
data["name"].append("wang")
data["age"].append(22)
data["sex"].append('M')
data["score"].append(102)
dataFrame = pd.DataFrame(data=data, columns=columns)
print dataFrame
dataFrame.to_csv("instance.csv", index=False)

#read csv
df = pd.read_csv("instance.csv")
#print df.columns
#sort by a column
print df.sort_values(by="score")
#select some rows and one column
dl = df.loc[0:, "score"]
#change some value
for i in range(len(dl)):
    if dl[i] >= 100:
        dl[i] = 100
print dl
print type(dl)
#sleect some rows and some columns
dls = df.loc[0:, ["name", "score"]]
print dls
#print type(dls)
df.to_csv("instance.csv")