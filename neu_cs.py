"""
CS5001, Fall 2022
Final Project: Professors' public information directory
Define functions to extract all professor home page urls from Khoury College
of Computer Sciences of Northeastern University, and extract basic professors'
information from each professor's home page.
Xinyue Han
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


def get_js_soup(url, dynamic_web):
    """ Helper function to get the HTML content with webdriver and parse the
        content.
        Parameters:
            url : string, a website url
            dynamic_web : boolean, indicates whether a website is dynamic
                          loading or not
        Returns :
            soup : BeautifulSoup object which contains website data
    """
    # uses Chromedriver to connect with the website
    options = Options()
    options.headless = True     # launch browser without UI
    driver = webdriver.Chrome('./chromedriver', options=options)
    driver.get(url)
    # scroll to the bottom for dynamic website
    cur_height = driver.execute_script('return document.body.scrollHeight')
    while dynamic_web:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(5)
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == cur_height:
            break
        cur_height = new_height
    res_html = driver.execute_script('return document.body.innerHTML')
    soup = BeautifulSoup(res_html, 'html.parser')
    driver.close()
    return soup


def scrape_faculty_links_neu(dir_url):
    """ Extracts all professor home page urls from Khoury of Computer Sciences
        department page.
        Parameters:
            dir_url : string, department website url
        Returns :
            faculty_links : a list which contains professor home page urls
    """
    faculty_links = []
    # call the helper function to extract data from this department website
    soup = get_js_soup(dir_url, True)
    # get all classes which contain the professor home page link
    person_blocks = soup.find_all('div', class_='person-block grid-25 '
                                                'mobile-grid-50 grid-parent '
                                                'background-main animator '
                                                'on-screen interactive')
    # traverse all the professors' person_block classes
    for person in person_blocks:
        home_page_link = person.find('a')['href']  # find the url of home page
        faculty_links.append(home_page_link)   # append to the list
    return faculty_links


def scrape_home_page_neu(fac_url):
    """ Extracts basic professors' information from each professor's home page.
        Parameters:
            fac_url : string, professor's home page url
        Returns :
            fullname : string, professor's full name
            email : string, professor's email
            research_interests : string, professor's research interest
                                 separates by comma
    """
    fullname = ''
    email = ''
    research_interests = []
    # call the helper function to extract data from this professor's home page
    soup = get_js_soup(fac_url, False)
    # get the class contains fullname and email information
    profile_sec1 = soup.find('div', class_='grid-30 hero-content grid-parent'
                                           ' grid-container')
    if profile_sec1 is not None:
        find_name = profile_sec1.find('div', class_='headline')
        fullname = find_name.string.strip()  # find professor's fullname
        extras = profile_sec1.find('div', class_='extras')
        if extras.find('a') is not None:
            email = extras.find('a')['href'][7:]  # find professor's email
    # get the class contains research interests information
    profile_sec2 = soup.find('div', class_='template-Glass-Moon-Generic Small '
                                           'Xsmall Default Optionx3 template '
                                           'enable-rich')
    if profile_sec2 is not None:
        all_headers = profile_sec2.find_all('h2')
        for header in all_headers:
            try:
                # find 'h2' that have text is 'research interests'
                if header.string.lower() == 'research interests':
                    ul = header.find_next()
                    lis = ul.find_all('li')
                    for li in lis:
                        # append all research interests to the list
                        research_interests.append(li.string)
                    break
            # uses exception to deal with the span text in headers
            except AttributeError or TypeError:
                # find 'h2' that have text is 'research interests'
                if header.find('span').string.lower() == 'research interests':
                    ul = header.find_next('ul')
                    lis = ul.find_all('li')
                    for li in lis:
                        # append all research interests to the list
                        research_interests.append(li.find('span').string)
                    break
            finally:
                continue
    # convert the research interest list to string
    research_interests = ', '.join(filter(None, research_interests))
    return fullname, email, research_interests
