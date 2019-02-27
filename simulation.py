import numpy as np
from radiation import solarRadiation

#Params
MINIMUM_LIGHT=101.95 #in Watts


def simulate(LATITUDE, DAYLIGHT_SAVINGS, SAMPLES):
    #LATITUDE in degrees from equator
    #DAYLIGHT_SAVINGS=False|True -> Simulació amb canvi d'horari?
    wakingTime=np.random.normal(420.39, 40.7, SAMPLES) #in minutes
    awakeHours=np.random.normal(24*60-461.4, 72.1, SAMPLES) #in minutes
    energy=0
    for i in range(SAMPLES): #Loop over samples
        for d in range(365): #Loop over days in year
            for hour in range(24):
                m=hour*60
                if m>wakingTime[i] and m<wakingTime[i]+awakeHours[i]: #Awake?
                    radiation=solarRadiation((m - (60 if (DAYLIGHT_SAVINGS and d>90 and d<300) else 0))%(24*60), d+(1 if (m>(24*60)) else 0), LATITUDE)
                    if radiation<MINIMUM_LIGHT: #Enough light?
                        energy+=(MINIMUM_LIGHT-radiation)*60*60
        print("sample %d done"%i)

    energy=energy/SAMPLES
    return energy

if __name__ == "__main__":
    print(simulate(41.3818, False, 1000)) #Latitud de Barcelona
