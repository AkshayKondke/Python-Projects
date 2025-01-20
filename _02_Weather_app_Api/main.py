
import requests


api_key = "your api key here"
BASE_URL = "https://api.weatherbit.io/v2.0/current"


def get_weather(city):
    
    params = {
        "city" : city,
        "key" : api_key 
    }

    response = requests.get(BASE_URL, params)

    if response.status_code == 200:
        data = response.json()
        return data
    else :
        return None

def main():
    print("\nWelcome to Weather App!!\n")

    city = input("Enter the city name: ")
    # req = f"{BASE_URL}?city={city}&key={api_key}"
    # print(req)


    res_data = get_weather(city)

    if res_data:
        city_name = res_data["data"][0]["city_name"]
        # country = res_data["data"][0]["country"]
        tmp = res_data["data"][0]["temp"]
        description = res_data["data"][0]["weather"]["description"]
        time_zone = res_data["data"][0]["timezone"]

        print(f"City: {city_name}")
        # print(f"Country: {country}")
        print(f"Temperature: {tmp}")
        print(f"Weather: {description}")
        print(f"Timezone: {time_zone}")

    else:
        print("Unable to fetch weather data. Please try again.")


if __name__ == "__main__":
    main()
