import math


vector = [1, 2, 3, 4, 1, 2, 3]
fm = 0
for each in vector:
    fm = fm + math.exp(each)

for i in range(len(vector)):
    vector[i] = math.exp(vector[i]) / fm

print vector
print sum(vector)
print max(vector)