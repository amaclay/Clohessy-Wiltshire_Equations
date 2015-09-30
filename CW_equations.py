from math import *

#Constants
MTOFT = 2.54*12/100
RTD = 180/pi
MU = 398600000000000
RE = 6378145

class Equations:
    def __init__(self):
                
# Initialize output table
        self.outputTable = [['t(s)','t(m)','x(m)','y(m)','z(m)','xd(m)','yd(m)','zd(m)']]

    def calculate(self, entry):

# Store entered values
        self.altitude = float(entry[0])
        self.fx = float(entry[1])
        self.fy = float(entry[2])
        self.fz = float(entry[3])
        self.xd = float(entry[4])
        self.yd = float(entry[5])
        self.zd = float(entry[6])
        self.x  = float(entry[7])
        self.y  = float(entry[8])
        self.z  = float(entry[9])

# Initial Calculations
        self.metersPerFoot = 2.54*12/100        # m/ft
        self.rtd = 180/pi                       # deg/rad
        self.mu = 398600000000000               # m^3/s^2
        self.Re = 6378145                       # m
        self.r = self.altitude * 1000 + self.Re # km
        self.w = sqrt(MU/(self.r**3))           # rad/s
        self.rev = self.w * 86400 / (2*pi)      # rev/day
        self.p = 2 * pi / self.w                # sec
        self.q = self.p / 60                    # min
        
##        self.drift_rate = (self.xOut[51] + self.xOut[52]) / 2 / self.p

        for i in range(0,121):
            j = i*120

            self.outputTable += [[j, #t(s)
                int(j/60), #t(m)
                round((self.xd/self.w)*sin(self.w*j)-(3*self.x+2*self.yd/self.w)*cos(self.w*j)+(4*self.x+2*self.yd/self.w), 2), #x
                round((6*self.x+4*self.yd/self.w)*sin(self.w*j)+(2*self.xd/self.w)*cos(self.w*j)-(6*self.w*self.x+3*self.yd)*j+(self.y-2*self.xd/self.w), 2), #y
                round(self.z*cos(self.w*j)+(self.zd/self.w)*sin(self.w*j), 2), #z
                round(self.xd*cos(self.w*j)+(3*self.w*self.x+2*self.yd)*sin(self.w*j), 2), #xd
                round((6*self.w*self.x+4*self.yd)*cos(self.w*j)-2*self.xd*sin(self.w*j)-(6*self.w*self.x+3*self.yd), 2), #yd
                round(-self.z*self.w*sin(self.w*j)+self.zd*cos(self.w*j), 2)]] #yd

        return self.outputTable


