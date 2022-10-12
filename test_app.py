import unittest
import app

class TestApp(unittest.TestCase):
    
    def test_time2text(self):
        self.assertEqual(app.time2text(1,00),'''One o'clock''')
        self.assertEqual(app.time2text(2,00),'''Two o'clock''')
        self.assertEqual(app.time2text(13,00),'''One o'clock''')
        self.assertEqual(app.time2text(13,10),'Ten past one')
        self.assertEqual(app.time2text(13,30),'Half past one')
        self.assertEqual(app.time2text(13,35),'Twenty five to two')
        self.assertEqual(app.time2text(13,55),'Five to two')

if __name__=='__main__':
    unittest.main()