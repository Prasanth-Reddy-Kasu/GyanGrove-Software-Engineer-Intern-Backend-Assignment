from flask import Flask, request, jsonify
import sqlite3
import requests
from datetime import datetime, timedelta
import json
import os

app = Flask(__name__)

# Function to retrieve weather information from the external API
def get_weather(city, date):
    # API URL for weather data
    weather_api_url = f"https://gg-backend-assignment.azurewebsites.net/api/Weather?code=KfQnTWHJbg1giyB_Q9Ih3Xu3L9QOBDTuU5zwqVikZepCAzFut3rqsg==&city={city}&date={date}"
    response = requests.get(weather_api_url)
    # Check if request was successful (status code 200)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Weather data not available"}

# Function to calculate distance between two geographical coordinates using external API
def get_distance(lat1, lon1, lat2, lon2):
    # API URL for distance calculation
    distance_api_url = f"https://gg-backend-assignment.azurewebsites.net/api/Distance?code=IAKvV2EvJa6Z6dEIUqqd7yGAu7IZ8gaH-a0QO6btjRc1AzFu8Y3IcQ==&latitude1={lat1}&longitude1={lon1}&latitude2={lat2}&longitude2={lon2}"
    response = requests.get(distance_api_url)
    # Check if request was successful (status code 200)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Distance data not available"}

# Route to retrieve weather information for a city and date
@app.route('/api/events/weather/<city>/<date>', methods=['GET'])
def weather(city, date):
    return jsonify(get_weather(city, date))

# Route to calculate distance between two geographical coordinates
@app.route('/api/events/distance/<lat1>/<lon1>/<lat2>/<lon2>', methods=['GET'])
def distance(lat1, lon1, lat2, lon2):
    return jsonify(get_distance(lat1, lon1, lat2, lon2))

# Route to add a new event to the database
@app.route('/api/events/add', methods=['POST'])
def add_event():
    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()
    
    data = request.json

    # Check if all required fields are present in the request JSON
    required_fields = ['event_name', 'city_name', 'date', 'time', 'latitude', 'longitude']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    event_name = data['event_name']
    city_name = data['city_name']
    date = data['date']
    time = data['time']
    latitude = data['latitude']
    longitude = data['longitude']

    try:
        # Attempt to insert the event into the database
        cursor.execute("INSERT INTO events (event_name, city_name, date, time, latitude, longitude) VALUES (?, ?, ?, ?, ?, ?)",
                       (event_name, city_name, date, time, latitude, longitude))
        conn.commit()
        conn.close()

        return jsonify({"message": "Event added successfully"}), 201

    except sqlite3.Error as e:
        # If an error occurs during the database operation, roll back the transaction
        conn.rollback()
        conn.close()

        # Return an error message along with the specific error from the database
        return jsonify({"error": f"Failed to add event to the database: {str(e)}"}), 500

# Route to find events within a specified date range
@app.route('/api/events/find', methods=['GET'])
def find_events():
    conn = sqlite3.connect('events.db')
    cursor = conn.cursor()
    
    latitude = float(request.args.get("User's Source Latitude"))
    longitude = float(request.args.get("User's Source Longitude"))
    date = request.args.get('date')

    start_date = datetime.strptime(date, '%Y-%m-%d')
    end_date = start_date + timedelta(days=14)

    cursor.execute("SELECT event_name, city_name, date, latitude, longitude FROM events WHERE date BETWEEN ? AND ? ORDER BY date,city_name;", 
                   (start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')))
    events_data = cursor.fetchall()

    events = []
    for event in events_data:
        # Retrieve weather information for each event
        weather_response = get_weather(event[1], event[2])
        weather = weather_response.get('weather', 'data not available')
        # Calculate distance between event and specified location
        distance_response = get_distance(latitude, longitude, float(event[-2]), float(event[-1]))
        distance = distance_response.get('distance', 'data not available')
        
        event_dict = {
            "event_name": event[0],
            "city_name": event[1],
            "date": event[2],
            "weather": weather,
            "distance_km": float(distance)
        }
        events.append(event_dict)
    
    total_events = len(events)
    total_pages = len(events) // 10 + 1
    pages_list = dict()
    for i in range(total_pages):
        page_key = f"page{i+1}"  # Key for the current page
        page_events = events[i*10 : (i+1)*10]
        print(page_events)
        pages_list.update({
            page_key: {
                "events": page_events,  # Slice events list to get 10 events for current page
                "page": i+1,
                "pageSize": 10,
                "totalEvents": total_events,
                "totalPages": total_pages
            }})

    conn.close()

    return json.dumps(pages_list, sort_keys=False)

if __name__ == '__main__':
    # Run the app using Gunicorn
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
