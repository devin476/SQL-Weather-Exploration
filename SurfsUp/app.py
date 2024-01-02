from flask import Flask, jsonify
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import numpy as np

# Database setup
engine = create_engine("sqlite:///../Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask setup
app = Flask(__name__)

# Flask routes
@app.route("/")
def home():
    return '''
        <h1>API Routes</h1>
        <a href="/api/v1.0/precipitation" style="display: block; margin: 10px; text-align: center; background-color: #4CAF50; color: white; padding: 14px 20px; text-decoration: none; border: none; border-radius: 4px; cursor: pointer;">Precipitation</a>
        <a href="/api/v1.0/stations" style="display: block; margin: 10px; text-align: center; background-color: #008CBA; color: white; padding: 14px 20px; text-decoration: none; border: none; border-radius: 4px; cursor: pointer;">Stations</a>
        <a href="/api/v1.0/tobs" style="display: block; margin: 10px; text-align: center; background-color: #f44336; color: white; padding: 14px 20px; text-decoration: none; border: none; border-radius: 4px; cursor: pointer;">Temperature Observations (TOBS)</a>
        <a href="/api/v1.0/<start>" style="display: block; margin: 10px; text-align: center; background-color: #e7e7e7; color: black; padding: 14px 20px; text-decoration: none; border: none; border-radius: 4px; cursor: pointer;">Start Date</a>
        <a href="/api/v1.0/<start>/<end>" style="display: block; margin: 10px; text-align: center; background-color: #555555; color: white; padding: 14px 20px; text-decoration: none; border: none; border-radius: 4px; cursor: pointer;">Start/End Date</a>
    '''

@app.route("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    # Query for the last 12 months of precipitation data
    start_date = '2017-07-10'
    results = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= start_date).all()
    session.close()

    # Convert list of tuples into a dictionary
    precipitation = {date: prcp for date, prcp in results}

    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    # Query all stations
    results = session.query(Station.station).all()
    session.close()

    # Convert list of tuples into normal list
    stations = list(np.ravel(results))

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    most_active_station = 'USC00519281'
    start_date = '2017-07-10'
    # Query the last year of temperature observations
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= 'start_date', Measurement.station == most_active_station).all()
    session.close()

    # Convert list of tuples into dict
    temperatures = {date: tobs for date, tobs in results}

    return jsonify(temperatures)

@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def start_end(start=None, end=None):
    session = Session(engine)
    if not end:
        results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    else:
        results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    session.close()

   
    temps = list(np.ravel(results))

    return jsonify(temps)

if __name__ == '__main__':
    app.run(debug=True)