import unittest
from .models import news
News = news.News

class NewsTest(unittest.TestCase):
    def setUp(self):
        self.new_news = News('Thesun.co.uk','Taxi ploughs into World Cup fans in Moscow leaving seven injured','Moscow police believe the driver may have lost control of the vehicle this afternoon','https://i2-prod.mirror.co.uk/incoming/article12730482.ece/ALTERNATES/s1200/Group-E-Brazil-vs-Switzerland-Rostov-On-Don-Russian-Federation-17-Jun-2018.jpg',2018-06-16)

        def test_instance(self):
            self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()