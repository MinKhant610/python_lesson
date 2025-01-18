setA = {1, 2, 3, 4}
setB = {1, 2, 5, 6}
print('setA union setB ', setA.union(setB))
print('setA intersection setB', setA.intersection(setB))
print('setB intersection setA', setB.intersection(setA))

setC = {1, 2, 3, 4}
setD = {3, 4, 5, 6}
print('setC difference setD ', setC.difference(setD))
print('setD difference setC ', setD.difference(setC))
print(setC - setD)
print(setD - setC)
print('summerize difference ', setC.symmetric_difference(setD))
