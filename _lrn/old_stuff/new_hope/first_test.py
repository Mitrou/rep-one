#! /usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import selenium
from selenium import webdriver
import time


class TestBaseFlow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_1page_open_ch(self):
        self.driver.get("https://www.google.com.ua/")
        self.driver.implicitly_wait(10)
        self.assertIn("Google", self.driver.title)

    def test_1page_open_ch2(self):
        self.driver.get("https://www.returnofreckoning.com/")
        self.assertIn("Return", self.driver.title)

    def teardown(self):
        self.driver.quit()


# class TestBaseFlow2(unittest.TestCase):
#     def setUp(self):
#         self.driver2 = webdriver.Firefox()
#
#     def test_1page_open_ff(self):
#         self.driver2.get("https://www.google.com.ua/")
#         self.assertIn("Google", self.driver2.title)
#
#     def teardown(self):
#         self.driver2.quit()


# class TestBaseFlow3(unittest.TestCase):
#     def setUp(self):
#         self.driver3 = webdriver.Ie()
#
#     def test_1page_open_ie(self):
#         self.driver3.get("https://www.google.com.ua/")
#         self.assertIn("Google", self.driver3.title)
#
#     def teardown(self):
#         self.driver3.quit()

if __name__ == '__main__':
    unittest.main()
