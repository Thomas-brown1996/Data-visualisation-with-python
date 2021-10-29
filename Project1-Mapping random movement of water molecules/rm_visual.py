import matplotlib.pyplot as plt
from randommolecule import Randomdroplet

#make a random movement
rm = Randomdroplet(30_000)
rm.fill_droplets()

#plot points in movement
plt.style.use('classic')
fig, ax = plt.subplots()
point_numbers =range(rm.num_points)
ax.scatter(rm.x_values, rm.y_values, c=point_numbers, cmap=plt.cm.Blues,
edgecolor='none', s=1)

ax.scatter(rm.x_values, rm.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none',
     s=15)

#highlight first and last points
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rm.x_values[-1], rm.y_values[-1], c='red', edgecolors='none',
        s=100)
    
    #can remove axis if wanted
ax.get_xaxis().set_visible(True)
ax.get_yaxis().set_visible(True)

plt.show()

 