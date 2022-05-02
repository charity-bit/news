from os import name
import unittest
from ..app.models import Source




class SourceTest(unittest.TestCase):
    '''
    Test class to test behavior of source class
    '''

    def setUp(self):
        '''
          Setup method that will run before every test
        '''
        # id,name,description,url,category,country
        self.new_source = Source('aftenposten','Aftenposten','Norges ledende nettavis med alltid oppdaterte nyheter innenfor innenriks, utenriks, sport og kultur.','https://www.aftenposten.no','general','no')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


