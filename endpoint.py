import requests
import json


class Weather():

    def __init__(self, zip_code):
        self.zip_code = zip_code
        self.url = "http://api.wunderground.com/api/conditions/forecast10day/astronomy/alerts/currenthurricane/{}.json".format(zip_code)
        json = requests.get(self.url).json()


class Current():
    # feature = conditions

    def __init__(self):
        self.weather = None
        self.current = None
        self.temp = None

    def get_current_weather():
        pass

class TenDayForecast():
    # feature = forecast10day

    def __init__(self):
        self.ten_day = []

    def get_ten_day():
        pass

class Sun():
    # features = astronomy

    def __init__(self):
        self.sun_rise = None
        self.sun_set = None

    def get_sun():
        pass


class Alerts():
    # features = alerts

    def __init__(self):
        self.alerts = None

    def get_alerts():
        pass


class ActiveHurricanes():
    # feature = currenthurricane

    def __init__(self):
        self.name = []

    def get_canes():
        pass
