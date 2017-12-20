import csv

csv_file = open("output.csv", "w")
csv_writer = csv.writer(csv_file)

header = ["imageId", "Label"]
csv_writer.writerow(header)
key = 1
value = 2
var = [key, value]
csv_writer.writerow(var)
csv_file.close()