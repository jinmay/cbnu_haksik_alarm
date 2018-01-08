import requests
from bs4 import BeautifulSoup
from django.http import HttpResponse
from .models import (
                Main, Yangjin, Yangsung, Crj,
                Galaxy,
            )


# 학교기숙사 + 청람재 크롤링 사전준비
def ready_crawling(dorm):
    dorm_in_advanced = {
        'main': {
            'db': 'Main.objects.all().delete()',
            'url': 'https://dorm.chungbuk.ac.kr/sub05/5_2.php?type1=5&type2=2',
        },
        'yangjin': {
            'db': 'Yangjin.objects.all().delete()',
            'url': 'https://dorm.chungbuk.ac.kr/sub05/5_2_tab3.php?type1=5&type2=2',
        },
        'yangsung': {
            'db': 'Yangsung.objects.all().delete()',
            'url': 'https://dorm.chungbuk.ac.kr/sub05/5_2_tab2.php?type1=5&type2=2',
        },
        'crj': {
            'db': 'Crj.objects.all().delete()',
            'url': 'http://www.cbhscrj.kr/food/list.do?menuKey=39',
        },
    }

    dorm_in_advanced[dorm]['db']
    url = dorm_in_advanced[dorm]['url']
    response = requests.get(url, verify=False)
    html = BeautifulSoup(response.content, 'lxml', from_encoding="utf-8")
    if dorm == 'main':
        menus = html.select('tr[id]')
    elif dorm == 'crj':
        menus = html.select('div.food_week_box')
    else:
        menus = html.select('tr')[1:8]
    
    return menus


# 중문기숙사
def main_crawling(request):
    menus = ready_crawling('main')

    for day in range(7):
        main_menu = "{}\n\n[아침]\n{}\n\n[점심]\n{}\n\n[저녁]\n{}".format(menus[day].find_all('td')[0].get_text().strip(),
            menus[day].find_all('td')[1].get_text("\n").strip(),
            menus[day].find_all('td')[2].get_text("\n").strip(),
            menus[day].find_all('td')[3].get_text("\n").strip())

        main = Main(number = day, menu = main_menu)
        main.save()

    return HttpResponse(status=200)


# 양진재
def jin_crawling(request):
    menus = ready_crawling('yangjin')

    for day in range(6):
        jin_menu = "{}\n\n[아침]\n{}\n\n[점심]\n{}\n\n[저녁]\n{}".format(menus[day].find_all('td')[0].get_text().strip(),
            menus[day].find_all('td')[1].get_text("\n").strip(),
            menus[day].find_all('td')[2].get_text("\n").strip(),
            menus[day].find_all('td')[3].get_text("\n").strip())

        jin = Yangjin(number = day, menu = jin_menu)
        jin.save()

    return HttpResponse(status=200)


# 양성재
def sung_crawling(request):
    menus = ready_crawling('yangsung')

    for day in range(6):
        sung_menu = "{}\n\n[아침]\n{}\n\n[점심]\n{}\n\n[저녁]\n{}".format(menus[day].find_all('td')[0].get_text().strip(),
            menus[day].find_all('td')[1].get_text("\n").strip(),
            menus[day].find_all('td')[2].get_text("\n").strip(),
            menus[day].find_all('td')[3].get_text("\n").strip())

        sung = Yangsung(number = day, menu = sung_menu)
        sung.save()

    return HttpResponse(status=200)


# 청람재
def crj_crawling(request):
    menus = ready_crawling('crj')

    for day in range(7):
        crj_menu = "{}\n\n[아침]\n{}\n\n[점심]\n{}\n\n[저녁]\n{}".format(menus[day].find_all('p')[0].get_text().strip(),
            menus[day].find_all('p')[1].get_text().replace(',', "\n").strip(),
            menus[day].find_all('p')[2].get_text().replace(',', "\n").strip(),
            menus[day].find_all('p')[3].get_text().replace(',', "\n").strip())

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
