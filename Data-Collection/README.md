# Data Collection

This Python application is designed to collect data from the NOAA Space Weather Prediction Center (SWPC) and the data is the Real-Time Solar Wind (RTSW) from the NOAA/DSCOVR satellite.  
The source is available at: https://services.swpc.noaa.gov/products/geospace/propagated-solar-wind-1-hour.json  

The app uses pystow to download the data and store it in a host directory.
To persist the data, the JSON object is pickled and stored in a directory structure that is based on the date of the data.

-----

You have been assigned to write an app that collects data from an outside source.  
The source is from the NOAA Space Weather Prediction Center (SWPC) and the data is the Real-Time Solar Wind (RTSW) from the NOAA/DSCOVR satellite.  
The source is available at: https://services.swpc.noaa.gov/products/geospace/propagated-solar-wind-1-hour.json

Develop an application and/or associated with Application Programming Interfaces (APIs), in Python 3, that will download RTWS data. If you are asked to persist this data, how will you go about achieving this task? Write a persistent layer with extensibility in mind.  
- Be aware that you need to extend it to other different NOAA data sources.  
- Pay attention to cadence, real-time requirements, and network constraints.

(Optional) Finally, you are asked to containerize your app, please provide the appropriate necessary files, that will allow running your app as a container, in your favorite container runtime.

(Bonus: web-gui) You are now tasked with writing a dashboard that will provide early warning of solar storms, you may use any web-based GUI framework, e., g React, Vue, angular, you wish to accomplish this task.

(Bonus: Machine Learning): Write a prediction engine that will try to forecast future space weather based on past data.  
- What was your preferred approach to this problem?  
- Test it for some time, how would you go about comparing it to the real results?
