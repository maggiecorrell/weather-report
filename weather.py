from endpoint import Weather, Current, TenDayForecast, Sun, Alerts, ActiveHurricanes
import re


def main():
    zip_code = input("Please enter a 5 digit zipcode: ")
    if re.match(r'\d{5}', zip_code):
        current = Current.get_current_weather()
        ten_day = TenDayForecast.get_ten_day()
        sun = Sun.get_sun()
        alerts = Alerts.get_alerts()
        hurricanes = ActiveHurricanes.get_canes()
    else:
        print('Please enter a valid area code!')


if __name__ == "__main__":
    main()
