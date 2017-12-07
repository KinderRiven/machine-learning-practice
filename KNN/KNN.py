from numpy import *


def file2matrix(filename):
    data_file = open(filename, "r")
    data_lines = data_file.readlines()
    res_mat = zeros((len(data_lines), 3))
    res_vector = []
    index = 0
    for line in data_lines:
        line = line.strip()
        list_format = line.split('\t')
        res_mat[index, :] = list_format[0:3]
        res_vector.append(int(list_format[-1]))
        index = index + 1
    return res_mat, res_vector


def algorithm_knn(test_data , input_mat, input_vector, k) :
    print test_data
    print input_mat.shape
    diff_mat = tile(test_data, (input_mat.shape[0], 1)) - input_mat
    dist2_mat = diff_mat**2
    sum_mat = dist2_mat.sum(1)
    dist_mat = sum_mat**0.5
    sorted_dist = dist_mat.argsort()
    res_dict = {}
    for i in range(k):
        index = sorted_dist[i]
        print dist_mat[index], input_vector[index]
        res_dict[input_vector[index]] = res_dict.get(input_vector[index], 0) + 1
    print res_dict

input_mat, input_vector = file2matrix("datingTestSet2.txt")
test_data = [50000, 17.249135, 0.492735]
print type(test_data)
print type(input_mat)
algorithm_knn(test_data, input_mat, input_vector, 10)