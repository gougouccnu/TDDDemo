from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
import sys
from unittest import skip
from .base import FunctionTest


class ItemValidationTest(FunctionTest):

	def test_cannot_add_empty_list_items(self):
		
		self.browser.get(self.server_url)
		self.browser.find_element_by_id('id_new_item').send_keys('\n')

		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error, "You can't have a empty list item")

		self.browser.find_element_by_id('id_new_item').send_keys('Buy milk')
		self.check_for_row_in_list_table('1: Buy milk')

		self.browser.find_element_by_id('id_new_item').send_keys('\n')

		error = self.browser.find_css_selector('.has-error')
		self.assertEqual(error, "You can't have a empty list item")

		self.browser.find_element_by_id('id_new_item').send_keys('Make tea')
		self.check_for_row_in_list_table('1: Buy milk')
		self.check_for_row_in_list_table('2: Make tea')
		