#This code can optimize (with the Pareto method) to find most affordable laptops with max Ram   
import mysql.connector
import matplotlib.pyplot as plt
import numpy 
import matplotlib.pyplot as plt
import oapackage


cnx = mysql.connector.connect(user='md', password='M1377mmn',
                              host='127.0.0.1',
                              database='learn')
cursor = cnx.cursor()

query = 'SELECT * FROM laptop;'
cursor.execute(query)

datapoints = [[],[],[]]
for (Ram,Name,Cost) in cursor :
    datapoints[2].append(Name)
    datapoints[1].append(Ram)
    datapoints[0].append(Cost*(-1))



pareto=oapackage.ParetoDoubleLong()

for ii in range(0, len(datapoints[1])):
    d0ii = numpy.float64(datapoints[0][ii])
    d1ii = numpy.float64(datapoints[1][ii])
    w=oapackage.doubleVector((d0ii, d1ii))

    #w=oapackage.doubleVector( (datapoints[0,ii], datapoints[1,ii]))
    pareto.addvalue(w, ii)

pareto.show(verbose=1)
lst=pareto.allindices()

for i in lst :
    print("The most affordable laptop with %dG ram is : %s"% (datapoints[1][i],datapoints[2][i]))
    print("its price is : %d million Tomans" %(datapoints[0][i]*(-1)))
    print("*****")

h=plt.plot(datapoints[0], datapoints[1], '.b', markersize=5, label='Non Pareto-optimal')
_=plt.title('The input data', fontsize=1)
plt.xlabel('Cost', fontsize=16)
plt.ylabel('Ram', fontsize=16)
plt.show()   


cnx.close()