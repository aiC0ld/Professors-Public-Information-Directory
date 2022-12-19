"""
CS5001, Fall 2022
Final Project: Professors' public information directory
Call the function that defined in neu_cs.py and uoi_math.py. Get professors'
public information such as fullname, email, research interests. Finally, dumps
these information to a Json called data.json.
Xinyue Han
"""

from neu_cs import *
from uoi_math import *
import json

output = []

# url of Khoury College of Computer Sciences department website
dir_url = 'https://www.khoury.northeastern.edu/about/people/'
# extracts all professors' home page link by scrape_faculty_links_neu function
faculty_links = scrape_faculty_links_neu(dir_url)
# traverse the list of home page urls
for i in faculty_links:
    # extracts professor's basic information by scrape_home_page_neu function
    fullname, email, research_interests = scrape_home_page_neu(i)
    # stores every professor's information in a dictionary which has 5 keys
    dictionary = {'name': fullname, 'email': email,
                  'research_interests': research_interests,
                  'university': 'Northeastern University',
                  'department': 'CS'}
    output.append(dictionary)


# url of the website of Mathmatics Department of UoI
dir_url = 'https://math.illinois.edu/directory/faculty'
# get all professors' home page link by scrape_faculty_links_uoi function
faculty_links = scrape_faculty_links_uoi(dir_url)
# traverse the list of home page urls
for i in faculty_links:
    # extracts professor's basic information by scrape_home_page_uoi function
    fullname, email, research_interests = scrape_home_page_uoi(i)
    # stores every professor's information in a dictionary which has 5 keys
    dictionary = {'name': fullname, 'email': email,
                  'research_interests': research_interests,
                  'university': 'University of Illinois',
                  'department': 'Math'}
    output.append(dictionary)

# dumps the output to a Json called data.json
with open("data.json", "w") as output_file:
    json_obj = json.dumps(output, indent=5)
    output_file.write(json_obj)
