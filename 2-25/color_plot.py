import numpy as np
import matplotlib.pyplot as plt
from netCDF4 import Dataset
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

w_file = '/Users/brownscholar/Desktop/InternGit/ocean-motion-2021/2-25/test/ss1a2ww.gr' # fix this
w = open(w_file, "r")

#open netcdf file
original_data = Dataset('/Users/brownscholar/Desktop/BridgeUp_Year2/n-atlantic-2018.nc')

#get latitude and longitude from netcdf file: 
#lat = original_data.variable['lat'][:]
#lon = original_data.variable['lon'][:]

num_lat = 158
num_lon = 122
levels = 1

# make empty numpy array of shape lat, lon depth shape for storing w:
array = np.zeros((1,158,122))


# use a loop to read w_file into the variable 
#(skip first two lines of the file)
w.readline()
w.readline()
for x in range(0,levels):
	for y in range(0,num_lat):
		for z in range(0,num_lon):
			array[x,y,z] = w.readline()
	


#this stuff defines the colorspace (we can google colormaps to learn more if we want to)
top = cm.get_cmap('Blues_r', 128)
bottom = cm.get_cmap('Reds', 128)

newcolors = np.vstack((top(np.linspace(0, 1, 128)),
                       bottom(np.linspace(0, 1, 128))))
newcmp = ListedColormap(newcolors, name='RedBlue')




#now use the following function to plot your data:
#function to make colorplot is:
p = plt.pcolormesh(array[0,2:-2,2:-2],cmap = newcmp) #where V is the numpy array with the data
plt.show()

# you can use these to add the x and y ticks to your plot:
# I am happy to talk to you about why this works
#plt.xticks(np.arange(0,num_lon,10),lon[::10])
#plt.yticks(np.arange(0,num_lat,10),lat[::10])


