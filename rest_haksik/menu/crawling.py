import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from .models import (
                Main, Yangjin, Yangsung, Crj,
                Galaxy,
            )


# 중문기숙사
def main_crawling(request):
    Main.objects.all().delete()
    main_url = 'https://dorm.chungbuk.ac.kr/sub05/5_2.php?type1=5&type2=2'
    main_response = requests.get(main_url, verify=False)
    main_html = BeautifulSoup(main_response.content, 'lxml', from_encoding="utf-8")
    main_menus = main_html.select('tr[id]')

    for day in range(7):
        main_menu = "{}\n\n[아침]\n{}\n\n[점심]\n{}\n\n[저녁]\n{}".format(main_menus[day].find_all('td')[0].get_text().strip(),
            main_menus[day].find_all('td')[1].get_text("\n").strip(),
            main_menus[day].find_all('td')[2].get_text("\n").strip(),
            main_menus[day].find_all('td')[3].get_text("\n").strip())

        main = Main(number = day, menu = main_menu)
        main.save()

    return HttpResponse(status=200)


# 양진재
def jin_crawling(request):
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

        jin = Yangjin(number = day, menu = jin_menu)
        jin.save()

    return HttpResponse(status=200)


# 양성재
def sung_crawling(request):
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

        sung = Yangsung(number = day, menu = sung_menu)
        sung.save()

    return HttpResponse(status=200)


# 청람재
def crj_crawling(request):
    Crj.objects.all().delete()
    crj_url = 'http://www.cbhscrj.kr/food/list.do?menuKey=39'
    crj_response = requests.get(crj_url)
    crj_html = BeautifulSoup(crj_response.content, 'lxml')
    crj_menus = crj_html.select('div.food_week_box')

    for day in range(7):
        crj_menu = "{}\n\n[아침]\n{}\n\n[점심]\n{}\n\n[저녁]\n{}".format(crj_menus[day].find_all('p')[0].get_text().strip(),
            crj_menus[day].find_all('p')[1].get_text().replace(',', "\n").strip(),
            crj_menus[day].find_all('p')[2].get_text().replace(',', "\n").strip(),
            crj_menus[day].find_all('p')[3].get_text().replace(',', "\n").strip())

        crj = Crj(number = day, menu = crj_menu)
        crj.save()

    return HttpResponse(status=200)


# 은하수식당
def galaxy_crawling(request):
    Galaxy.objects.all().delete()
    galaxy_url = 'http://coop.cbnu.ac.kr/m0304'
    galaxy_response = requests.get(galaxy_url)
    bsobj = BeautifulSoup(galaxy_response.content, 'lxml')

    tr_list = bsobj.select("table tbody tr")
    price = tr_list[1].select("td")[1].get_text()
    lunch_row = tr_list[1].select("td")[2:]
    dinner_row = tr_list[3].select("td")[2:]

    for index, (lunch, dinner) in enumerate(zip(lunch_row, dinner_row)):
        galaxy_menu = "[점심]\n{}\n\n[저녁]\n{}".format(lunch.get_text().strip(), dinner.get_text().strip())
        galaxy = Galaxy(number = index, menu = galaxy_menu)
        galaxy.save()

    return HttpResponse(status=200)
