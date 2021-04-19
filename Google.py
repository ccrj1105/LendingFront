# coding=utf-8
import sys,unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import os

class LendingFrontSearch(unittest.TestCase):

	def setUp(lending):
		lending.driver = webdriver.Chrome(ChromeDriverManager().install())

	def test_search_keyword_assert(lending):
		driver = lending.driver
		driver.get("https://www.google.com/")
		txt_searchBox = driver.find_element_by_name("q")
		keyword = "djfasdjflkdajslfjdasljf12313"
		txt_searchBox.send_keys(keyword)
		txt_searchBox.send_keys(Keys.RETURN)
		assert driver.find_element_by_xpath("//h3").is_displayed() == False



	def tearDown(lending):
		lending.driver.close()

if __name__ == "__main__":
	unittest.main()
