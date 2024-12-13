# used for plotting purposes using the plot() method
# we use pyplot a submodule of matplotlib for plotting puropes
# we import it by import matplotlib.pyplot as plt 
# we also use numpy for numerical computations
import matplotlib.pyplot as plt
import numpy as np
x = np.array[1,3]
y = np.array[0,6]
plt.plot(x,y)
plt.show()

# the above expression draws a line between point [1,0] and [3,6]


                       # PLOTING X AND Y POINTS
# we use the plot() method
  # 1.ploting a straight line
# involves parameters on the x axis and the y axis
import matplotlib.pyplot as plt
import numpy as np
x = np.array[2,3]
y = np.array[10,6]  # here we pass arrays [2,10], [3,6] to the plot function
plt.plot(x,y)
plt.show()

 #2.plotting without a line 
# we use only makers and you can use shortcut string notation parameter 'o', which means 'rings'.
import matplotlib.pyplot as plt
import numpy as np
x = np.array[2,3]
y = np.array[10,6]  # here we pass arrays [2,10], [3,6] to the plot function
plt.plot(x,y,'o')
plt.show()

    #3.Multiple points
#You can plot as many points as you like, just make sure you have the same number of points in both axis.
#eg draw a line diagrma (1,3) (5,8) (8,7)
import matplotlib.pyplot as plt
import numpy as np
x = np.array[1,5,8]
y = np.array[3,8,7]
plt.plot(x,y)
plt.show()

  #4.default X-points
#if there are no expoints they will take default values 0,1,2,3,4,5
import matplotlib.pyplot as plt
import numpy as np
y = np.array[10,6,5,6,8,9]  
plt.plot(x,y,)
plt.show()

    #4.MARKERS
#You can use the keyword argument marker to emphasize each point with a specified marker:
#Mark each point with a circle
import  sys
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use('Agg')# backend to store figures without displaying

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o') 
plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)# where figure is stored
sys.stdout.flush()# flush the buffer even before system completes running


#marker references
# Marker	Description
# 'o'	Circle	
# '*'	Star	
# '.'	Point	
# ','	Pixel	
# 'x'	X	
# 'X'	X (filled)	
# '+'	Plus	
# 'P'	Plus (filled)	
# 's'	Square	
# 'D'	Diamond	
# 'd'	Diamond (thin)	
# 'p'	Pentagon	
# 'H'	Hexagon	
# 'h'	Hexagon	
# 'v'	Triangle Down	
# '^'	Triangle Up	
# '<'	Triangle Left	
# '>'	Triangle Right	
# '1'	Tri Down	
# '2'	Tri Up	
# '3'	Tri Left	
# '4'	Tri Right	
# '|'	Vline	
# '_'	Hline


   #.Format string fmt
#You can also use the shortcut string notation parameter to specify the marker.
#This parameter is also called fmt, and is written with this syntax:
#marker|line|color
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker='o', linestyle='-', color='r')
plt.show()


#Line Reference
# Line Syntax	Description
# '-'	         Solid line	
# ':'	         Dotted line	
# '--'	         Dashed line	 
# '-.'	         Dashed/dotted line


# color reference 
# Color Syntax	Description
# 'r'	         Red	
# 'g'	         Green	
# 'b'	         Blue	
# 'c'	         Cyan	
# 'm'	         Magenta	
# 'y'	         Yellow	
# 'k'	         Black	
# 'w'	         White


   # Marker Size 
#You can also specify the size of the marker using the markersize keyword or short form ms.
#The size is specified in points, where 1 point is 1/72 of an inch
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array[2,4,5,3,6]
plt.plot(ypoints,ms = 20 , linestyle = '-.',color ='k')


    # Marker color
#You can use the keyword argument markeredgecolor or the shorter mec to set the color of the edge of the markers:
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

#You can use the keyword argument markerfacecolor or the shorter mfc to set the color inside the edge of the markers:
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'w')
plt.show()

# using both mec and mfc
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'w', mec = 'r')
plt.show()


                      #5.MATPLOTLIB LINE
   # line widith 
# we can use the keyword linewidith or lw to show the line widith
# the answer is usually in a floating form
import matplotlib.pyplot as plt
import numpy as np
ylabel = np.array[1,5,7,3,8]
plt.plot(ylabel,lw = 10.5, ls = '--',mec = 'magenta' ,mfc = 'k')
plt.show()

  #multiple lines
# you can draw multiple line by adding plt.plot() functions
import matplotlib.pyplot as plt
import numpy as np
ylabel = np.array[1,5,7,3,8]
xlabel = np.array[5,8,7,4,9]
plt.plot(ylabel)
plt.plot(xlabel)
# you can as well use the plt.plot() function to draw many lines at once
import matplotlib.pyplot as plt
import numpy as np
ylabel = np.array[1,5,7,3,8]
xlabel = np.array[5,8,7,4,9]

plt.plot(xlabel,ylabel)


             #6.MATPLOTLIB Labels And Title
# we use the keyword label() for x and y axis
# for instance xlabel and ylabel
import matplotlib.pyplot as plt
import numpy as np
x = np.array[40,60,90,75,85,88,55]
y = np.array[110,99,120,160,145,150,180]
plt.plot(x,y)
xlabel('diastol')
ylabel('systol')
plt.show()

 # we can add the title to the graph using the title key word
 # the title is usually in a string format
 #we can also add the location of title usong the loc keyword 
 #the title location is usually set to left right or centre
import matplotlib.pyplot as plt
import numpy as np
x = np.array[40,60,90,75,85,88,55]
y = np.array[110,99,120,160,145,150,180]
plt.plot(x,y)
plt.title('Heart Rates',loc='center')
xlabel('diastol')
ylabel('systol')
plt.show()

 #we can also add the font size of the title,xlabel,ylabel using the fontsize keyword
 #we can use the fontdict parameter to add the font size of the title,xlabel and ylabel
import matplotlib.pyplot as plt
import numpy as np
font1 = {'family':'Times New Roman','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
x = np.array[40,60,90,75,85,88,55]
y = np.array[110,99,120,160,145,150,180]
plt.plot(x,y)
plt.title('Heart Rates',loc='center',fontdict=font1)
xlabel('distol',fontdict=font2)
ylabel('systol',fontdict=font2)
plt.show()

             #7.MATPLOLIB GRID
# with pyplot we the keyword grid()
# we can specifiy which axis to have the grid that is xaxis or yaxis
#we can also sttle the grid that is font size color etc
import matplotlib.pyplot as plt
import numpy as np
font1 = {'family':'Times New Roman','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}
x = np.array[40,60,90,75,85,88,55]
y = np.array[110,99,120,160,145,150,180]
plt.plot(x,y)
plt.title('Heart Rates',loc='center',fontdict=font1)
xlabel('distol',fontdict=font2)
ylabel('systol',fontdict=font2)
plt.grid(axis=y,color='green' ,linestyle='-.' ,linewidth=10.5)
plt.show()

          #8.MATPLOTLIB SUBPLOT
#we use the subplot() function to draw multiple plots on one figure
import matplotlib.pyplot as plt
import numpy as np
#plot 1
x = np.array[40,60,90,75,85,88,55]
y = np.array[110,99,120,160,145,150,180]
plt.subplot()
plt.plot(x,y)
#plt 2
v = np.array[1,4,3,2,5,5]
f = np.array[3,4,5,6,7,]
plt.subplot()
plt.plot(v,f)
plt.show()

# we use the subplot function in three layout configurations whereby the first one rep rows,2nd one rep columns and 3rd rep the postn ot index
import matplotlib.pyplot as plt
import numpy as np
#plot 1
x = np.array[40,60,90,75,85,88,55]
y = np.array[110,99,120,160,145,150,180]
plt.subplot(1,2,1)
plt.plot(x,y)
#plt 2
v = np.array[1,4,3,2,5,5]
f = np.array[3,4,5,6,7,]
plt.subplot(1,3,2)
plt.plot(v,f)
plt.show()


# you can also add a title and a suptitle to the subplot figure
# a suptitle is the the general title of the figure
# the title is the specific title fot each figure
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()
 
 
 
               #MATPLOT SCATTER
# we use the scatter() function to draw the scatter plots
# the value on the x axis must correrelate to the other value in the y axis
import matplotlib.pyplot as plt
import numpy as np
x = np.array [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = np.array [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x,y)
plt.show

  #colors
# you can set the color of the scatter plot using the c argument
import matplotlib.pyplot as plt
import numpy as np
x = np.array ([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array ([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x,y ,c='r')

x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
plt.scatter(x, y, c = 'k')

plt.show
   #color each dot
# you set the color of each dot using the arrray of colors
#here the keyword color does not work rather the c argument is used
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array(["red","green","blue","yellow","pink","black","orange","purple","beige","brown","gray","cyan","magenta"])

plt.scatter(x, y, c=colors)

plt.show()

   #color map
# you can use the cmap argument to set the color map of the scatter plot 
# color map contain list of colors ranging from 0 to 100
# 'viridis' is the built colormap keyfunction in matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.show()

 # we can include the color bar in the plot using the plt.colorbar() function
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()

plt.show()
 

       # size of the dots
  #you can change the size of the dots with the s argument.
#Just like colors, make sure the array for sizes has the same length as the arrays for the x- and y-axis:
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes)

plt.show()


   # alpha
   # you can change the transparency of the dots with the alpha argument.
import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes = np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

plt.scatter(x, y, s=sizes , alpha=0.9)

plt.show()