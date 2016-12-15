import numpy as n
import os

try:
    argv, expt, num_el_fine_th, dt, eccen = argv
    expt = int(expt)
    d = n.genfromtxt('ExptParameters.dat', delimiter=',')
    th, ODg, eccen = d[ d[:,0]==expt, 1:]   
except:
    ID = '0.875' # Inner Radius
    tg = '0.038'
    num_el_fine_th = 12 # Num elements thru the test section thicknes
    dt = .01

Lg = '0.2'
Ltop = '1.3'  # Length of thick section above radius/chamf
ODtop = '0.98425'    # Radius of thick section    
R = '0.125'    # Radius of chamf
    
### Nodes
os.system('python Nodes.py {} {:.1f} {.5f} {.4f} {:.4f} {.3f} {:d} {.3f}'.format(
                Lg, Ltop, ODtop, ID, tg, R, num_el_fine_th, dt)
