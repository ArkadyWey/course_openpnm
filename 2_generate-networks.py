import openpnm as op  
import numpy as np
import matplotlib.pyplot as plt
op.visualization.set_mpl_style()

# Create a cubic network 
pn = op.network.Cubic(shape=[2,2,2], spacing=1e-5)

# Plot network
ax = op.visualization.plot_coordinates(pn)
ax = op.visualization.plot_connections(pn,ax=ax)

# Make another one that is 8,4,2
pn = op.network.Cubic(shape=[8,4,2], spacing=[10e-5,5e-5,4e-5])

# Plot it 
ax = op.visualization.plot_coordinates(pn)
ax = op.visualization.plot_connections(pn, ax=ax)

# Make another one with more connections 
pn = op.network.Cubic(shape=[4,4,4], spacing=[1e-5,1e-5,1e-5], connectivity=26)

# Plot it 
ax = op.visualization.plot_coordinates(network=pn)
ax = op.visualization.plot_connections(network=pn, ax=ax)

# Trim the network using the topotools module and its trim function
pn = op.network.Cubic(shape=[4,4,4],spacing=1e-5,connectivity=26)

np.random.seed(0)
drop = np.random.randint(0, pn.Nt, 500) # will drop numbers between 0 and number of throats from a list of 500 of them

op.topotools.trim(network=pn, throats=drop)

ax = op.visualization.plot_coordinates(network=pn)
ax = op.visualization.plot_connections(network=pn, ax=ax)
#plt.show()

# Print details about network
print(pn)

# Using network.pores and network.throats - the two 'properties' that all networks MUST have 
Ps = pn.pores()
print("The following is a list of all pores: ", Ps) # pores are nodes

Ps_back = pn.pores("back")
print("The following pores are labelled with 'back': {}".format(Ps_back))

Ps_left = pn.pores("left")
print("The following pores are labelled with 'left': {}".format(Ps_left))

Ps_back_left = pn.pores(["back","left"])
print("The following pores are labelled with 'back' and 'left': {}".format(Ps_back_left))
# NB: I don't understand this - surely this should be an interection of the other two lists?!

Ts_surface = pn.throats("surface")
print("The following throats are labelled 'surface': {}".format(Ts_surface))


# Cubic Templates 
