import os
import pyowm
import psycopg2


# settings.local 에서 불러오고 싶은데 
# 나름대로 해봐도 못하겠어서 급한대로 아래와 같이 사용
owm_apikey = os.environ["OWM_APIKEY"]


try:
    conn = psycopg2.connect("dbname=rest_haksik") # psql db 연결하고
    cur = conn.cursor() # cursor 생성하고

    owm = pyowm.OWM(owm_apikey)
    observation = owm.weather_at_place('Cheongju,KR')
    weather = observation.get_weather()

    temperature_dict = weather.get_temperature('celsius') # 기본값은 켈빈온도라서 섭씨로 바꿔주어야 함
    temperature = temperature_dict['temp']
    temperature = int(temperature)
    # print(temperature)

    # cur.execute("INSERT INTO weather_weather (temp) VALUES (%s, )", (temperature)) # 온도 집어넣기!!

    SQL = "INSERT INTO weather_weather (temp) VALUES (%s);"
    data = (temperature, )
    cur.execute(SQL, data) # 온도 집어넣기!!
    conn.commit()

finally:
    if conn:
        cur.close()
        conn.close()