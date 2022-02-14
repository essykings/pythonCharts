#Plot a single graph


import matplotlib.pyplot as plt
year =[2010,2011,2012,2013,2014,2015]
sales = [0, 1000,5000,15000,50000,100000]
plt.plot(year, sales)plt.xlabel('year') 
plt.ylabel('Amount in Dollars') 
  
# title
plt.title("Linear graph Showing Growth of Lux store")
plt.show()


# Multiple plots

import matplotlib.pyplot as plt
year =[2010,2011,2012,2013,2014,2015]
sales = [0, 1000,5000,15000,50000,100000]
profit = [0,600,3000,9000,30000,60000]
plt.plot(year, sales)
plt.plot(year,profit)

plt.xlabel('year') 
plt.ylabel('Amount in Dollars') 
  
# displaying the title
plt.title("Linear graph Showing Growth of Lux store")
plt.show()


# Bar Chart

from matplotlib import pyplot as plt
pizzas = ['Cheese',
'Veggie', 'Pepperoni', 'Meat', 'Margherita', 'Chicken', 'Hawaiian', 'Buffalo']
    
popularity =  [98, 90, 86, 84, 82, 80,80,80]
plt.bar(range(len(pizzas)), popularity)
ax = plt.subplot()
ax.set_xticks(range(8))
ax.set_xticklabels(pizzas,rotation=40)
plt.show()



# Stacked bars
from matplotlib import pyplot as plt
pizzas = ['Cheese',
'Veggie', 'Pepperoni', 'Meat', 'Margherita', 'Chicken', 'Hawaii', 'Buffalo']
    
popularity_in_A =  [98, 90, 86, 84, 82, 80,80,80]
popularity_in_B =  [90, 85, 84, 83, 82, 80,80,80]
plt.bar(range(len(pizzas)), popularity_IN_A)
plt.bar(range(len(pizzas)), popularity_IN_A, bottom =popularity_IN_B  )
ax = plt.subplot()
ax.set_xticks(range(8))
# ax.set_xticks([0, 1, 2, 3, 4, 5, 6, 7, 8])
ax.set_xticklabels(pizzas,rotation=40)
plt.show()


#Pie Charts
from matplotlib import pyplot as plt
programming_languages = ["Python", "Java","Javascript",   "C++", "C#", 'C','Typescript']
Popularity = [230000, 170000, 150000, 100000,70000,70000,50000]
# plt.pie(Popularity)
plt.pie(Popularity,labels = programming_languages,   autopct='%0.1f%%')
plt.axis('equal')
plt.show()


#Histograms
from matplotlib import pyplot as pltdata = [100,  210, 0, 3, 20, 1000]
plt.hist(data, bins=20)plt.show()
