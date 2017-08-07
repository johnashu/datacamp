import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from io import BytesIO


csv_file = np.genfromtxt('percent-bachelors-degrees-women-usa.csv', delimiter=',')
df = pd.read_csv('percent-bachelors-degrees-women-usa.csv')

print(df.columns.get_loc('Education'))


year = csv_file[:,0]
physical_sciences = csv_file[:,14]
computer_science = csv_file[:,7]
health = csv_file[:,12]
education = csv_file[:,8]

"""
plt.plot(year, physical_sciences, color='blue')
plt.plot(year, computer_science, color='red')
plt.show()

###

plt.axes([0.05, 0.05, 0.425, 0.9])
plt.plot(year, physical_sciences, color='blue')

plt.axes([0.525, 0.05, 0.425, 0.9])
plt.plot(year, computer_science, color='red')

plt.show()

###

plt.subplot(1, 2, 1)

plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')

plt.subplot(1, 2, 2)
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

# Use plt.tight_layout() to improve the spacing between subplots
plt.tight_layout()
plt.show()


###

plt.subplot(2, 2, 1)
plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')

plt.subplot(2, 2, 2)

plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

plt.subplot(2, 2, 3)

plt.plot(year, health, color='green')
plt.title('Health Professions')

plt.subplot(2, 2, 4)

plt.plot(year, education, color='yellow')
plt.title('Education')

plt.tight_layout()
plt.show()

###

plt.plot(year,computer_science, color='red') 
plt.plot(year, physical_sciences, color='blue')

plt.xlabel('Year')
plt.ylabel('Degrees awarded to women (%)')


plt.xlim(1990, 2010)

plt.ylim(0, 50)

plt.title('Degrees awarded to women (1990-2010)\nComputer Science (red)\nPhysical Sciences (blue)')
plt.show()

plt.savefig('xlim_and_ylim.png')


plt.plot(year,computer_science, color='blue')
plt.plot(year, physical_sciences,color='red')

plt.axis((1990, 2010, 0, 50))

plt.show()

plt.savefig('axis_limits.png')




plt.plot(year, computer_science, color='red', label='Computer Science') 


plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')

plt.legend(loc='lower center')

plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()



plt.plot(year, computer_science, color='red', label='Computer Science') 
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')
plt.legend(loc='bottom right')

cs_max = computer_science.max()
yr_max = year[computer_science.argmax()]

plt.annotate('Maximum', xy=(yr_max, cs_max), xytext=(yr_max+5, cs_max+5), arrowprops=dict(facecolor='black'))

plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()



plt.plot(year, computer_science, color='red', label='Computer Science') 
plt.plot(year, physical_sciences, color='blue', label='Physical Sciences')
plt.legend(loc='bottom right')

cs_max = computer_science.max()
yr_max = year[computer_science.argmax()]

# Add a black arrow annotation
plt.annotate('Maximum', xy=(yr_max, cs_max), xytext=(yr_max+5, cs_max+5), arrowprops=dict(facecolor='black'))

plt.xlabel('Year')
plt.ylabel('Enrollment (%)')
plt.title('Undergraduate enrollment of women')
plt.show()

"""

plt.style.use('ggplot')

plt.subplot(2, 2, 1) 


plt.plot(year, physical_sciences, color='blue')
plt.title('Physical Sciences')

plt.subplot(2, 2, 2)
plt.plot(year, computer_science, color='red')
plt.title('Computer Science')

cs_max = computer_science.max()
yr_max = year[computer_science.argmax()]
plt.annotate('Maximum', xy=(yr_max, cs_max), xytext=(yr_max-1, cs_max-10), arrowprops=dict(facecolor='black'))

plt.subplot(2, 2, 3)
plt.plot(year, health, color='green')
plt.title('Health Professions')

plt.subplot(2, 2, 4)
plt.plot(year, education, color='yellow')
plt.title('Education')

plt.tight_layout()
plt.show()