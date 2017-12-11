from pandas import *

data1 = {"java": 2000, "python": 1000, "c++": 2000}
index1 = {"java", "python", "c", "c#"}
se = Series(data=data1, index=index1)
print se

column = ["id", "name", "age", "sex", "score", "final"]
data = {"id": ["1", "2", "3"],
        "name": ["han", "min", "yang"],
        "age": [18, 19, 22],
        "sex": ["man", "woman", "man"],
        "score": [99, 100, 99]}
fr = DataFrame(data=data, columns=column)
print fr