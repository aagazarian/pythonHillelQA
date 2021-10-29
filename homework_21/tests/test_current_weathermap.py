import json

from requests import Response

from homework_21.infrastructure.current_weather_service import CurrentWeatherService


def test_check_weather_by_city(current_weather_service):
    current_weather_response = current_weather_service.get_by_city("Kyiv")
    check_status_and_content_type(current_weather_response, 200, "application/json; charset=utf-8")
    current_weather = json.loads(current_weather_response.text, object_hook=CurrentWeatherService.custom_decoder)
    assert current_weather.name == "Kyiv"
    assert current_weather.sys.country == "UA"


def test_check_weather_by_geo_coord(current_weather_service):
    current_weather_response = current_weather_service.get_by_geo_coord("50.4333", "30.5167")
    check_status_and_content_type(current_weather_response, 200, "application/json; charset=utf-8")
    current_weather = json.loads(current_weather_response.text, object_hook=CurrentWeatherService.custom_decoder)
    assert current_weather.name == "Kyiv"
    assert current_weather.sys.country == "UA"


def test_check_weather_by_zip_code(current_weather_service):
    current_weather_response = current_weather_service.get_by_zip_code("94040", "US")
    check_status_and_content_type(current_weather_response, 200, "application/json; charset=utf-8")
    current_weather = json.loads(current_weather_response.text, object_hook=CurrentWeatherService.custom_decoder)
    assert current_weather.name == "Mountain View"
    assert current_weather.sys.country == "US"


def check_status_and_content_type(response: Response, expected_status: int, expected_content_type: str):
    assert response.status_code == expected_status
    assert response.headers.get('content-type') == expected_content_type
