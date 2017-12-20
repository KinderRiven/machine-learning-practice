

class DF:

    def __init__(self, tf_list):
        self.tf_list = tf_list

    def test(self, filename):
        test_file = open(filename)
        lines = test_file.readlines()
        for line in lines:
            line = line.strip()
            line = line.split('\t')
            print line

    def run(self):
        for tf in self.tf_list:
            self.test(tf)

tf_list = ["lenses.txt"]
df = DF(tf_list)
df.run()