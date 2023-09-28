# Data Collection

This Python application is designed to collect data from the NOAA Space Weather Prediction Center (SWPC) and the data is the Real-Time Solar Wind (RTSW) from the NOAA/DSCOVR satellite.  
The source is available at: https://services.swpc.noaa.gov/products/geospace/propagated-solar-wind-1-hour.json  

The app uses pystow to download the data and store it in a host directory.
To persist the data, the JSON object is pickled and stored in a directory structure that is based on the date of the data.
Alternatively, a Pandas Dataframe could be used to store the data in a CSV file, with some additional code to handle the directory structure,  
and a limit on the number of files in a directory/rows in the dataframe.
