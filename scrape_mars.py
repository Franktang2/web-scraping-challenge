#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import pandas as pd
import os
from bs4 import BeautifulSoup as bs
import requests


# # NASA Mars News


def mars_news(browser):

    url1 = "https://mars.nasa.gov/news/"
    response1 = requests.get(url1)
    soup = BeautifulSoup(response1.text, 'html.parser')
    try:
        #print(soup.prettify())
        results_title = soup.find_all("div", class_="content_title")
        #print(results_title)
        results_p = soup.find_all('div', class_="rollover_description_inner")
        
    except:
        return None, None
    return results_title[0].text, results_p[0].text

# # JPL Mars Space Images - Featured Image

def mars_image(browser):

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url)
    image_button = browser.find_by_id("full_image")
    image_button.click()
    browser.is_element_present_by_text("more info", wait_time=1)
    more_info_element = browser.find_link_by_partial_text("more info")
    more_info_element.click()
    html = browser.html
    image_soup = BeautifulSoup(html, "html.parser")
    try:
        img_url = image_soup.select_one("figure.lede a img").get("src")
        #img_url
        img_url = f"https://www.jpl.nasa.gov{img_url}"
    except:
        AttributeError:
        return None
    return img_url




# # Mars Weather

def mars_weather(browser):

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://twitter.com/marswxreport?lang=en"
    browser.visit(url)
    html = browser.html
    weather_soup = BeautifulSoup(html, "html.parser")
    mars_weather_tweet = weather_soup.find("div", 
                                       attrs={
                                           "class": "tweet", 
                                            "data-name": "Mars Weather"
                                        })
    mars_weather = mars_weather_tweet.find("p", "tweet-text").get_text()
    #print(mars_weather)
    return mars_weather




# # Mars Facts

def mars_facts(browser):

    pandas_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(pandas_url)
    #tables
    #type(tables)
    df = tables[0]
    #df.head()
    df.columns=["Description", "Value"]
    df.set_index("Description", inplace=True)
    return df





# # Mars Hemispheres

def mars_hemispheres(browser):

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url)

    hemisphere_image = []
    links = browser.find_by_css("a.product-item h3")
    for item in range(len(links)):
        hemisphere = {}
    
        browser.find_by_css("a.product-item h3")[item].click()   

        sample_element = browser.find_link_by_text("Sample").first
        hemisphere["img_url"] = sample_element["href"]

        hemisphere["title"] = browser.find_by_css("h2.title").text

        hemisphere_image.append(hemisphere)

        browser.back()

    return hemisphere_image


def scrape():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)
    news_title, news_paragraph = mars_news(browser)
    img_url = mars_image(browser)
    mars_weather = mars_weather(browser)
    facts = mars_facts()
    hemisphere_image_urls = mars_hemisphere(browser)

    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": img_url,
        "weather": mars_weather,
        "facts": facts,
        "hemispheres": hemisphere_image_urls,
    }
    browser.quit()
    return data 

if __name__ == "__main__":
    print(scrape_all())



