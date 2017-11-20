from numpy import *

print 'create a new matrix'

matt = mat(random.rand(4, 4))
print matt
print matt.I
myEye = matt * matt.I