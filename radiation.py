import numpy as np

def cos(angle):
    return np.cos(np.deg2rad(angle))

def sin(angle):
    return np.sin(np.deg2rad(angle))

def arcsin(val):
    return np.degrees(np.arcsin(val))

def solarRadiation(timeOfDay, day, latitude):
    declination=arcsin(sin(-23.44) * cos((360/365.24)*(day+10)+(360/np.pi)* 0.0167 * sin((360/365.24)*(day-2))))
    radiation=1367*0.53*(sin(declination)*sin(latitude)+cos(declination)*cos(latitude)*cos(((timeOfDay-12*60)/(24*60))*360))
    return radiation if radiation>=0 else 0
