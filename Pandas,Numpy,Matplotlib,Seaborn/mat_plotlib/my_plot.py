import matplotlib.pyplot as plt
import numpy as np

print()
x= np.linspace(-10,10,100)
print('X-axis:',x)

print()

y= x**2
print('Y-axis:',y)

print()
z= np.cos(x)
print('Z-axis:',y)

'''plt.plot(x,y,'r')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("y vs x")
plt.show()'''

#Object Oriented Method

fig = plt.figure()

axis1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axis2 = fig.add_axes([0.65, 0.66, 0.2, 0.2])
axis3 = fig.add_axes([0.65, 0.2, 0.2, 0.2])

axis1.plot(y,x,label='x')
axis1.plot(y,np.sin(x),label='sin(x)')
axis1.set_xlabel('y values')
axis1.set_ylabel('x values')
axis1.set_title('x vs y')
axis1.legend(loc = 3)

axis2.plot(x,y,'-')
axis2.set_xlabel('x values', fontsize=9)
axis2.set_ylabel('y values', fontsize=9)
axis2.set_title('y vs x', fontsize=9)
axis2.tick_params(labelsize=9)

axis3.plot(x,z,'--')
axis3.set_xlabel('x values', fontsize=9)
axis3.set_ylabel('z values', fontsize=9)
axis3.set_title('z vs x', fontsize=9)
axis3.tick_params(labelsize=9)
plt.show()
