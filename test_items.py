import pytest
import time

from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestItem():
    
    def test_item_page_should_contain_add_button(self, browser):
        browser.get(link)
        time.sleep(5)
        assert browser.find_element_by_css_selector(".btn-add-to-basket")
