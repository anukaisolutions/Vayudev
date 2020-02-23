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
![4d Deviation](https://github.com/anukaisolutions/Vayudev/blob/master/assets/4dDeviation.png)

<h2>Steps</h2>
<h2>1. 3D Dynamic Airspace Division</h2>
<h3>Dimenshions</h3>
  
<pre>
Flight Separation Rules
Prohibited/Restricted Airspaces
Individual Cube Score
</pre>

![Deviation](https://github.com/anukaisolutions/Vayudev/blob/master/assets/deviation.png)

![Score Cube](https://github.com/anukaisolutions/Vayudev/blob/master/assets/scoreCube.png)
<h2>2. Individual Cube Score</h2>
Score = Congestion( Sector Congestion,Airport Congestion,NOTAM’s,Arrival Airpseort,Departure Airport ) 
      + Aerodynamic Drag(Air Density,Aircraft Type,Bank Angle,Coefficient of Drag,Engine Type,Flight Path Angle,Phase of                flight,True Airspeed,Wind Speed,Wind Direction,Weight) 
      + Weather( Air Pressure,Air Temperature,Humidity,Cloud Cover,Thunderstorm,Precipitation)



<h2>Automated & Intelligent Flight Plan Builder</h2>
<pre>
Goal is to maximise safety while mnimising the fuel and time.
By using Generative Adversarial Networks + Reinforcement learning it will Output: 
Optimal 4D trajectory in ICAO format
Available in AFTN, XML & CSV
</pre>

![Behaviour Analysis](https://github.com/anukaisolutions/Vayudev/blob/master/assets/behaviour.png)
     
<h2>Data Sources</h2>
<pre>
1. Flight Dynamic(FlightRadar24,FlightAware,Mode-S Radars,ADS-B,Aircraft performance files(.opf))
2. Air Traffic (FlightRadar24,FlightAware,ADS-B)
3. Weather(IMD,MetGIS,OpenWeather,Mode-S,METAR,WorldWeather,NOAA,University of Wyoming,UASS(Radiosonde))
</pre>

![Deployment Architecture](https://github.com/anukaisolutions/Vayudev/blob/master/assets/architecture.png)

<h2>LSTM</h2>
Long Short-Term Memory (LSTM) networks are a type of recurrent neural network capable of learning order dependence in sequence prediction problems

![LSTM](https://github.com/anukaisolutions/Vayudev/blob/master/assets/lstm.png)
![Workflow](https://github.com/anukaisolutions/Vayudev/blob/master/assets/workflow.png)

<h2>BADA Equations</h2>

![Bada](https://github.com/anukaisolutions/Vayudev/blob/master/assets/bada.png)
![Bada](https://github.com/anukaisolutions/Vayudev/blob/master/assets/bada2.png)

<h3>Operation file for coefficient of drag and coefficient of thrust</h3>

![Operation file](https://github.com/anukaisolutions/Vayudev/blob/master/assets/opfile.png)

<h3>Calculation of upper air data using ground level data and equations</h3>

![Upper Air Data Calculation](https://github.com/anukaisolutions/Vayudev/blob/master/assets/upperAir.png)

