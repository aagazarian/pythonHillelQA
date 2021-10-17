import pytest

from homework_21.infrastructure.current_weather_service import CurrentWeatherService


@pytest.fixture(scope="session")
def current_weather_service() -> CurrentWeatherService:
    yield CurrentWeatherService()
