import random
import math as m

def pickPoint():
    """
    Returns a point picked randomly on a sphere in such fashion that if the
    procedure is repeated many times it will result in an equally dense
    distribution on the sphere. Longitude is a random variate drawn from
    unif(0, 2pi) and latitude (interestingly) is a random variate chosen
    corresponding to a probability density function cosine([-pi/2, pi/2]).
    The latter is achieved by integrating cosine on a corresponding domain
    (the result being -sine([-pi/2, pi/2]), choosing an intermediate random
    variate unif(-1, 1), and mapping the intermediate variate through the
    inverse of the integral, which gives us -arcsin([-1, 1])). It's then noticed
    it is as good as arcsin([-1, 1]);
    
    Returned value, point, is a (lon, lat) tuple.
    """
    lon = random.uniform(0, 2 * m.pi)
    lat = m.asin(random.uniform(-1, 1))
    return lon, lat

def sphereDistance(point1, point2):
    """
    Computes the distance from point1 to point2 using so-called harvesine
    formula.

    Returned value, distance, is an angle in radians. 
    """
    dlat = point2[1] - point1[1]
    dlon = point2[0] - point1[0]
    a = pow(m.sin(dlat/2), 2) + m.cos(point1[1]) * m.cos(point2[1]) * pow(m.sin(dlon/2), 2)
    
    return 2 * m.atan2(m.sqrt(a), m.sqrt(1-a))

def moveOnSphere(point, bearing, distance):
    """
    Point is a (lon, lat) pair, bearing is the direction of movement, and
    distance is the distance expressed as an angle, pi being the farthest
    distance.

    Returned value, point, is a (lon, lat) tuple

    The formula is derived using sage, have a look at formulaDerivation.py
    and README.md  
    """
    #newLon = m.pi - m.acos((m.cos(point[0]) * m.cos(bearing) * m.sin(distance) * m.sin(point[1]) - m.cos(distance) * m.cos(point[0]) * m.cos(point[1]) + m.sin(distance) * m.sin(point[0]) * m.sin(bearing)) / m.sqrt(-1 * m.cos(point[1]) ** 2 * m.cos(bearing) ** 2 * m.sin(distance) ** 2 - 2 * m.cos(distance) * m.cos(point[1]) * m.cos(bearing) * m.sin(distance) * m.sin(point[1]) - m.cos(distance) ** 2 * m.sin(point[1]) ** 2 + 1))
    newLat = m.asin(m.cos(point[1]) * m.cos(bearing) * m.sin(distance) + m.cos(distance) * m.sin(point[1]))
    newLon = point[0] + m.atan2(m.sin(bearing) * m.sin(distance) * m.cos(point[1]), m.cos(distance) - m.sin(point[1]) * m.sin (newLat))
    return newLon, newLat

def polarToXYZ(point):
    """
    Translate point from geographic coordinates to cartesian, where X is
    pointing eastwards, Y is pointing north and Z is pointing roughly towards
    Africa.
    """
    X = m.sin(point[0]) * m.cos(point[1])
    Y = m.sin(point[1])
    Z = m.cos(point[0]) * m.cos(point[1])
    return (X, Y, Z)
rtd = (180/m.pi)
dtr = (m.pi/180)
