from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
import sys
from unittest import skip
from .base import FunctionTest


class ItemValidationTest(FunctionTest):

	def test_cannot_add_empty_list_items(self):
		
		self.browser.get(self.server_url)
		# inputbox = self.browser.find_element_by_id('id_new_item')
		# inputbox.send_keys('test not add empty Buy milk')
		# inputbox.send_keys(Keys.ENTER)

		# self.browser.implicitly_wait(3)

		# # inputbox = self.browser.find_element_by_id('id_new_item')
		# # inputbox.send_keys('Use peacock feathers to make a fly')
		# # inputbox.send_keys(Keys.ENTER)

		# self.check_for_row_in_list_table('1: Buy milk')
		# self.browser.implicitly_wait(3)

		self.browser.find_element_by_id('id_new_item').send_keys('\n')
		self.browser.implicitly_wait(3)

		error = self.browser.find_element_by_css_selector('.has-error')
		self.browser.implicitly_wait(3)

		self.assertEqual(error.text, "You can't have an empty list item")
		self.browser.implicitly_wait(10)

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('after blank Buy milk')
		inputbox.send_keys(Keys.ENTER)
		self.check_for_row_in_list_table('1:after blank Buy milk')

		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys(Keys.ENTER)

		error = self.browser.find_element_by_css_selector('.has-error')
		self.assertEqual(error.text, "You can't have an empty list item")

		self.browser.find_element_by_id('id_new_item').send_keys('Make tea')
		self.check_for_row_in_list_table('1:after blank Buy milk')
		self.check_for_row_in_list_table('2:Make tea')
		