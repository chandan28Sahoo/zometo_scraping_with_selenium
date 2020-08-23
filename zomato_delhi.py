from selenium import webdriver
from bs4 import BeautifulSoup
import json
from pprint import pprint

driver=webdriver.Chrome(r"C:\Users\CHANDAN SAHU\Desktop\chromedriver")

for k in range(1,2025):
    link = "https://www.zomato.com/ncr/connaught-place-delhi-restaurants?page=" + str(k)
        # page_list.append(link)
    # print(link)
    driver.get(link)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    name_resturent=[]
    link=[]
    rating=[]
    r1_title=[]
    location=[]
    new_list=[]

    main_=soup.find("div",class_="col-s-16 search_results mbot")
    main=main_.find("section",id="search-results-container")
    m=main.find_all("a",class_="result-title hover_feedback zred bold ln24 fontsize0")
    ################################
    for i in m:
        name_resturent.append(i.text.strip())
    # print(name_resturent)
    # print(len(name_resturent))
    ###############################
    for i in m:
        if "href" in i.attrs:
            link.append(str(i.attrs["href"]))
    # print(link)
    # print(len(link))
    ################################
    list_of_facility = []
    a_title = main.find_all("div", class_="col-s-12")
    for i in a_title:
        a = i.find("div", class_="res-snippet-small-establishment mt5")
        facility = []
        try:
            b = a.find_all("a")
            for i in b:
                facility.append(i.text)
        except AttributeError:
            facility.append("nothing")
        list_of_facility.append(facility)
    # print(list_of_facility)
    # print(len(list_of_facility))

    rating_list=[]
    rating1=main.find_all("div",class_="col-s-12")
    for i in rating1:
        re=i.find_all('span', class_="rating-value")
        a=[]
        for j in re:
            a.append(j.text)
        rating_list.append(a)
    # print(rating_list)
    location_=main.find_all("div",class_="col-m-16 search-result-address grey-text nowrap ln22")
    for i in location_:
        b=i.text
        location.append(b)
    # print(location)

    cuisines_list=[]
    cuisines=main.find_all("div",class_="search-page-text clearfix row")
    for i in cuisines:
        a=i.find("div",class_="clearfix")
        b=a.find_all("a")
        sub_cuisines=[]
        for i in b:
            sub_cuisines.append(i.text)
        cuisines_list.append(sub_cuisines)
    # print(cuisines_list)

    cost_for_2=[]
    for i in cuisines:
        try:
            a = i.find("div", class_="res-cost clearfix").text.split()[-1]
            cost_for_2.append(a)
        except AttributeError:
            cost_for_2.append("")
    # print(cost_for_2)

    hour=[]
    for i in cuisines:
        try:
            a = i.find("div", class_="col-s-11 col-m-12 pl0 search-grid-right-text").text.strip()
            hour.append(a)
        except AttributeError:
            hour.append("no time")
    # print(hour)

    featured_list = []
    for i in cuisines:
        a = i.find("div", class_="res-collections clearfix")
        featured=[]
        try:
            b = a.find_all("a")
            for i in b:
                featured.append(i.text.strip())
        except AttributeError:
            pass
        featured_list.append(featured)
    # print(featured_list)

    discount_list=[]
    for i in cuisines:
        a = i.find("div", class_="res-offers clearfix")
        discount=[]
        try:
            b = a.find_all("a")
            for i in b:
                discount.append(i.text.strip())
        except AttributeError:
            discount.append("no discount")
        discount_list.append(discount)
    # print(discount_list)

    data_list=[]
    resturent_list = {}
    for i in range(0,len(link)):
        data = {}
        data[" url "]=link[i]
        data[" location "]=location[i]
        data[" rating "]=rating_list[i]
        data[" facility "]=featured_list[i]
        data[" cuisines "]=cuisines_list[i]
        data[" cost_for_two "]=cost_for_2[i]
        data[" hour "]=hour[i]
        data[" featured "]=featured_list[i]
        data[" discount "]=discount_list[i]
        # print(data)
        resturent_list[name_resturent[i]]=data
        data_list.append(resturent_list.copy())
    # pprint(resturent_list)
    pprint(data_list)

    with open('zomato_all_files/'+str(k)+'.json','w') as write_file:
        json.dump(data_list,write_file,indent=2)
        write_file.close()

