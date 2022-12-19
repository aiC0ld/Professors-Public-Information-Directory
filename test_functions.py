"""
CS5001, Fall 2022
Final Project: Professors' public information directory
Uses unittest.TestCase to test functions of this project.
Xinyue Han
"""

from neu_cs import *
from uoi_math import *
import unittest

neu_dir_url = 'https://www.khoury.northeastern.edu/about/people/'
neu_dir_url_first = 'https://www.khoury.northeastern.edu/people/anis-abdulle/'

uoi_dir_url = 'https://math.illinois.edu/directory/faculty'
uoi_dir_url_first = 'https://math.illinois.edu/directory/profile/sahlgren'

neu_fac_url1 = 'https://www.khoury.northeastern.edu/people/mamoun-abu-samaha/'
research_interests1 = 'Mobility, Cybersecurity, Artificial intelligence'
neu_fac_url2 = 'https://www.khoury.northeastern.edu/people/divya-chaudhary/'
research_interests2 = 'Cloud computing, Load scheduling, Machine learning, ' \
                      'Systems and networking'
uoi_fac_url = 'https://math.illinois.edu/directory/profile/sahlgren'
research_interests3 = 'Number Theory'


# class for testing functions
class TestGetData(unittest.TestCase):
    # test scrape_faculty_links_neu function
    def test_scrape_faculty_links_neu(self):
        fac_links = scrape_faculty_links_neu(neu_dir_url)
        # test expect faculty numbers of Khoury of Northeastern University
        self.assertEqual(len(fac_links), 435)
        # test the first faculty home page link
        self.assertEqual(fac_links[0], neu_dir_url_first)

    # test scrape_faculty_links_uoi function
    def test_scrape_faculty_links_uoi(self):
        fac_links = scrape_faculty_links_uoi(uoi_dir_url)
        # test expect faculty numbers of Math Department of University of Illinois
        self.assertEqual(len(fac_links), 162)
        # test the first faculty home page link
        self.assertEqual(fac_links[0], uoi_dir_url_first)

    # test scrape_faculty_page_neu function
    def test_scrape_faculty_page_neu(self):
        # test research interests without <span> of Northeastern University
        self.assertEqual(scrape_home_page_neu(neu_fac_url1),
                         ('Mamoun Abu-Samaha', 'mamoun@northeastern.edu',
                          research_interests1))
        # test research interests with <span> of Northeastern University
        self.assertEqual(scrape_home_page_neu(neu_fac_url2),
                         ('Divya Chaudhary', 'd.chaudhary@northeastern.edu',
                          research_interests2))

    # test test_scrape_faculty_page_uoi function
    def test_scrape_faculty_page_uoi(self):
        # test a simple case of one home page of University of Illinois
        self.assertEqual(scrape_home_page_uoi(uoi_fac_url),
                         ('Scott Ahlgren', 'sahlgren@illinois.edu',
                          research_interests3))


if __name__ == '__main__':
    unittest.main(verbosity=2)
