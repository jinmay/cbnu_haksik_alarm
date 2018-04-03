import os
import pyowm
import psycopg2


# settings.local ( fail )
owm_apikey = os.environ["OWM_APIKEY"]


try:
    conn = psycopg2.connect("dbname=rest_haksik") # connect to psql db
    cur = conn.cursor() # initialize cursor

    owm = pyowm.OWM(owm_apikey)
    observation = owm.weather_at_place('Cheongju,KR')
    weather = observation.get_weather()

    temperature_dict = weather.get_temperature('celsius') # convert Kelvin to celsius
    temperature = temperature_dict['temp']
    temperature = int(temperature)

    clouds = weather.get_clouds()
    humidity = weather.get_humidity()

    print("구름: {}\n습도: {}%".format(clouds, humidity))
    # print(temperature)

    # cur.execute("INSERT INTO weather_weather (temp) VALUES (%s, )", (temperature))
    SQL = "INSERT INTO weather_weather (temp, humidity, clouds) VALUES (%s, %s, %s);"
    data = (temperature, humidity, clouds)
    cur.execute(SQL, data)
    conn.commit()

finally:
    if conn:
        cur.close()
        conn.close()