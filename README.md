# Daylight Savings Mathematical Model
> Modelling populations to decide whether daylight savings make sense

# Set up
```bash
virtualenv venv
. venv/bin/activate
pip install -r requirements
```

# Run simulations
## Simulate yearly energy consumption per person in Barcelona
```
python simulate.py
```

## Plot yearly energy savings over latitude 
```
python plotLatitude.py
```

## Plot sun radiation over 24 hours for the first day of the year at latitude 40º
```
python plotRadiation.py
```
The results are in W/m^2
