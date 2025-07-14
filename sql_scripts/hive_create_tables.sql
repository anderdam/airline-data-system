CREATE TABLE flights (
  flight_date STRING,
  airline_code STRING,
  flight_number STRING,
  origin STRING,
  destination STRING,
  departure_delay INT,
  arrival_delay INT,
  cancelled BOOLEAN,
  diverted BOOLEAN
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
