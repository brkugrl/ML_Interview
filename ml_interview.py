# -*- coding: utf-8 -*-
"""ML_Interview.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YTuFJBQ2W-yQeWJz2qKuWgnSWZpPVsEe
"""

import numpy as np
import matplotlib.pyplot as plt

numberOfFamilies = 1000
numberOfSamples = 10000


class Person():
  def __init__(self, familyID):
    self.familyID = familyID
  def getFamilyID(self):
    return self.familyID

class Population():
  def __init__(self):
    self.population = []
  def addPerson(self, person):
    self.population.append(person)
  def getPopulationSize(self):
    return(len(self.population))
  def getRandomPerson(self):
    return self.population[np.random.randint(0, len(self.population))]



families = {i:[] for i in range(0,numberOfFamilies)}

def updateFamilies(families, familyID, familyMember):
  families[familyID].append(familyMember)



population = Population()

for l in range(numberOfFamilies):
  sizeOfFamily = np.random.randint(1, 10)
  for _ in range(sizeOfFamily):
    familyMember = Person(l)
    population.addPerson(familyMember)
    updateFamilies(families, l, familyMember)

hist = []
totalSampleSize = 0
for _ in range(numberOfSamples):
  sampleFamilyID = (population.getRandomPerson()).getFamilyID()
  sampleFamilySize = len(families[sampleFamilyID])
  totalSampleSize += sampleFamilySize
  hist.append(sampleFamilySize)

plt.hist(hist, bins=9)
plt.title('Sampled Family Size')
plt.ylabel('number of samples')
plt.xlabel('family size')
plt.show()
   

hist2 = []
for k in range(len(families)):
  hist2.append(len(families[k]))

plt.hist(hist2, bins=9)
plt.title('Real Family Size')
plt.ylabel('number of families')
plt.xlabel('family size')
plt.show()


print('Sampled average family size:', totalSampleSize/numberOfSamples)
print('Real average family size:', population.getPopulationSize()/numberOfFamilies)


hist = []
for j in range(100):
  totalSampleSize = 0
  for _ in range(numberOfSamples):
    sampleFamilyID = (population.getRandomPerson()).getFamilyID()
    sampleFamilySize = len(families[sampleFamilyID])
    totalSampleSize += sampleFamilySize
  hist.append(totalSampleSize/numberOfSamples)

plt.hist(hist, bins=9)
plt.title('Histogram of x_mean')
plt.ylabel('number of samples')
plt.xlabel('average family size')
plt.show()
