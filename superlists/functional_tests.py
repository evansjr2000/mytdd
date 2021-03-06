from selenium import webdriver
import unittest

class NewVisitorTest ( unittest.TestCase ):

    def setUp ( self ):
        self.browser = webdriver.Firefox ()
        self.browser.implicitly_wait(10)

    def tearDown ( self ): #
        self.browser.quit () 

    def test_can_start_a_list(self):
       self.browser.get('http://localhost:8000')
       self.assertIn('To Do',self.browser.title)

if __name__ == '__main__':
    unittest.main(warnings='ignore')

