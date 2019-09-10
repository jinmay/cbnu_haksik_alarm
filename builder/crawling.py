import requests
from django.http import HttpResponse
from bs4 import BeautifulSoup
from .models import CentralDorm, Yangsung, Yangjin

# 중문기숙사
def central(request):
    CentralDorm.objects.all().delete()
    url = 'https://dorm.chungbuk.ac.kr/sub05/5_2.php?type1=5&type2=2'
    response = requests.get(url, verify=False)
    html = BeautifulSoup(response.content, 'lxml', from_encoding="utf-8")
    menus = html.select('tr[id]')

    for day in range(7):
        main_menu = "{}\n\n[아침]\n{}\n\n[점심]\n{}\n\n[저녁]\n{}".format(menus[day].find_all('td')[0].get_text().strip(),
            menus[day].find_all('td')[1].get_text("\n").strip(),
            menus[day].find_all('td')[2].get_text("\n").strip(),
            menus[day].find_all('td')[3].get_text("\n").strip())

        main = CentralDorm(day=day, menu=main_menu)
        main.save()

    return HttpResponse(status=200)

# 양성재
def yangsung(request):
    Yangsung.objects.all().delete()
    sung_url = 'https://dorm.chungbuk.ac.kr/sub05/5_2_tab2.php?type1=5&type2=2'
    sung_response = requests.get(sung_url, verify=False)
    sung_html = BeautifulSoup(sung_response.content, 'lxml', from_encoding="utf-8")
    sung_menus = sung_html.select('tr')[1:8]

    for day in range(7):
        sung_menu = "{}\n\n[아침]\n{}\n\n[점심]\n{}\n\n[저녁]\n{}".format(sung_menus[day].find_all('td')[0].get_text().strip(),
            sung_menus[day].find_all('td')[1].get_text("\n").strip(),
            sung_menus[day].find_all('td')[2].get_text("\n").strip(),
            sung_menus[day].find_all('td')[3].get_text("\n").strip())

        sung = Yangsung(day=day, menu=sung_menu)
        sung.save()

    return HttpResponse(status=200)

# 양진재
def yangjin(request):
    Yangjin.objects.all().delete()
    jin_url = 'https://dorm.chungbuk.ac.kr/sub05/5_2_tab3.php?type1=5&type2=2'
    jin_response = requests.get(jin_url, verify=False)
    jin_html = BeautifulSoup(jin_response.content, 'lxml', from_encoding="utf-8")
    jin_menus = jin_html.select('tr')[1:8]

    for day in range(7):
        jin_menu = "{}\n\n[아침]\n{}\n\n[점심]\n{}\n\n[저녁]\n{}".format(jin_menus[day].find_all('td')[0].get_text().strip(),
            jin_menus[day].find_all('td')[1].get_text("\n").strip(),
            jin_menus[day].find_all('td')[2].get_text("\n").strip(),
            jin_menus[day].find_all('td')[3].get_text("\n").strip())

        jin = Yangjin(day=day, menu=jin_menu)
        jin.save()

    return HttpResponse(status=200)