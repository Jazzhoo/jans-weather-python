import main




def test_weather():
    lon = 55
    lat = -3

    weather = main.get_weather(lon, lat)

    assert isinstance(weather, float)