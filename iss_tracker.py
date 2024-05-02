import requests

def get_iss_location():
    try:
        # Make API call to get ISS location data
        response = requests.get("http://api.open-notify.org/iss-now.json")
        data = response.json()
        
        # Extract latitude and longitude from the response
        latitude = data['iss_position']['latitude']
        longitude = data['iss_position']['longitude']
        
        return latitude, longitude
    except Exception as e:
        print("Error:", e)
        return None, None

def display_location(latitude, longitude):
    if latitude is not None and longitude is not None:
        print(f"ISS's present location: Latitude: {latitude}°, Longitude: {longitude}°")
    else:
        print("Failed to retrieve ISS location.")

def main():
    latitude, longitude = get_iss_location()
    display_location(latitude, longitude)

if __name__ == "__main__":
    main()
