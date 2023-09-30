import openpnm as op  
import numpy as np
import matplotlib.pyplot as plt
op.visualization.set_mpl_style()


# Cubic
# -------
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
# ---------------
# We can make cubic templates with more complex shape 
# In general we need to make an 'boolean image' (NB: Not sure what this is)

# Some boolean images are preprogrammed using functions in the topotools module 
im = op.topotools.template_cylinder_annulus(z=3, r_outer=8, r_inner=3)
pn = op.network.CubicTemplate(template=im)  # load network from template image instead

# Plot it
ax = op.visualization.plot_coordinates(network=pn)
ax = op.visualization.plot_connections(network=pn, ax=ax)




# Other Cubic Lattices 
# ------------
# There are several other cubic networks instances 
# These pack extra pores into the same amount of space 

# Face centred cubic networks
fcc = op.network.FaceCenteredCubic(shape=[4, 4, 4], spacing=1e-5)
ax = op.visualization.plot_connections(network=fcc)
ax = op.visualization.plot_coordinates(network=fcc, ax=ax)

# Body centred cubic networks 
bcc = op.network.BodyCenteredCubic(shape=[4,4,4], spacing=1e-5)
ax = op.visualization.plot_coordinates(network=bcc)
ax = op.visualization.plot_connections(network=bcc, ax=ax)

# Can use plot_coordinates and plot_connections 
# to isolate pores and throats with particular labels 
print(bcc)

ax = op.visualization.plot_connections(network=bcc, throats=bcc.throats("body_to_body"))
ax = op.visualization.plot_coordinates(network=bcc, pores=bcc.pores("body"), ax=ax)
ax = op.visualization.plot_connections(network=bcc, throats=bcc.throats("corner_to_body"), ax=ax, color="green")
ax = op.visualization.plot_coordinates(network=bcc, pores=bcc.pores("corner"), ax=ax, color="orange")




# Random networks
# ------------
# Network is stored in general way 
# Therefore storing random networks is simple 

# Voronoi
pn = op.network.Voronoi(shape=[1,1,1], points=4)

ax = op.visualization.plot_coordinates(network=pn)
ax = op.visualization.plot_connections(network=pn, ax=ax)

# Delaunay
pn = op.network.Delaunay(shape=[1,1,1], points=4)

ax = op.visualization.plot_coordinates(network=pn)
ax = op.visualization.plot_connections(network=pn, ax=ax)

# Delaunay Voronoi Dual
pn = op.network.DelaunayVoronoiDual(shape=[1,1,1], points=4)

ax = op.visualization.plot_coordinates(network=pn)
ax = op.visualization.plot_connections(network=pn, ax=ax)




# Imported networks 
# ------------
# Can handle network generated from an image 
# Basic idea is op needs [x,y,z] coordinates 
# of pores and which pores are connected to 
# which others

# Generated network 
coords = [
    [0,0,0],
    [1,0,0],
    [1,1,0],
    [0,1,0]
]

conns = [
    [0,1],
    [1,2],
    [2,3],
    [0,3]
]

diam_pores = [
    1,
    2,
    1,
    3
]

diam_throats = [
    0.5,
    0.2,
    0.8,
    0.7
]

pn = op.network.Network(coords=coords, conns=conns)
ax = op.visualization.plot_coordinates(network=pn)
ax = op.visualization.plot_connections(network=pn, ax=ax)

# Add data to pores and throats using labels 
# Note that the network is a dictionary 
# with two propertis: pore and throat 
pn["pore.diameter"]  = diam_pores
pn["throat.diameter"] = diam_throats




# Try an alternative way... 
# 
# Make a blank network 
pn_alt = op.network.Network()

# Then add properties to pores and throats
pn_alt["pore.coords"]   = coords

# pn_alt["throat.conns"]  = conns
# NB: Above will produce an error because needs numpy array
# Below will work
pn_alt["throat.conns"]  = np.array(conns)


pn_alt["pore.diameter"] = diam_pores
pn_alt["throat.diameter"] = diam_throats


# We can plot using network properties 
ax = op.visualization.plot_connections(network=pn_alt, size_by=pn["throat.diameter"], linewidth=4)
# ax = op.visualization.plot_connections(network=pn_alt, color_by=pn["throat.diameter"], ax=ax)

ax = op.visualization.plot_coordinates(network=pn_alt,  size_by=pn["pore.diameter"], markersize=500, ax=ax)
# ax = op.visualization.plot_coordinates(network=pn_alt, color_by=pn["pore.diameter"], ax=ax)



# NB: op.io provides lots of functions to extract networks from 
# different file formats
plt.show()
