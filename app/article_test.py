from os import name
import unittest
from models import article


Article = article.Article

class ArticleTest(unittest.TestCase):
    '''
    Test class to test behavior of article class
    '''

    def setUp(self):
        '''
          Setup method that will run before every test
        '''
        self.new_article = Article('"https://s.yimg.com/os/creatr-uploaded-images/2022-04/d4f7fc70-c4d6-11ec-bb67-a534341d9375','Hitting the Books: Dodge, Detroit and the Revolutionary Union Movement of 1968','After decades on the decline intro, America\'s labor movement is undergoing a massive renaissance with Starbucks, Amazon and Apple Store employees leading the way. Though the tech sector has only just begun basking in the newfound glow of collective bargaining…','2022-05-01T14:00:34Z','Engadget','https://www.engadget.com/hitting-the-books-fight-like-hell-kim-kelly-simon-and-schuster-140034896.html')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))


if __name__ == '__main__':
    unittest.main()
