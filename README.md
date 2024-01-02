# SQLAlchemy Challenge - Climate Analysis and Exploration

## Part 1: Climate Analysis and Data Exploration

### Objectives

- Connected to the SQLite database using SQLAlchemy `create_engine`.
- Reflected tables into classes using SQLAlchemy `automap_base`.
- Linked Python to the database by creating an SQLAlchemy session.
- Performed a precipitation analysis and a station analysis.
- Closed the session at the end of the analysis.

### Precipitation Analysis

- Found the most recent date in the dataset.
- Retrieved the last 12 months of precipitation data.
- Loaded query results into a Pandas DataFrame and sort by date.
- Plotted the results and print summary statistics.

### Station Analysis

- Calculated the total number of stations.
- Listed the stations and observation counts in descending order.
- Found the most active station and retrieve the last 12 months of temperature observation data (TOBS).
- Plotted the results as a histogram.

## Part 2: Climate App

Developed a Flask API based on the queries developed.

### Routes

- `/`: Home page listing all routes.
- `/api/v1.0/precipitation`: JSONified precipitation data for the last year.
- `/api/v1.0/stations`: JSON list of stations.
- `/api/v1.0/tobs`: JSON list of temperature observations for the previous year from the most active station.
- `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`: JSON list of the min, avg, and max temperature for a given start or start-end range.


## References

- Menne, M.J., et al. (2012). An overview of the Global Historical Climatology Network-Daily Database. Journal of Atmospheric and Oceanic Technology, 29, 897-910. [Link](https://journals.ametsoc.org/view/journals/atot/29/7/jtech-d-11-00103_1.xml)

