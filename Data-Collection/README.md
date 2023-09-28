# Data Collection

This Python application is designed to collect data from the NOAA Space Weather Prediction Center (SWPC) and the data is the Real-Time Solar Wind (RTSW) from the NOAA/DSCOVR satellite.  
The source is available at: https://services.swpc.noaa.gov/products/geospace/propagated-solar-wind-1-hour.json  

The app uses pystow to download the data and store it in a host directory.
The data is then parsed into a Pandas DataFrame and pickled to a file within the repository.  
A maximum of 100 files are stored, and the oldest file is deleted when a new file is downloaded.

A dockerfile is included to build a container to run the application.