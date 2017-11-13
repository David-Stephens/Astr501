import numpy as np

dataFile = 'iso_massf00520.DAT'


indexPos = np.array([0, 5])
chargeNumPos = np.array([5, 12])
massNumPos = np.array([12, 17])
isomerPos = np.array([17, 21])
massFracPos = np.array([21, 35])
namePos = np.array([37, 42])

totalToRemove = 0.0
toSkip = 6

newData = open('iso_massf00521' + '.DAT', 'w')
oldData = open(dataFile, 'r')

x=0.995
h1=7.52973E-01
h2=1.941917367E-05
he3=7.526718108E-06
he4=2.470E-01
li6=9.69829224E-15
li7=3.499818504E-10

iso_change = {
      'PROT': x * h1,
      'HE2': x * h2,
      'HE3': x * he3,
      'HE4': x * he4,
      'LI6': x * li6,
      'LI7': x * li7,
    };


for key, elem in iso_change.items():
  totalToRemove += elem
  
indices = []
chargeNumbers = []
massNumbers = []
nameIndex = []
massFraction = []
isomers = []
realNameIndex = []

header = ''
skip = 0    
for line in oldData:
  if (skip > toSkip):
    indices.append(line[indexPos[0]:indexPos[1]].replace(' ', ''))
    chargeNumbers.append(line[chargeNumPos[0]:chargeNumPos[1]].replace(' ', ''))
    massNumbers.append(line[massNumPos[0]:massNumPos[1]].replace(' ', ''))
    massFraction.append(line[massFracPos[0]:massFracPos[1]].replace(' ', ''))
    isomers.append(line[isomerPos[0]:isomerPos[1]].replace(' ', ''))
    realNameIndex.append(line[namePos[0]:namePos[1]])
      
    nameIndex.append(line[namePos[0]:namePos[1]].replace(' ', ''))
  else:
    header += line
    
  skip += 1
 
oldData.close()

totalElements = skip - toSkip - 1

newData.write(header)

for i in range(totalElements):
  if nameIndex[i] in iso_change or float(massFraction[i]) <= 1.0e-99 or int(isomers[i]) != 1:
    if nameIndex[i] in iso_change:
      massFraction[i] = "{:.5E}".format(iso_change[nameIndex[i]])
      
    print ('Not changing ' + nameIndex[i] + '\n')
  else:
    massFraction[i] = "{:.5E}".format(float(massFraction[i]) * (1 - totalToRemove))
  
  newData.write(
      indices[i].rjust(5) 
        + chargeNumbers[i].rjust(7) 
        + massNumbers[i].rjust(5) 
        + isomers[i].rjust(4) 
        + massFraction[i].rjust(14) 
        + realNameIndex[i].rjust(7) 
        + '\n'
      )
 
newData.close()
