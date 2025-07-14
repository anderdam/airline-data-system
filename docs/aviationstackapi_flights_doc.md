## Flights
Real-Time Flights Available on: All plans

The API is capable of tracking flights and retrieving flight status information in real-time. In order to look up real-time information about one or multiple flights, you can use the API's flights endpoint together with optional parameters to filter your result set.

Example API Request:

```
Run API Request:
https://api.aviationstack.com/v1/flights
    ? access_key = {API_KEY}
```

### HTTP GET Request Parameters:

| Object                 | Description                                                                                                                                                                                                           |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| access_key             | [Required] Your API access key, which can be found in your acccount dashboard.                                                                                                                                        |
| callback               | [Optional] Use this parameter to specify a JSONP callback function name to wrap your API response in. Learn more about JSONP Callbacks.                                                                               |
| limit                  | [Optional] Specify a limit of results to return in your API response. Maximum allowed value is 100 below <br/>Professional Plan and 1000 on and above Professional Plan. Default value is 100.                        |
| offset                 | [Optional] Specify an offset for pagination. Example: Specifying an offset of 10 in combination with a <br/>limit of 10 will show results 10-20. Default offset value is 0, starting with the first available result. |
| flight_status          | [Optional] Filter your results by flight status. Available values: scheduled, active, landed, <br/>cancelled, incident, diverted                                                                                      |
| flight_date            | [Optional] Filter your results by providing a flight date in the format YYYY-MM-DD. Example: <br/>2019-02-28                                                                                                          |
| dep_iata               | [Optional] Filter your results by departure city or airport using an IATA code. You can retrieve <br/>IATA codes using the Airports or Cities API endpoints.                                                          |
| arr_iata               | [Optional] Filter your results by arrival city or airport using an IATA code. You can retrieve IATA <br/>codes using the Airports or Cities API endpoints.                                                            |
| dep_icao               | [Optional] Filter your results by departure airport using an ICAO code. You can retrieve ICAO codes <br/>using the Airports API endpoint.                                                                             |
| arr_icao               | [Optional] Filter your results by arrival airport using an ICAO code. You can retrieve ICAO codes <br/>using the Airports API endpoint.                                                                               |
| airline_name           | [Optional] Filter your results by airline name. You can retrieve airline names using the <br/>Airlines API endpoint.                                                                                                  |
| airline_iata           | [Optional] Filter your results by airline IATA code. You can retrieve airline IATA codes using <br/>the Airlines API endpoint.                                                                                        |
| airline_icao           | [Optional] Filter your results by airline ICAO code. You can retrieve airline ICAO codes using <br/>the Airlines API endpoint.                                                                                        |
| flight_number          | [Optional] Filter your results by providing a flight number. Example: 2557                                                                                                                                            |
| flight_iata            | [Optional] Filter your results by providing a flight IATA code. Example: MU2557                                                                                                                                       |
| flight_icao            | [Optional] Filter your results by providing a flight ICAO code. Example: CES2557                                                                                                                                      |
| min_delay_dep          | [Optional] Filter your results by providing a minimum amount of minutes in departure delay. <br/>Example: 7 for seven minutes of delay in departure.                                                                  |
| min_delay_arr          | [Optional] Filter your results by providing a minimum amount of minutes in arrival delay. <br/>Example: 7 for seven minutes of delay in arrival.                                                                      |
| max_delay_dep          | [Optional] Filter your results by providing a maximum amount of minutes in departure delay. <br/>Example: 60 for one hour of delay in departure.                                                                      |
| max_delay_arr          | [Optional] Filter your results by providing a maximum amount of minutes in arrival delay. <br/>Example: 60 for one hour of delay in arrival.                                                                          |
| arr_scheduled_time_arr | [Optional] Filter your results by providing a arrival date in the format YYYY-MM-DD. <br/>Example: 2019-02-28                                                                                                         |
| arr_scheduled_time_dep | [Optional] Filter your results by providing a departure date in the format YYYY-MM-DD. <br/>Example: 2019-02-28                                                                                                       |

Example API Response:

```json
{
    "pagination": {
        "limit": 100,
        "offset": 0,
        "count": 100,
        "total": 1669022
    },
    "data": [
        {
            "flight_date": "2019-12-12",
            "flight_status": "active",
            "departure": {
                "airport": "San Francisco International",
                "timezone": "America/Los_Angeles",
                "iata": "SFO",
                "icao": "KSFO",
                "terminal": "2",
                "gate": "D11",
                "delay": 13,
                "scheduled": "2019-12-12T04:20:00+00:00",
                "estimated": "2019-12-12T04:20:00+00:00",
                "actual": "2019-12-12T04:20:13+00:00",
                "estimated_runway": "2019-12-12T04:20:13+00:00",
                "actual_runway": "2019-12-12T04:20:13+00:00"
            },
            "arrival": {
                "airport": "Dallas/Fort Worth International",
                "timezone": "America/Chicago",
                "iata": "DFW",
                "icao": "KDFW",
                "terminal": "A",
                "gate": "A22",
                "baggage": "A17",
                "delay": 0,
                "scheduled": "2019-12-12T04:20:00+00:00",
                "estimated": "2019-12-12T04:20:00+00:00",
                "actual": null,
                "estimated_runway": null,
                "actual_runway": null
            },
            "airline": {
                "name": "American Airlines",
                "iata": "AA",
                "icao": "AAL"
            },
            "flight": {
                "number": "1004",
                "iata": "AA1004",
                "icao": "AAL1004",
                "codeshared": null
            },
            "aircraft": {
               "registration": "N160AN",
               "iata": "A321",
               "icao": "A321",
               "icao24": "A0F1BB"
            },
            "live": {
                "updated": "2019-12-12T10:00:00+00:00",
                "latitude": 36.28560000,
                "longitude": -106.80700000,
                "altitude": 8846.820,
                "direction": 114.340,
                "speed_horizontal": 894.348,
                "speed_vertical": 1.188,
                "is_ground": false
            }
        },
        [...]
    ]
}
```

Please note: The API response above has been shortened to show only one flight result for readability purposes.

### API Response Objects:
| Response Object                | 	Description                                                                                                                                                                    |
|--------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| pagination > limit             | 	Returns the specified or default limit of results per pagination page.                                                                                                         |
| pagination > offset            | 	Returns the specified or default pagination offset.                                                                                                                            |
| pagination > count             | 	Returns the number of results found on the current pagination page.                                                                                                            |
| pagination > total             | 	Returns the total number of results found for your API request.                                                                                                                |
| results                        | Returns an array of flights, included objects are explained below.                                                                                                              |
| flight_date                    | 	Returns the date of the flight. Format: YYYY-MM-DD                                                                                                                             |
| flight_status                  | Returns the flight status. Possible values: scheduled, active, landed, cancelled, incident, diverted                                                                            |
| departure > airport            | 	Returns the name of the departure airport.                                                                                                                                     |
| departure > timezone           | 	Returns the departure timezone. Example: America/Los_Angeles                                                                                                                   |
| departure > iata               | 	Returns the IATA code of the departure location/airport.                                                                                                                       |
| departure > icao               | 	Returns the ICAO code of the departure location/airport.                                                                                                                       |
| departure > terminal           | 	Returns the departure terminal.                                                                                                                                                |
| departure > gate               | 	Returns the departure gate.                                                                                                                                                    |
| departure > delay              | 	Returns the delay in departure in minutes.                                                                                                                                     |
| departure > scheduled          | 	Returns the scheduled departure date and time in RFC3339 (ISO8601) format. Example: 2019-12-12T04:20:00+00:00                                                                  |
| departure > estimated          | 	Returns the estimated departure date and time in RFC3339 (ISO8601) format. Example: 2019-12-12T04:20:00+00:00                                                                  |
| departure > actual             | 	Returns the actual departure date and time in RFC3339 (ISO8601) format. Example: 2019-12-12T04:20:00+00:00                                                                     |
| departure > estimated_runway   | 	Returns the estimated runway date and time in RFC3339 (ISO8601) format in the departure location/airport. Example: 2019-12-12T04:20:00+00:00                                   |
| departure > actual_runway      | 	Returns the actual runway date and time in the departure location/airport in RFC3339 (ISO8601) format. Example: 2019-12-12T04:20:00+00:00                                      |
| arrival > airport              | 	Returns the name of the arrival airport.                                                                                                                                       |
| arrival > timezone             | 	Returns the arrival timezone. Example: America/Los_Angeles                                                                                                                     |
| arrival > iata                 | 	Returns the IATA code of the arrival location/airport.                                                                                                                         |
| arrival > icao                 | 	Returns the ICAO code of the arrival location/airport.                                                                                                                         |
| arrival > terminal             | 	Returns the arrival terminal.                                                                                                                                                  |
| arrival > gate                 | 	Returns the arrival gate.                                                                                                                                                      |
| arrival > baggage              | 	Returns the baggage claim gate at the arrival airport.                                                                                                                         |
| arrival > delay                | 	Returns the delay in arrival in minutes.                                                                                                                                       |
| arrival > scheduled            | 	Returns the scheduled arrival date and time in RFC3339 (ISO8601) format. Example: 2019-12-12T04:20:00+00:00                                                                    |
| arrival > estimated            | 	Returns the actual arrival date and time in RFC3339 (ISO8601) format. Example: 2019-12-12T04:20:00+00:00                                                                       |
| arrival > actual               | 	Returns the actual arrival date and time in RFC3339 (ISO8601) format. Example: 2019-12-12T04:20:00+00:00                                                                       |
| arrival > estimated_runway     | 	Returns the estimated runway date and time in the arrival location/airport in RFC3339 (ISO8601) format. Example: 2019-12-12T04:20:00+00:00                                     |
| arrival > actual_runway        | 	Returns the actual runway date and time in the arrival location/airport in RFC3339 (ISO8601) format. Example: 2019-12-12T04:20:00+00:00                                        |
| airline > name                 | 	Returns the name of the airline. Example: American Airlines                                                                                                                    |
| airline > iata                 | 	Returns the IATA code of the airline. Example: AA                                                                                                                              |
| airline > icao                 | 	Returns the ICAO code of the airline. Example: AAL                                                                                                                             |
| flight > number                | 	Returns the flight number. Example: 1004                                                                                                                                       |
| flight > iata                  | 	Returns the IATA number of the flight. Example: AA1004                                                                                                                         |
| flight > icao                  | 	Returns the ICAO number of the flight. Example: AAL1004                                                                                                                        |
| flight > codeshared            | 	Returns one or more sub-objects detailing the operating airline and flight in a codeshare agreement (e.g., a Qantas flight operated by LATAM), or null if no codeshare exists. |
| live > updated                 | 	Returns the exact date and time the live data was collected in RFC3339 (ISO8601) format.                                                                                       |
| live > latitude                | 	Returns the latitude coordinate associated with the aircraft location.                                                                                                         |
| live > longitude               | 	Returns the longitude coordinate associated with the aircraft location.                                                                                                        |
| live > altitude                | 	Returns the altitude (in meters) of the aircraft at the given time.                                                                                                            |
| live > direction               | 	Returns the direction (in degrees) of the aircraft at the given time.                                                                                                          |
| live > speed_horizontal        | 	Returns the horizontal speed (in kilometers per hour) of the aircraft at the given time.                                                                                       |
| live > speed_vertical          | 	Returns the vertical speed (in kilometers per hour) of the aircraft at the given time.                                                                                         |
| live > is_ground               | 	Returns true or false depending on whether or not the aircraft is on the ground at the given time.                                                                             |
| live > aircraft > registration | 	Returns the registration number of the aircraft. Example: N160AN                                                                                                               |
| live > aircraft > iata         | 	Returns the IATA code of the aircraft. Example: A321                                                                                                                           |
| live > aircraft > icao         | 	Returns the ICAO code of the aircraft. Example: A321                                                                                                                           |
| live > aircraft > icao24       | 	Returns the ICAO24 code of the aircraft. Example: A0F1BB                                                                                                                       |

Using Flight endpoint, you can track Flight in real time and get flight status information.

### Python example to get real-time flight data:

```python
import requests

url = "https://api.aviationstack.com/v1/flights?access_key={PASTE_YOUR_API_KEY_HERE}"

response = requests.get(url)

print(response.json())
```

Historical Flights Available on: Basic Plan and higher

Apart from providing data about real-time flight, the API's flights endpoint is also capable of looking up data about historical flights. In order to request data about one or more past flights, simply attach the flight_date parameter to your API request URL and set it to a date of your choice.

Example API Request:

```plaintext
Run API Request
https://api.aviationstack.com/v1/flights
    ? access_key = {API_KEY}
    & flight_date = 2025-06-11
```
Note: Aviationstack provides historical data for the last 3 months only.

HTTP GET Request Parameters:

| Object                 | 	Description                                                                                                                                                                                                      |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| access_key             | 	[Required] Your API access key, which can be found in your acccount dashboard.                                                                                                                                   |
| flight_date            | 	[Required] Specify your historical flight date in the format YYYY-MM-DD. Example: 2019-02-28                                                                                                                     |
| callback               | 	[Optional] Use this parameter to specify a JSONP callback function name to wrap your API response in. Learn more about JSONP Callbacks.                                                                          |
| limit                  | 	[Optional] Specify a limit of results to return in your API response. Maximum allowed value is 100 below Professional Plan and 1000 on and above Professional Plan. Default value is 100.                        |
| offset                 | 	[Optional] Specify an offset for pagination. Example: Specifying an offset of 10 in combination with a limit of 10 will show results 10-20. Default offset value is 0, starting with the first available result. |
| flight_status          | 	[Optional] Filter your results by flight status. Available values: scheduled, active, landed, cancelled, incident, diverted                                                                                      |
| dep_iata               | 	[Optional] Filter your results by departure city or airport using an IATA code. You can retrieve IATA codes using the Airports or Cities API endpoints.                                                          |
| arr_iata               | 	[Optional] Filter your results by arrival city or airport using an IATA code. You can retrieve IATA codes using the Airports or Cities API endpoints.                                                            |
| dep_icao               | 	[Optional] Filter your results by departure airport using an ICAO code. You can retrieve ICAO codes using the Airports API endpoint.                                                                             |
| arr_icao               | 	[Optional] Filter your results by arrival airport using an ICAO code. You can retrieve ICAO codes using the Airports API endpoint.                                                                               |
| airline_name           | 	[Optional] Filter your results by airline name. You can retrieve airline names using the Airlines API endpoint.                                                                                                  |
| airline_iata           | 	[Optional] Filter your results by airline IATA code. You can retrieve airline IATA codes using the Airlines API endpoint.                                                                                        |
| airline_icao           | 	[Optional] Filter your results by airline ICAO code. You can retrieve airline ICAO codes using the Airlines API endpoint.                                                                                        |
| flight_number          | 	[Optional] Filter your results by providing a flight number. Example: 2557                                                                                                                                       |
| flight_iata            | 	[Optional] Filter your results by providing a flight IATA code. Example: MU2557                                                                                                                                  |
| flight_icao            | 	[Optional] Filter your results by providing a flight ICAO code. Example: CES2557                                                                                                                                 |
| min_delay_dep          | 	[Optional] Filter your results by providing a minimum amount of minutes in departure delay. Example: 7 for seven minutes of delay in departure.                                                                  |
| min_delay_arr          | 	[Optional] Filter your results by providing a minimum amount of minutes in arrival delay. Example: 7 for seven minutes of delay in arrival.                                                                      |
| max_delay_dep          | 	[Optional] Filter your results by providing a maximum amount of minutes in departure delay. Example: 60 for one hour of delay in departure.                                                                      |
| max_delay_arr          | 	[Optional] Filter your results by providing a maximum amount of minutes in arrival delay. Example: 60 for one hour of delay in arrival.                                                                          |
| arr_scheduled_time_arr | 	[Optional] Filter your results by providing a arrival date in the format YYYY-MM-DD. Example: 2019-02-28                                                                                                         |
| arr_scheduled_time_dep | 	[Optional] Filter your results by providing a departure date in the format YYYY-MM-DD. Example: 2019-02-28                                                                                                       |

Using Flight endpoint, you can also get the historical flight data. Use flight_date parameter this YYYY-MM-DD format.




import requests

url = "https://api.aviationstack.com/v1/flights?access_key={PASTE_YOUR_API_KEY_HERE}"

querystring = {"date":"2019-12-11"}

response = requests.get(url, params=querystring)

print(response.json())







Example API Response:

Important: The API response returned for historical flights is identical to the API response returned for real-time flight data. To see the API response, please jump to the Real-Time Flights section.
