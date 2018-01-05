import psycopg2
import os
import pyowm

# settings.local 에서 불러오고 싶은데 
# 나름대로 해봐도 못하겠어서 급한대로 아래와 같이 사용
owm_apikey = os.environ["OWM_APIKEY"] 
owm = pyowm.OWM(owm_apikey)

observation = owm.weather_at_place('Cheongju,KR')
w = observation.get_weather()

temperature = w.get_temperature('celsius')
print(temperature['temp'])