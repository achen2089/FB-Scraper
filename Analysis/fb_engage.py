from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
import selenium
import time
import matplotlib.pyplot as plt

import pandas as pd
import time
from selenium.webdriver import Chrome
from datetime import datetime

from datetime import datetime
import schedule
import time

def scrape_FB(url):
    chrome_options = selenium.webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = Chrome('../chromedriver', options=chrome_options) 

    browser.get(url)

    t_end = time.time() + 1*60
    while time.time() < t_end:
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(2)

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
        #    print("photo")
            content_type.append("photo")
        elif ("videos" in link):
        #   print("video")
            content_type.append("video")
        else:
        #    print("post")
            content_type.append("post")
        
        try:
        #    print(elem.find_element_by_class_name("_81hb").text, "likes")
            likes.append(elem.find_element_by_class_name("_81hb").text)
        except Exception as exception:
            likes.append("0")
            
            
        try:
        #    print(elem.find_element_by_class_name("_3hg-").text)
            comments.append(elem.find_element_by_class_name("_3hg-").text)
        except Exception as exception:
            comments.append("0 Comments")
            
            
        try:
        #    print(elem.find_element_by_class_name("_355t").text)
            shares.append(elem.find_element_by_class_name("_355t").text)
        except Exception as exception:
            shares.append("0 Shares")

    df = pd.DataFrame({"date":date,"content_type":content_type, "likes":likes, "comments":comments, "shares":shares})
    #df.to_csv("SCU_FB.csv")
    return df


