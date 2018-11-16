import math
import statistics


def area(r):
    """ Area of a circle with radius 'r'
    """
    return math.pi * (r**2)

radii = [2,5,7.1,8.0,10.11]
areas = []

for r in radii:
    a = area(r)
    areas.append(a)
print(areas)

#With map function I can do the same thing map(function,my_list) or map(f,data)
print(list(map(area,radii)))

#---------------------------------------------------------------------

#Lambda and map function
#This is a list of tuples
temps_world = [('Berlin',29),('Tokio',27),('New York',28),('London',22)]
#function will be pass a map
c_to_f = lambda lf: (lf[0], (9/5) * lf[1] + 32)
print(list(map(c_to_f,temps_world)))

#--------------------------------------------------------------------

#Filter function is used to select certain pieces of data from a list,tuple or other collection data
data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print('avg = ',avg)
print('values > av',list(filter(lambda x : x > avg, data)))
print('values < av',list(filter(lambda x : x < avg, data)))

#--------------------------------------------------------------
#REMOVE MISSING DATA
countries = ['alemania','argentina','brazil','chile','','colombia','','ecuador','','venezuela']
print(len(countries))
print(len(list(filter(None,countries))))
print(list(filter(None,countries)))
