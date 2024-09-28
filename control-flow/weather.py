import requests

# Your API key from the weather service (replace 'your_api_key' with the actual API key)
API_KEY = '482d2b25850146c088751423242509'

# Base URL for the API (Example using WeatherAPI)
BASE_URL = 'https://www.weatherapi.com/my/'

# City for which you want the weather information
city = 'Nairobi'

# Full URL to make the API request
url = f"{BASE_URL}?key={API_KEY}&q={city}"

# Make a GET request to fetch the weather data
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Convert the response to JSON format
    data = response.json()
    
    # Extract relevant weather information
    location = data['location']['name']
    temperature = data['current']['temp_c']  # Temperature in Celsius
    condition = data['current']['condition']['text']  # Weather condition
    wind_speed = data['current']['wind_kph']  # Wind speed in kph
    
    # Print the weather information
    print(f"Weather in {location}:")
    print(f"Temperature: {temperature}°C")
    print(f"Condition: {condition}")
    print(f"Wind Speed: {wind_speed} kph")
else:
    # If the API call failed
    print("Error fetching weather data. Please check your API key and city name.")
