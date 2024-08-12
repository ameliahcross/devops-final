import unittest
from bs4 import BeautifulSoup

class TestIndexHtml(unittest.TestCase):
    def test_hola_mundo(self):
        with open('index.html') as f:
            soup = BeautifulSoup(f, 'html.parser')
            h1 = soup.find('h1').text
            self.assertEqual(h1, 'Hola Mundo')

if __name__ == '__main__':
    unittest.main()
