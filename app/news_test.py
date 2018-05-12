import unittest #importing the unittest module
from .models import news #import the news.py file

News = news.News #we get the news class

class NewsTest(unittest.TestCase)   
#We create a test class. 
    def setUp(self): #setup method will be used as 'data' that fit ur parameters. Must be done before the tests

        self.new_news = News('TheStreet.com, Stephen Guilfoyle, Nvidia: These Guys Are Playing For Keeps, CEO Jensen Huang said :We had a strong quarter with growth across every platform....NVDA, "https://www.thestreet.com/investing/nvidia-these-guys-are-playing-for-keeps-14586993, http://s.thestreet.com/files/tsc/v2008/photos/contrib/uploads/302a9435-31d2-11e8-b78e-01593ca03ebe.png, 2018-05-11T13:00:21Z')

    def test_instance(self): #this is a testcase that uses isinstance  to check if the object is an instance of the parent class.
        self.assertTrue(isinstance(self.new_news, News))

if __name__ == '__main__':
    unittest.main()
