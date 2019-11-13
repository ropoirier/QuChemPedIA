#!/usr/bin/python2.6
# -*- coding: UTF-8 -*-
import unittest
from selenium import webdriver

class TestCesiSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_results_page_shows(self):
        self.driver.get("http://www.cesi.fr")
        select = Select(self.driver.find_element_by_id('form_1579'))
        select.select_by_value("Informatique et systèmes d'information")
        btn = self.driver.find_element_by_css_selector("input[type=\"submit\"]")
        btn.click()

        page_url = self.driver.current_url
        page_title = self.driver.find_element_by_css_selector(".txtblancRechercheTitre").text

        self.assertEqual(page_url, 'http://www.cesi.fr/recherche-formulaire-portail.asp')
        self.assertEqual(page_title, u'VOTRE RÉSULTAT, VOTRE RECHERCHE')

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
