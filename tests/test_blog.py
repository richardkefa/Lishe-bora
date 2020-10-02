import unittest
from app.models import Blog
from app import db


class BlogModelTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Blog class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_blog = Blog(1,'Python Must Be Crazy''Flask is Hard','29-09-2020', 1, 'Great piece')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))
