#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: maxschallwig
"""

from selenium import webdriver


#http://chromedriver.chromium.org/downloads

options = webdriver.ChromeOptions() 
options.add_argument('headless') 
pathToChromeDriver = ""
driver = webdriver.Chrome(executable_path = pathToChromeDriver,
                          options=options)

#browser = webdriver.PhantomJS() 

driver.quit()