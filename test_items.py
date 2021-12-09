import pytest
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestItem():
    
    def test_item_page_should_contain_add_button(self, browser):
    
        browser.get(link)
        time.sleep(1)
        ele = None
        try:
            ele = browser.find_element_by_css_selector(".btn-add-to-bsket")
        except NoSuchElementException:
            assert ele != None, "Add to basket button is missing"
