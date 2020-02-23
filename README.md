# Vayudev
Vayudev is a deep learning powered & web based automated flight plan builder & intuitive deviation monitoring system.

<h2>Problems</h2>
<pre>
1. Flight Deviation?
2. Inaccurate flight path predictions
3. 25+ manual parametres to process( Air Traffic, Air Space, Wind speed, Wind Direction etc)
</pre>

<h2>Vayudev</h2>
<pre>
1. Automated & Intelligent Flight plan builder( Build most Economical flight plan in seconds )
2. Intutive Deviation Monitor( Predict deviations before-hand )
</pre>

![Deviation](https://github.com/anukaisolutions/Vayudev/assets/deviation.png)

<h2>Steps</h2>
<h2>1. 3D Dynamic Airspace Division</h2>
<h3>Dimenshions<h3>
<pre>
Flight Separation Rules
Prohibited/Restricted Airspaces
Individual Cube Score
</pre>
![3d Cube](https://github.com/anukaisolutions/Vayudev/assets/scoreCube.png)
  
<h2>2. Individual Cube Score</h2>
Score = Congestion( Sector Congestion,Airport Congestion,NOTAM’s,Arrival Airport,Departure Airport ) 
      + Aerodynamic Drag(Air Density,Aircraft Type,Bank Angle,Coefficient of Drag,Engine Type,Flight Path Angle,Phase of                flight,True Airspeed,Wind Speed,Wind Direction,Weight) 
      + Weather( Air Pressure,Air Temperature,Humidity,Cloud Cover,Thunderstorm,Precipitation)

<h2>Automated & Intelligent Flight Plan Builder</h2>
<pre>
Goal is to maximise safety while mnimising the fuel and time.
By using Generative Adversarial Networks + Reinforcement learning it will Output: 
Optimal 4D trajectory in ICAO format
Available in AFTN, XML & CSV
</pre>
     
     
<h2>Data Sources</h2>
<pre>
1. Flight Dynamic(FlightRadar24,FlightAware,Mode-S Radars,ADS-B,Aircraft performance files(.opf))
2. Air Traffic (FlightRadar24,FlightAware,ADS-B)
3. Weather(IMD,MetGIS,OpenWeather,Mode-S,METAR,WorldWeather,NOAA,University of Wyoming,UASS(Radiosonde))
</pre>

