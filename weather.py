from endpoint import Current, TenDayForcast, Sun, Alerts, ActiveHurricanes
import re


def __main__():
    zip_code = input("Please enter a 5 digit zipcode: ")
    if re.match(r'\d{5}', zip_code):
        current = Current.get_current_weather()
        10_day = TenDayForcast.get_ten_day()
        sun = Sun.get_sun()
        alerts = Alerts.get_alerts()
        hurricanes = ActiveHurricanes.get_canes()
    else:
        print('Please enter a valid area code!')

if __name__ == "__main__":
    main()
