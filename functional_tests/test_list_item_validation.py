from selenium import webdriver
from selenium.webdriver.common.keys import Keys  
import sys
from unittest import skip
from .base import FunctionTest


class ItemValidationTest(FunctionTest):

	
	def test_cannot_add_empty_list_items(self):
		self.fail('write me!')

		