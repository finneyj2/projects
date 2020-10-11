import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt; plt.rcdefaults()
import tableQueryConnect
import tableQueryColleges
import tableQueryConditions
#h = np.array ([2, 3, 4, 5, 6])
#numPractice = np.array([72,200.00, 75,500.00, 71,800.00, 62,400.00])
#numPM = np.mean(numPractice)
#hPM = np.mean(h)
#numPME =np.median(numPractice)
#numPSTD = np.std(numPractice)
#X = hPM
#Y = numPM
#plt.scatter(X,Y)
#plt.title('Relationship Between Temperature and Iced Coffee Sales')
#plt.show()

def AVbar_graph():
    medBar = tableQueryConnect.runStatsMean()
    midBar = tableQueryConnect.runStatsMeanMid()
    mid10 = tableQueryConnect.runStatsMean10()
    objects = ('N.MedianSalary', 'N.MidCareer', 'N.10thPercentile', 'N.90thPercentile')
    y_pos = np.arange(len(objects))
    performance = [74786.0,69.274,mid10,142766.0]
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Range')
    plt.title('Salaries')

    plt.show()

def AVbarR_graph():
    objects = ('California', 'Western', 'Northeastern', 'Midwestern', 'Southern' )
    y_pos = np.arange(len(objects))
    locationMidC = tableQueryConditions.runWhere()
    locationEast = tableQueryConditions.runWhereEast()
    locationNortheast = tableQueryConditions.runWhereNorthEast()
    locationMidwest = tableQueryConditions.runWhereMidWestern()
    locationSouthern = tableQueryConditions.runWhereSouthern()
    performance = [50314.81481481482,44080.48780487805,48400.0, 44052.857142857145, 44271.794871794875]
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Starting_Median_Salary')
    plt.title('Salaries')

    plt.show()

def AVbarR_graphMidCareerMedian():
    objects = ('California', 'Western', 'Northeastern', 'Midwestern', 'Southern' )
    y_pos = np.arange(len(objects))
    locationMidC = tableQueryConditions.runWhereMidCareer()
    locationWest = tableQueryConditions.runWhereWestMidCareer()
    locationNortheast = tableQueryConditions.runWhereNorthEastMidCareer()
    locationMidwest = tableQueryConditions.runWhereMidWesternMidCareer()
    locationSouthern = tableQueryConditions.runWhereSouthernMidCareer()
    performance = [locationMidC,locationWest,locationNortheast, locationMidwest, locationSouthern]
    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('MidCareer_Median_Salary')
    plt.title('Salaries')

    plt.show()
def typeBarM_graph():
    typeLib = tableQueryColleges.runType()
    typePart = tableQueryColleges.runTypeParty()
    typeEn = tableQueryColleges.runTypeEn()
    typeState = tableQueryColleges.runTypeState()
    typeIv = tableQueryColleges.runTypeIvy()

    objects = ('Liberal Arts', 'Party', 'Engineering', 'State', 'Ivy' )
    y_pos = np.arange(len(objects))
    performance = [typeLib, typePart, typeEn, typeState, typeIv]
    plt.bar(y_pos, performance, align ='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('Starting_Median_Salary')
    plt.title('Salaries')

    plt.show()

def typeBarMidCareerMedian():
    typeLibMidCareer = tableQueryColleges.runType()
    typePartMidCareer = tableQueryColleges.runTypeParty()
    typeEnMidCareer = tableQueryColleges.runTypeEn()
    typeStateMidCareer = tableQueryColleges.runTypeState()
    typeIvMidCareer = tableQueryColleges.runTypeIvy()
    objects = ('Liberal Arts', 'Party', 'Engineering', 'State', 'Ivy' )
    y_pos = np.arange(len(objects))
    performance = [typeLibMidCareer, typePartMidCareer, typeEnMidCareer, typeStateMidCareer, typeIvMidCareer]
    plt.bar(y_pos, performance, align ='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('MidCareer_Median_Salary')
    plt.title('Salaries')

    plt.show()
if __name__ == '__main__':
    AVbar_graph()
    AVbarR_graph()
    AVbarR_graphMidCareerMedian()
    typeBarM_graph()
    typeBarMidCareerMedian()
