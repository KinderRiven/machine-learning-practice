import csv
import numpy as np


def file2matrix(filename):
    train_file = open(filename, "r")
    csv_reader = csv.reader(train_file)
    ret_mat = []
    ret_class = []
    index = 0
    for line in csv_reader:
        if index > 0:
            ret_mat.append(line[1:])
            ret_class.append(int(line[0]))
        index = index + 1
    return ret_mat, ret_class


def KNN(test_data, data_matrix, ret_class, k):
    rep_mat = np.tile(test_data, (data_mat.shape[0], 1))
    diff_mat = data_matrix - rep_mat
    sq2_mat = diff_mat**2
    sum_mat = sq2_mat.sum(1)
    dist_mat = sum_mat**0.5
    sort_mat = dist_mat.argsort()
    dict = {}
    for each in range(k):
        idx = sort_mat[each]
        dict[ret_class[idx]] = dict.get(ret_class[idx], 0) + 1
    return max(dict)


ret_matrix, ret_class = file2matrix("train.csv")
data_mat = np.array(ret_matrix).astype(np.int32)
test_file = open("test.csv", "r")
test_reader = csv.reader(test_file)
index = 0
result_file = open("sample_submission.csv", "w")
result_writer = csv.writer(result_file)
header = ["imageId", "Label"]
result_writer.writerow(header)
for test in test_reader:
    if index > 0:
        test_data = np.array(test).astype(np.int32)
        res = KNN(test_data, data_mat, ret_class, 10)
        print index, res
        result_writer.writerow([index, res])
    index = index + 1
result_file.close()
