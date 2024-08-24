import json
import os
import sys
import requests
from typing import Union
from pydantic import BaseModel

class GeoRequest(BaseModel):
    city: str
    country: Union[str, None] = None
    state: Union[str, None] = None

weather_api = os.getenv("WEATHER_API_KEY")

def get_lat_long(req: GeoRequest, api_key: str):
    api_url = f"https://api.api-ninjas.com/v1/geocoding?city={req["city"]}"
    headers = {"X-Api-Key": api_key}
    if req.get("country"):
        api_url += f"&country={req["country"]}"
    if req.get("state"):
        api_url += f"&state={req["state"]}"
    resp = requests.get(api_url, headers=headers)

    if resp.status_code == requests.codes.ok:
        return resp.text
    else:
        print("Error occured: ", resp.status_code, resp.text)

def get_weather(lon: float, lat: float):
    r = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m",)
    print(f"Status: {r.status_code} and reason: {r. reason}")
    current_temp = r.json().get("current").get("temperature_2m")
    # print(f"Current temp: {current_temp}")
    return current_temp


def main():
    print("Hello from Jan's Weather app written in Python")
 
    geo_resp = get_lat_long(
        {"city": "City of Edinburgh", "country": "GB"}, weather_api)
    print(geo_resp)    
    geo_resp = json.loads(geo_resp)
    geo_resp = geo_resp[0]
    temp = get_weather(geo_resp.get("longitude"), geo_resp.get("latitude"))

    print("=== from weather ===")
    print(temp)

    pass

if __name__ == "__main__":
    main()
