"""
CS5001, Fall 2022
Final Project: Professors' public information directory
Define functions to extract all professor home page urls from Mathmatics
Department of University of Illinois, and extract basic professors' information
from each professor's home page.
Xinyue Han
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


def get_js_soup(url):
    """ Helper function to get the HTML content with webdriver and parse the
        content.
        Parameters:
            url : string, a website url
        Returns :
            soup : BeautifulSoup object which contains website data
    """
    # uses Chromedriver to connect with the website
    options = Options()
    options.headless = True  # launch browser without UI
    driver = webdriver.Chrome('./chromedriver', options=options)
    driver.get(url)
    res_html = driver.execute_script('return document.body.innerHTML')
    soup = BeautifulSoup(res_html, 'html.parser')
    driver.close()
    return soup


def scrape_faculty_links_uoi(dir_url):
    """ Extracts all professor home page urls from the Directory Listing Page.
        Parameters:
            dir_url : string, department website url
        Returns :
            faculty_links : a list which contains professor home page urls
    """
    faculty_links = []
    faculty_base_url = 'https://math.illinois.edu'
    # call the helper function to extract data from this department website
    soup = get_js_soup(dir_url)
    # get all classes which contain the professor home page link
    profile_card = soup.find_all('article', class_='profile-card')
    for profile in profile_card:
        rel_link = profile.find('a')['href']  # get url
        # add base url since url returned is relative
        faculty_links.append(faculty_base_url + rel_link)
    return faculty_links


def scrape_home_page_uoi(fac_url):
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
    soup = get_js_soup(fac_url)
    # get the class contains fullname information
    profile_sec1 = soup.find('div', class_='l-bl block block-config-provider-'
                                           '-core block-plugin-id--page-title'
                                           '-block')
    if profile_sec1 is not None:
        find_name = profile_sec1.find('h1', class_='page__title')
        fullname = find_name.string.strip().replace('  ', ' ')
    # get the class contains email information
    profile_sec2 = soup.find('div', class_='field field-user--field-dircore'
                                           '-email field-formatter-email-mailto '
                                           'field-name-field-dircore-email '
                                           'field-type-email field-label-hidden '
                                           'has-single')
    if profile_sec2 is not None:
        item = profile_sec2.find('div', class_='field__item')
        email = item.find('a')['href'][7:]
    # get the class contains research interests information
    profile_sec3 = soup.find('div', class_='field field-user--field-dircore-'
                                           'research-areas field-formatter-'
                                           'entity-reference-label field-name'
                                           '-field-dircore-research-areas field'
                                           '-type-entity-reference field-label-'
                                           'above has-single')
    profile_sec4 = soup.find('div', class_='field field-user--field-dircore-'
                                           'research-areas field-formatter-'
                                           'entity-reference-label field-name'
                                           '-field-dircore-research-areas field'
                                           '-type-entity-reference field-label-'
                                           'above has-multiple')
    if profile_sec3 is not None:
        items = profile_sec3.find_all('div', class_='field__item')
        for item in items:
            research_interest = item.find('a').string
            research_interests.append(research_interest)
    if profile_sec4 is not None:
        items = profile_sec4.find_all('div', class_='field__item')
        for item in items:
            research_interest = item.find('a').string
            research_interests.append(research_interest)
    # convert the research interest list to string
    research_interests = ', '.join(filter(None, research_interests))
    return fullname, email, research_interests
