import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from .models import (
                Main, Yangsung, Yangjin
            )


# week의 시작은 "일요일" / 인덱스: 1 입니다.

# 중문기숙사
def main_crawling(request):
    Main.objects.all().delete()
    main_url = 'https://dorm.chungbuk.ac.kr/sub05/5_2.php?type1=5&type2=2'
    main_response = requests.get(main_url, verify=False)
    main_html = BeautifulSoup(main_response.content, 'lxml', from_encoding="utf-8")
    main_menus = main_html.select('tr[id]')

    for day in range(7):
        breakfast = main_menus[day].find_all('td')[1].get_text("\n").strip()
        lunch = main_menus[day].find_all('td')[2].get_text("\n").strip()
        dinner = main_menus[day].find_all('td')[3].get_text("\n").strip()

        main = Main(day=day, breakfast=breakfast, lunch=lunch, dinner=dinner)
        main.save()

    return HttpResponse(status=200)

# 양성재
def sung_crawling(request):
    Yangsung.objects.all().delete()
    sung_url = 'https://dorm.chungbuk.ac.kr/sub05/5_2_tab2.php?type1=5&type2=2'
    sung_response = requests.get(sung_url, verify=False)
    sung_html = BeautifulSoup(sung_response.content, 'lxml', from_encoding="utf-8")
    sung_menus = sung_html.select('tr')[1:8]

    for day in range(7):
        breakfast = sung_menus[day].find_all('td')[1].get_text("\n").strip()
        lunch = sung_menus[day].find_all('td')[2].get_text("\n").strip()
        dinner = sung_menus[day].find_all('td')[3].get_text("\n").strip()

        sung = Yangsung(day=day, breakfast=breakfast, lunch=lunch, dinner=dinner)
        sung.save()

    return HttpResponse(status=200)

# 양진재
def jin_crawling(request):
    Yangjin.objects.all().delete()
    jin_url = 'https://dorm.chungbuk.ac.kr/sub05/5_2_tab3.php?type1=5&type2=2'
    jin_response = requests.get(jin_url, verify=False)
    jin_html = BeautifulSoup(jin_response.content, 'lxml', from_encoding="utf-8")
    jin_menus = jin_html.select('tr')[1:8]

    for day in range(7):
        breakfast = jin_menus[day].find_all('td')[1].get_text("\n").strip()
        lunch = jin_menus[day].find_all('td')[2].get_text("\n").strip()
        dinner = jin_menus[day].find_all('td')[3].get_text("\n").strip()

        jin = Yangjin(day=day, breakfast=breakfast, lunch=lunch, dinner=dinner)
        jin.save()

    return HttpResponse(status=200)