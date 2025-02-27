import requests
import pandas as pd

# Function to get air quality data from OpenAQ
def get_air_quality_data(city, start_date, end_date, parameter='pm25'):
    url = f'https://api.openaq.org/v1/measurements'
    params = {
        'city': city,
        'parameter': parameter,
        'date_from': start_date,
        'date_to': end_date,
        'limit': 10000
    }
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data['results'])
    df['date'] = pd.to_datetime(df['date']['utc'])
    return df[['date', 'value']]

# Function to get weather data from OpenWeatherMap
def get_weather_data(city, api_key, start_date, end_date):
    url = f'http://api.openweathermap.org/data/2.5/onecall/timemachine'
    weather_data = []
    dates = pd.date_range(start_date, end_date)
    for date in dates:
        timestamp = int(date.timestamp())
        params = {
            'lat': city['lat'],
            'lon': city['lon'],
            'dt': timestamp,
            'appid': api_key
        }
        response = requests.get(url, params=params)
        data = response.json()
        weather_data.append(data['current'])
    df = pd.DataFrame(weather_data)
    df['date'] = pd.to_datetime(df['dt'], unit='s')
    return df[['date', 'temp', 'humidity', 'wind_speed']]

# Example usage
if __name__ == "__main__":
    city = 'Los Angeles'
    start_date = '2022-01-01'
    end_date = '2022-12-31'
    api_key = 'YOUR_OPENWEATHERMAP_API_KEY'

    aq_data = get_air_quality_data(city, start_date, end_date)
    weather_data = get_weather_data({'lat': 34.0522, 'lon': -118.2437}, api_key, start_date, end_date)

    # Merge datasets
    data = pd.merge(aq_data, weather_data, on='date')
    data.to_csv('air_quality_weather_data.csv', index=False)