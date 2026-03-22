#Run this is terminal to know the version of matplotlib
#python -c "import matplotlib;print(matplotlib.__version__)"

#Line plot
import matplotlib.pyplot as plt
import numpy as np
# x = np.arange(1,11)
# y = x**2
# plt.plot(x,y) #used to draw line plots
# plt.xlabel("Values of X") #Describes X - axis
# plt.ylabel("Power of X") #Describes Y - axis
# plt.title("First Line Plot Graph") #Adds title to graph
# plt.show() #Displays the graph 

#Questiion-1
# x = np.array([1,2,3,4,5])
# y = np.array([4,2,4,2,4])
# plt.plot(x,y) #used to draw line plots
# plt.xlabel("Values of X") #Describes X - axis
# plt.ylabel("Values of Y") #Describes Y - axis
# plt.title("First Line Plot Graph") #Adds title to graph
# plt.show() #Displays the graph 

#Questiion-2
x = np.arange(1,11)
y = x**3
plt.plot(x,y,marker="^",linestyle=':',color='orange') #used to draw line plots
plt.xlabel("Values of X") #Describes X - axis
plt.ylabel("Power of X") #Describes Y - axis
plt.title("Cube Line Plot Graph") #Adds title to graph
plt.show() #Displays the graph 

# Line Style property - supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'

