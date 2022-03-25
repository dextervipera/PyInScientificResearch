# https://www.youtube.com/watch?v=UO98lJQ3QGI

from matplotlib import pyplot as plt
#from snipplets import dev_x, dev_y

print (plt.style.available)

#plt.style.use('seaborn-darkgrid')
plt.xkcd()

# Median Developer Salaries by Age
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200,
         56000, 62316, 64928, 67317, 68748, 73752]


# Median Python Developer Salaries by Age
py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
py_dev_y = [45372, 48876, 53850, 57287, 63016,
            65998, 70003, 70000, 71496, 75370, 83640]
#plt.grid(True)

plt.plot(dev_x, dev_y, 
         label='All devs')


plt.plot(py_dev_x,py_dev_y, 'or--', label='Py devs')


plt.title('Median sallary by age')

# plt.legend(['dev','Py dev'])
plt.legend()
plt.xlabel('Age')
plt.ylabel('Sallary [USD]')



plt.tight_layout()
plt.savefig('plot.png')

plt.show()