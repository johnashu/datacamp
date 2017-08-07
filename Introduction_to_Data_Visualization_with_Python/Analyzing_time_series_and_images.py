import pandas as pd
import numpy as np


csv_file = np.genfromtxt(
    'stocks.csv', delimiter=',')
df = pd.read_csv('stocks.csv')

date = csv_file[:, 0]
aapl = csv_file[:, 1]
ibm = csv_file[:, 2]
csco = csv_file[:, 3]
msft = csv_file[:, 4]


print(df.columns.get_loc('AAPL'))

auto_csv = np.genfromtxt('auto-mpg.csv', delimiter=',')
df1 = pd.read_csv('auto-mpg.csv')
print(df1.columns.get_loc('hp'))

mpg = auto_csv[:, 0]
hp = auto_csv[:, 3]

auto = df1

tips_csv = pd.read_csv('tips.csv')
tips = tips_csv

import seaborn as sns
import matplotlib.pyplot as plt

plt.plot(aapl, color='blue', label='AAPL')
plt.plot(ibm, color='green', label='IBM')
plt.plot(csco, color='red', label='CSCO')
plt.plot(msft, color='magenta', label='msft')

plt.legend(loc='upper left')

plt.xticks(rotation=60)
plt.show()

"""

plt.subplot(2,1,1)
plt.xticks(rotation=45)
plt.title('AAPL: 2001 to 2011')
plt.plot(aapl, color='blue')

view = aapl['2007':'2008']

plt.subplot(2,1,2)
plt.xticks(rotation=45)
plt.title('AAPL: 2007 to 2008')
plt.plot(view, color='black')
plt.tight_layout()
plt.show()




view = aapl['2007-11':'2008-04']
plt.subplot(2, 1, 1)
plt.xticks(rotation=45)
plt.title('AAPL: Nov. 2007 to Apr. 2008')
plt.plot(view, color='red')

view = aapl['2008-01']

# Plot the sliced series in the bottom subplot in green
plt.subplot(2, 1, 2)
plt.xticks(rotation=45)
plt.title('AAPL: Jan. 2008')
plt.plot(view, color='green')

plt.tight_layout()
plt.show()



view = aapl['2007-11':'2008-04']

plt.plot(aapl)
plt.xticks(rotation=45)
plt.title('AAPL: 2001-2011')

plt.axes([0.25, 0.5, 0.35, 0.35])

plt.plot(view, color='red')
plt.xticks(rotation=45)
plt.title('2007/11-2008/04')
plt.show()




plt.subplot(2, 2, 1)
plt.plot(mean_30, 'green')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('30d averages')

plt.subplot(2, 2, 2)
plt.plot(mean_75, 'red')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('75d averages')

plt.subplot(2, 2, 3)
plt.plot(mean_125, 'magenta')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('125d averages')

plt.subplot(2, 2, 4)
plt.plot(mean_250, 'cyan')
plt.plot(aapl, 'k-.')
plt.xticks(rotation=60)
plt.title('250d averages')

plt.show()

"""

orig = plt.imread('moon.jpg')
pixels = orig.flatten()

plt.hist(pixels, bins=256, range=(0, 256),
         normed=True, color='blue', alpha=0.3)
plt.show()

minval, maxval = orig.min(), orig.max()

print(minval, maxval)


image = plt.imread('640px-Unequalized_Hawkes_Bay_NZ.jpg')

plt.subplot(2, 1, 1)
plt.title('Original image')
plt.axis('off')
plt.imshow(image, cmap='gray')

pixels = image.flatten()

plt.subplot(2, 1, 2)
plt.xlim((0, 255))
plt.title('Normalized histogram')
plt.hist(pixels, bins=64, color='red', alpha=0.4, range=(0, 256), normed=True)
plt.show()

plt.subplot(2, 1, 1)
plt.imshow(image, cmap='gray')
plt.title('Original image')
plt.axis('off')


plt.subplot(2, 1, 2)
pdf = plt.hist(pixels, bins=64, range=(0, 256), normed=False,
               color='red', alpha=0.4)
plt.grid('off')

plt.twinx()


cdf = plt.hist(pixels, bins=64, range=(0, 256),
               normed=True, cumulative=True,
               color='blue', alpha=0.4)

plt.xlim((0, 256))
plt.grid('off')
plt.title('PDF & CDF (original image)')
plt.show()


cdf, bins, patches = plt.hist(pixels, bins=256, range=(0,256), normed=True, cumulative=True)
new_pixels = np.interp(pixels, bins[:-1], cdf*255)

new_image = new_pixels.reshape(image.shape)

plt.subplot(2,1,1)
plt.title('Equalized image')
plt.axis('off')
plt.imshow(new_image, cmap='gray')

plt.subplot(2,1,2)
pdf = plt.hist(new_pixels, bins=64, range=(0,256), normed=False,
               color='red', alpha=0.4)
plt.grid('off')

plt.twinx()
plt.xlim((0,256))
plt.grid('off')

plt.title('PDF & CDF (equalized image)')

cdf = plt.hist(new_pixels, bins=64, range=(0,256),
               cumulative=True, normed=True,
               color='blue', alpha=0.4)
plt.show()

image = plt.imread('hs-2004-32-b-small_web.jpg')

plt.subplot(2,1,1)
plt.title('Original image')
plt.axis('off')
plt.imshow(image)

red, blue, green = image[:,:,0], image[:,:,1], image[:,:,2]

red_pixels = red.flatten()
blue_pixels = blue.flatten()
green_pixels = green.flatten()

plt.subplot(2,1,2)
plt.title('Histograms from color image')
plt.xlim((0,256))
plt.hist(red_pixels, bins=64, normed=True, color='red', alpha=0.2)
plt.hist(blue_pixels, bins=64, normed=True, color='blue', alpha=0.2)
plt.hist(green_pixels, bins=64, normed=True, color='green', alpha=0.2)

plt.show()

image = plt.imread('hs-2004-32-b-small_web.jpg')

red, blue, green = image[:,:,0], image[:,:,1], image[:,:,2]
red.pixels = red.flatten()
blue.pixels = blue.flatten()
green.pixels = green.flatten()

plt.subplot(2, 2, 1)
plt.grid('off')
plt.xticks(rotaion=60)
plt.xlabel('red')
plt.ylabel('green')
plt.hist2d(red_pixels, green_pixels, bins=(32,32))

plt.subplot(2, 2, 2)
plt.grid('off')
plt.xticks(rotaion=60)
plt.xlabel('green')
plt.ylabel('blue')
plt.hist2d(green_pixels, blue_pixels, bins=(32,32))

plt.subplot(2, 2, 3)
plt.grid('off')
plt.xticks(rotation=60)
plt.xlabel('blue')
plt.ylabel('red')
plt.his2d(blue_pixels, red_pixels, bins=(32,32))

plt.show()




