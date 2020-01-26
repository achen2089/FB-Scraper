import pandas as pd
import time
from selenium.webdriver import Chrome
from datetime import datetime

from datetime import datetime
import schedule
import time
import numpy

from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import selenium
import time
import matplotlib.pyplot as plt
import matplotlib


matplotlib.use('Agg')

def scrape(link):
    print("Scrapping!!!")

    chrome_options = selenium.webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = Chrome('app/chromedriver', options=chrome_options) 
        
    
    browser.get(link)
    #browser.get("https://en-gb.facebook.com/pg/SantaClaraUniversity/posts/")

    print("=====Done loading=====")


    t_end = time.time() + 1*90
    while time.time() < t_end:
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)


    print("=====Done scrolling=====")

    lists = browser.find_elements_by_class_name("_5pcr")


    content_type = []
    likes = []
    comments = []
    date = []
    shares = []


    for elem in lists:
        
        link= elem.find_element_by_class_name("_5pcq").get_attribute("href")
        try:
            #print(elem.find_element_by_class_name("_5pcq").find_element_by_tag_name("abbr").get_attribute("title"))
            date.append(elem.find_element_by_class_name("_5pcq").find_element_by_tag_name("abbr").get_attribute("title"))
        except Exception as exception:
            print("bad post")
            date.append(date[-1])
            #print(elem.find_element_by_class_name("_5pcq").find_element_by_class_name("z_c3pyo1brp").get_attribute("title"))
            #date.append(elem.find_element_by_class_name("_5pcq").find_element_by_class_name("z_c3pyo1brp").get_attribute("title"))
        
        if ("photos" in link):
    #         print("photo")
            content_type.append("photo")
        elif ("videos" in link):
    #         print("video")
            content_type.append("video")
        else:
    #         print("post")
            content_type.append("post")
        
        try:
    #         print(elem.find_element_by_class_name("_81hb").text, "likes")
            likes.append(elem.find_element_by_class_name("_81hb").text)
        except Exception as exception:
    #         print(0)
            likes.append(0)
            
            
        try:
    #         print(elem.find_element_by_class_name("_3hg-").text)
            comments.append(elem.find_element_by_class_name("_3hg-").text)
        except Exception as exception:
    #         print(0)
            comments.append(0)
            
            
        try:
    #         print(elem.find_element_by_class_name("_355t").text)
            shares.append(elem.find_element_by_class_name("_355t").text)
        except Exception as exception:
    #         print(0)
            shares.append(0)
            
        #print()


    df= pd.DataFrame({"date":date,"content_type":content_type, "likes":likes, "comments":comments, "shares":shares})

    df.date = pd.to_datetime(df.date)
    df.likes = pd.to_numeric(df.likes)
    df.comments = pd.to_numeric(df.comments.str[0])
    df.shares = pd.to_numeric(df.shares.str[0])
    df.fillna(0, inplace = True)

    df = df[df.date.dt.year==2019]


    post_data = df
    num_photo = post_data.groupby('content_type').content_type.count()[0]
    num_post = post_data.groupby('content_type').content_type.count()[1]
    num_video = post_data.groupby('content_type').content_type.count()[2]
    labels = ['Photos', 'Posts', 'Videos']
    sizes = [num_photo, num_post, num_video]
    colors = ['#86ffd5', '#ffd586', '#ff86d9']
    explode = (0, 0, 0)
    # plt.title('Post breakdown')
    plt.pie(sizes, explode=explode, labels=labels, colors=colors,
    autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.savefig('app/static/images/post_type_breakdown.png')
    plt.clf()



    df.groupby(df.date.dt.month).sum()[["comments","shares"]].plot()
    plt.title("Comments and Shares by Month", size=15)
    plt.xlabel("Month", size=15)
    plt.ylabel("Amount", size=15);

    plt.savefig("app/static/images/comments_shares.png")
    plt.clf()

    df.groupby(df.date.dt.month).sum()[["likes"]].plot()
    plt.title("Total likes by Month", size=15)
    plt.xlabel("Month", size=15)
    plt.ylabel("# Likes", size=15);
    plt.savefig("app/static/images/likes.png")
    plt.clf()





