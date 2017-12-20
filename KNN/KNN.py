from numpy import *
import os


class KNN:
    def __init__(self, conf_file, train_file, test_file):
        self.conf_file = conf_file
        self.train_file = train_file
        self.test_file = test_file
        self.train_path = "trainingDigits/"
        self.test_path = "testDigits/"
        #self.test_path = "mytest/"
        self.vector_len = 1024
        self.train_matrix = zeros((len(self.train_file), self.vector_len))
        self.res_vector = []
        self.k = 15

    def train(self, filename):
        data_file = open(self.train_path + filename, "r")
        vector = []
        res = int(filename.split("_")[0])
        data_lines = data_file.readlines()
        for line in data_lines:
            line = line.strip()
            for i in range(len(line)):
                vector.append(int(line[i]))
        return vector, res

    def test(self, filename):
        test_file = open(self.test_path + filename, "r")
        vector = []
        test_lines = test_file.readlines()
        for line in test_lines:
            line = line.strip()
            for i in range(len(line)):
                vector.append(int(line[i]))
        vector_mat = tile(vector, (self.train_matrix.shape[0], 1))
        diff_mat = self.train_matrix - vector_mat
        print type(self.train_matrix), type(vector_mat), type(diff_mat)
        sq2_mat = diff_mat**2
        sum_mat = sq2_mat.sum(1)
        dist_mat = sum_mat**0.5
        sorted_index = dist_mat.argsort()
        dict = {}
        for i in range(self.k):
            index = sorted_index[i]
            dict[self.res_vector[index]] = dict.get(self.res_vector[index], 0) + 1
        res = int(filename.split("_")[0])
        print res, dict

    def run(self):
        index = 0
        for tf in self.train_file:
            vector, res = self.train(tf)
            self.res_vector.append(res)
            self.train_matrix[index, :] = vector
            index = index + 1
        print self.train_matrix.shape

        for ef in self.test_file:
            self.test(ef)

tfs = os.listdir("trainingDigits")
cfs = "conf"
efs = os.listdir("testDigits")
knn = KNN(cfs, tfs, efs)
knn.run()