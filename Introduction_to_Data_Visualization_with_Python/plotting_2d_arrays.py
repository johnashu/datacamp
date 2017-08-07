import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from io import BytesIO


csv_file = np.genfromtxt('percent-bachelors-degrees-women-usa.csv', delimiter=',')
df = pd.read_csv('percent-bachelors-degrees-women-usa.csv')

print(df.columns.get_loc('Education'))

auto_csv = np.genfromtxt('auto-mpg.csv', delimiter=',')
df1 = pd.read_csv('auto-mpg.csv')
print(df1.columns.get_loc('hp'))

mpg = auto_csv[:,0]
hp = auto_csv[:,3]

year = csv_file[:,0]
physical_sciences = csv_file[:,14]
computer_science = csv_file[:,7]
health = csv_file[:,12]
education = csv_file[:,8]


u = np.linspace(-2, 2, 3)

v = np.linspace(-1, 1, 5)

X, Y = np.meshgrid(u, v)

Z = X ** 2/25 + Y ** 2/4

print(X)
print(Y)
print(Z)

print('Z:\n', Z)
plt.set_cmap('gray')
plt.pcolor(Z)
plt.show()





u = np.linspace(-2, 2, 41)
v = np.linspace(-1, 1, 21)

# Generate 2-D arrays from u and v: X, Y
X,Y = np.meshgrid(u, v)

# Compute Z based on X and Y
Z = np.sin(3*np.sqrt(X**2 + Y**2)) 

plt.pcolor(Z)
plt.show()

plt.savefig('sine_mesh.png')




u = np.linspace(-2, 2, 65)
v = np.linspace(-1, 1, 33)

X, Y = np.meshgrid(u, v)
Z = X ** 2/25 + Y ** 2/4

plt.pcolor(X, Y, Z, cmap='autumn')
plt.colorbar()
plt.axis('tight')
#plt.show()

plt.contour(X, Y, Z, 30, cmap='autumn')
#plt.show()

plt.contourf(X, Y, Z, 30, cmap='autumn')
#plt.show()

plt.subplot(2,2,1)
plt.contour(X, Y, Z)

plt.subplot(2,2,2)
plt.contour(X, Y, Z, 100)

plt.subplot(2,2,3)
plt.contourf(X, Y, Z)

plt.subplot(2,2,4)
plt.contourf(X, Y, Z, 100)

plt.tight_layout()
plt.show()


plt.subplot(2,2,1)
plt.contourf(X,Y,Z,20, cmap='viridis')
plt.colorbar()
plt.title('Viridis')

plt.subplot(2,2,2)
plt.contourf(X,Y,Z,20, cmap='gray')
plt.colorbar()
plt.title('Gray')

plt.subplot(2,2,3)
plt.contourf(X, Y, Z, 20, cmap='autumn')
plt.colorbar()
plt.title('Autumn')

plt.subplot(2,2,4)
plt.contourf(X, Y, Z, 20, cmap='winter')
plt.colorbar()
plt.title('Winter')

plt.tight_layout()
plt.show()




plt.hist2d(hp, mpg, bins=(20,20), range=((40, 235), (8, 48)))
plt.colorbar()

plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hist2d() plot')
plt.show()



plt.hexbin(hp, mpg, gridsize=(15, 12), extent=(40, 235, 8, 48))

plt.colorbar(
plt.xlabel('Horse power [hp]')
plt.ylabel('Miles per gallon [mpg]')
plt.title('hexbin() plot')
plt.show()


img = plt.imread('sunflower.jpg')

plt.imshow(img)

plt.axis('off')
plt.show()

collapsed = img.mean(axis=2)

print(collapsed.shape)

plt.set_cmap('gray')
plt.imshow(collapsed, cmap='gray')
plt.axis('off')
plt.show()

uneven = collapsed[::4, ::2]
print(uneven.shape)
plt.imshow(uneven)
plt.axis('off')
plt.show()

plt.imshow(uneven, aspect=2.0)
plt.axis('off')
plt.show()

plt.imshow(uneven, cmap='gray', extent=(90,640,0,480))
plt.axis('off')
plt.show()

image = plt.imread('sunflower.jpg')

pmin, pmax = image.min(), image.max()
print("The smallest & largest pixel intensities are %d & %d." % (pmin, pmax))

rescaled_image = 256*(image - pmin) / (pmax - pmin)
print("The rescaled smallest & largest pixel intensities are %.1f & %.1f." % 
      (rescaled_image.min(), rescaled_image.max()))


plt.subplot(2,1,1)
plt.title('original image')
plt.axis('off')
plt.imshow(image)

plt.subplot(2,1,2)
plt.title('rescaled image')
plt.axis('off')
plt.imshow(rescaled_image)

plt.show()
