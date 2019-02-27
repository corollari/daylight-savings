import numpy as np

# Params
SAMPLES=100
LATITUDE=0 #in degrees from equator
MINIMUM_LIGHT=0 #in Watts
DAYLIGHT_SAVINGS=False #Simulació amb canvi d'horari?


def cos(angle):
    return np.cos(np.deg2rad(angle))

def sin(angle):
    return np.sin(np.deg2rad(angle))

def arcsin(val):
    return np.degrees(np.arcsin(val))

def solarRadiation(timeOfDay, day, latitude):
    declination=arcsin(sin(-23.44) * cos((360/365.24)*(day+10)+(360/np.pi)* 0.0167 * sin((360/365.24)*(day-2))))
    return 1367*0.53*(sin(declination)*sin(latitude)+cos(declination)*cos(latitude)*cos(((timeOfDay-12*60)/(24*60))*360))
wakingTime=np.random.normal(420.39, 40.7, SAMPLES) #in minutes
awakeHours=np.random.normal(24*60-461.4, 72.1, SAMPLES) #in minutes

energy=0

for i in range(SAMPLES): #Loop over samples
    for d in range(365): #Loop over days in year
        for m in range(24): # Loop over minutes in 2 days (some people stay awake after 12pm into the following day)
            if m>wakingTime[i] and m<wakingTime[i]+awakeHours[i]: #Awake?
                radiation=solarRadiation((m + (60 if DAYLIGHT_SAVINGS else 0))%(24*60), d+(1 if (m>(24*60)) else 0), LATITUDE)
                if radiation<MINIMUM_LIGHT: #Enough light?
                    energy+=(MINIMUM_LIGHT-radiation)*60
    print("sample %d done"%i)

energy=energy/SAMPLES
print(energy)
