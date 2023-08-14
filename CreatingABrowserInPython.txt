#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: maxschallwig
"""

url = "https://finance.yahoo.com/quote/AAPL/key-statistics?p=AAPL"

from selenium import webdriver

browser = webdriver.PhantomJS(executable_path = "/usr/local/bin/phantomjs")
browser.get(url)
browser.quit()