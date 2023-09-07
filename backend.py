import requests

API_KEY = "6e4cfeeded6be6d00332bd74694500ca"


def get_data(place, forcast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_variable = 8 * forcast_days
    filtered_data = filtered_data[:nr_variable]
    return filtered_data

if __name__=="__main__":
    print(get_data(place="tokyo"))