import csv
from pandas import *
import numpy as np
import pandas as pd


def read_file1(filename):
    rf = open(filename, "r")
    lines = rf.readlines()
    for line in lines:
        print line.strip()
    rf.close()


def read_file2(filename):
    rf = open(filename, "r")
    lines = rf.read()
    print lines
    rf.close()


def read_file3(filename):
    rf = open(filename, "r")
    try:
        while True:
            line = rf.readline()
            if line:
                print line.strip()
            else:
                break
    finally:
        rf.close()


def write_file1(filename):
    #a  = add
    #w+ = clear and write
    #w  = delete, build and write
    wf = open(filename, "a")
    data = "Hello World"
    wf.write(data)
    wf.close()


def write_file2(filename):
    wf = open(filename, "a")
    data = ["Hello World2", "Hello World3"]
    wf.writelines(data)
    wf.close()


dict = {"krven": 3000, "over": 2000, "tty": 1000}
idx = ["java", "python", "krven", "over", "tty"]
se = Series(dict)
see = Series(se, index=idx)
print see.isnull()
print see