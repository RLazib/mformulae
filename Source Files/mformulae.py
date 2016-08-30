import math

pi = 3.141592654

c = 299729458

def m2yd(m):
    return m / 0.9144

def yd2m(yd):
    return yd * 0.9144

def cm2in(cm):
    return cm / 2.54

def in2cm(inch):
    return inch * 2.54

def km2mi(km):
    return km / 1.609

def mi2km(mi):
    return mi * 1.609

def areasphere(rad):
    return 4 * math.pi * rad **2

def volsphere(rad):
    return (4 * math.pi * rad **3)/3

def areacone(rad, slant):
    return math. pi * rad * slant + math.pi * rad **2

def volcone(rad, hght):
    return math.pi * rad ** 2 * hght

def areacyl(rad, hght):
    return 2 * math.pi * rad ** 2 + 2 * math.pi * rad * hght

def volcyl(rad, hght):
    return math.pi * rad ** 2 * hght

def arearecprism(l, w, h):
    return 2 * (w * h + l * w + l * h)

def volrecprism(l, w, h):
    return l * w * h

def areasqrpyramid(slant, sl):
    2 * sl * slant + sl **2

def volsqrpyramid(hght, sl):
    (sl ** 2 * hght) / 3

def areatriprism(b, h, s, l):
    b * h + 2 * l * s + l * b

def voltriprism(b, h, l):
    (b * h * l) / 2

def areatripyramid(sl, slant, bth):
    return ((sl * bth)/2) + (((sl * slant) / 2) * 3)

def voltripyramid(hght, sl, bth):
    return (((sl * bth)/2) * hght) / 3

def tangent_deg(n):
    return math.tan(math.radians(n))

def sine_deg(n):
    return math.sin(math.radians(n))

def cosine_deg(n):
    return math.cos(math.radians(n))

def tangent_rad(n):
    return math.tan(n)

def sine_rad(n):
    return math.sin(n)

def cosine_ran(n):
    return math.cos(n)

def findangletan(opp, adj):
    return math.degrees(math.atan(opp / adj))

def findanglesin(opp, hyp):
    return math.degrees(math.asin(opp / hyp))

def findanglecos(adj, hyp):
    return math.degrees(math.acos(adj / hyp))

def masstoenergy(mass, velocity):
    return (mass * c ** 2) ** 2 + (velocity * c) ** 2

def density(mass, vol):
    return mass / vol

def pressure(force, area):
    return force / area

def getwatts(amps, volts):
    return amps * volts

def getamps(watts, volts):
    return watts / volts

def getvolts(watts, amps):
    return watts / amps


    
    
    
    

    
