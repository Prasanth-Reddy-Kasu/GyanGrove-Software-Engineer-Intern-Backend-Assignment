# GyanGrove-Software-Engineer-Intern-Backend-Assignment

Backend-Assignment by GyanGrove for Software Engineer Intern Role

## Tech Stack and Database

For this project, the following tech stack was chosen:

- **Python**: Chosen for its simplicity, versatility, and extensive ecosystem of libraries, particularly Flask for building the API.
- **Flask**: Used to create the RESTful API endpoints for handling HTTP requests.
- **SQLite3**: Utilized as the database management system due to its lightweight nature and simplicity for small-scale applications.
- **Requests library**: Employed for making HTTP requests to external APIs for weather information and distance calculation.

### Design Decisions

- **Python and Flask**: Chosen for their ease of use and rapid development capabilities, allowing for quick iteration and prototyping.
- **SQLite3**: Selected as the database due to its simplicity and minimal setup requirements, suitable for small-scale applications like this one.
- **Requests library**: Used to interact with external APIs for retrieving weather information and calculating distances, enhancing the functionality of the application without the need for complex integrations.

### Challenges Addressed

- **Choosing the Tech Stack**: Considered various tech stacks and frameworks before deciding on Python and Flask for their simplicity and suitability for the project requirements.
- **Integration with External APIs**: Ensured smooth integration with external APIs for retrieving weather information and calculating distances, handling errors, and edge cases effectively.

## Setting Up and Running the Project

To set up and run the project locally, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running the following command:
    ```
    pip install -r requirements.txt
    ```
3. Run the Flask application by executing the following command:
    ```
    python api.py
    ```
4. Access the API endpoints using tools like Postman, curl, or by sending HTTP requests programmatically.

## API Endpoints

### GET /api/events/weather

#### Description
Retrieve weather information for a specified city and date.

#### Request Format
- Parameters: `city` (string), `date` (string in YYYY-MM-DD format)

#### Response Format
- JSON object containing weather information, including temperature.
- Example: 
    ```json
    {
        "weather": "Snowy 14C"
    }
    ```

#### Breakdown
- This endpoint allows clients to retrieve weather information for a specific city and date.
- It accepts two query parameters: `city` (string) and `date` (string in YYYY-MM-DD format).
- Upon successful request, it returns a JSON object containing weather information, including temperature.
- If weather data is unavailable or an error occurs, an appropriate error message is returned.

### GET /api/events/distance

#### Description
Calculate the distance between two geographical coordinates.

#### Request Format
- Parameters: `lat1` (float), `lon1` (float), `lat2` (float), `lon2` (float)

#### Response Format
- JSON object containing the calculated distance in kilometers.
- Example:
    ```json
    {
        "distance": 14788.096540228473
    }
    ```

#### Breakdown
- This endpoint calculates the distance between two geographical coordinates provided by the client.
- It accepts four query parameters: `lat1` (float), `lon1` (float), `lat2` (float), and `lon2` (float).
- The response includes a JSON object containing the calculated distance in kilometers.
- If distance calculation fails or an error occurs, an appropriate error message is returned.

### POST /api/events/add

#### Description
Add a new event to the system.

#### Request Format
- JSON object containing event details, including `event_name`, `city_name`, `date`, `time`, `latitude`, and `longitude`.

#### Response Format
- JSON object confirming the successful addition of the event.
- Example:
    ```json
    {
        "event_name": "Birthday Party",
        "city_name": "New York",
        "date": "2024-04-15",
        "time": "15:00",
        "latitude": 40.7128,
        "longitude": -74.0060
    }
    ```

#### Breakdown
- This endpoint allows clients to add a new event to the system by providing event details in a JSON object.
- Required fields include `event_name`, `city_name`, `date`, `time`, `latitude`, and `longitude`.
- Upon successful addition, a confirmation message is returned.
- If any required field is missing or an error occurs during insertion, an appropriate error message is returned.

### GET /api/events/find

#### Description
Find events within a specified date range starting from the given date and extending up to 14 days ahead, from a given location.

#### Request Format
- Parameters: `latitude` (float), `longitude` (float), `date` (string in YYYY-MM-DD format)

#### Response Format
- JSON object containing a list of events within the specified date range, including event details, weather information, and distance.
- Example:
    ```json
    {
        "events": [
        {
            "event_name": "Birthday Party",
            "city_name": "New York",
            "date": "2024-04-15",
            "weather": "Sunny 22C",
            "distance_km": 5.67
        },
        {
            "event_name": "Concert",
            "city_name": "New York",
            "date": "2024-04-15",
            "weather": "Cloudy 18C",
            "distance_km": 3.21
        }
        // other event objects...
        ],
    "page": 1,
    "pageSize": 10,
    "totalEvents": 20,
    "totalPages": 2
    }
    ```

#### Breakdown
- This endpoint searches for events within a specified date range starting from the given date and extending up to 14 days ahead, from a given location (latitude and longitude).
- It accepts three query parameters: `latitude` (float), `longitude` (float), and `date` (string in YYYY-MM-DD format).
- The response includes a JSON object containing a list of events within the specified date range, along with weather information and distance.
- Pagination is applied to the response, limiting the number of events per page.

## File Structure

The project consists of the following files:

1. **api.py**: Contains the main Flask application code for handling API endpoints related to event management.
2. **events.py**: Includes functions for interacting with the SQLite database, such as creating the database, clearing existing data, and inserting data from a CSV file.
3. **events.db**: SQLite database file for storing event data.
4. **Backend_assignment_gg_dataset.csv**: CSV file containing event data to be inserted into the database.
5. **README.md**: This file, providing an overview of the project and its components.

## Description of Files

### api.py

- **Description**: Main application file containing Flask routes for handling API requests related to event management.
- **Contents**:
  - Definitions of Flask routes for retrieving weather information, calculating distance, adding events, and finding events within a specified date range.
  - Integration with external APIs for weather data and distance calculation.
  - Handling of database operations for adding and retrieving events.

### events.py

- **Description**: File containing functions for database management and data insertion from a CSV file.
- **Contents**:
  - Functions for creating the SQLite database, clearing existing data, and inserting data from a CSV file into the database.
  - Utilization of the `sqlite3` module for interacting with the SQLite database.

### events.db

- **Description**: SQLite database file used for storing event data.
- **Contents**: 
  - Tables and rows containing event information, including event name, city, date, time, latitude, and longitude.

### Backend_assignment_gg_dataset.csv

- **Description**: CSV file containing event data to be inserted into the database.
- **Contents**: 
  - Rows of event data, including event name, city, date, time, latitude, and longitude.

### Dependencies

- **Flask**: `3.0.2`
- **requests**: `2.31.0`
- **sqlite3**: Included in Python standard library

## screen recording showing the execution of the provided test case through your API

[![Postman Screen Record] https://github.com/Prasanth-Reddy-Kasu/GyanGrove-Software-Engineer-Intern-Backend-Assignment/blob/55a1df2da793f78008dfe52eb5425fe5fb20f7ae/Screen%20Record%20-%20API%20Execution.mp4
