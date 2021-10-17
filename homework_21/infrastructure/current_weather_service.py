import json
from collections import namedtuple

from homework_21.app import config
from requests import Response, get


def print_pretty_json_response(response):
    pretty_json = json.dumps(response.json(), sort_keys=True, indent=4)
    print(f"\nResponse:\n{pretty_json}")


class CurrentWeatherService:
    def __init__(self):
        self.__current_weather_url = f"{config['host']}/weather"
        self.__api_key = f"{config['appid']}"

    @staticmethod
    def custom_decoder(current_weather_dict):
        return namedtuple('X', current_weather_dict.keys())(*current_weather_dict.values())

    def get_by_city(self, city_name: str) -> Response:
        print(f"\nSendRequest to '{self.__current_weather_url}?q={city_name}&appid={self.__api_key}'")
        response = get(f"{self.__current_weather_url}?q={city_name}&appid={self.__api_key}")
        print_pretty_json_response(response)
        return response

    def get_by_geo_coord(self, lat: float, lon: float) -> Response:
        print(f"\nSendRequest to '{self.__current_weather_url}?lat={lat}&lon={lon}&appid={self.__api_key}'")
        response = get(f"{self.__current_weather_url}?lat={lat}&lon={lon}&appid={self.__api_key}")
        print_pretty_json_response(response)
        return response

    def get_by_zip_code(self, zip_code: int, country_code: str) -> Response:
        print(f"\nSendRequest to '{self.__current_weather_url}?zip={zip_code},{country_code}&appid={self.__api_key}'")
        response = get(f"{self.__current_weather_url}?zip={zip_code},{country_code}&appid={self.__api_key}")
        print_pretty_json_response(response)
        return response
