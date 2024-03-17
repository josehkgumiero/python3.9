import unittest

class Widget:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return f"{self.name} {self.size}"
    
    def get_size(self):
        return self.size
    
    def resize(self, new_size):
        self.size = new_size

class DefaultWidgetSizeTestCase(unittest.TestCase):
    def test_default_widget_size_50_50(self):
        widget = Widget('The Default Widget Size Test Case', (50, 50))
        self.assertEqual(widget.get_size(), (50, 50))

    def test_default_widget_size_40_40(self):
        widget = Widget('The Default Widget Size Test Case', (40, 40))
        self.assertEqual(widget.get_size(), (50, 50))

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget', (30, 30))

    def test_default_widget_size(self):
        self.assertEqual(self.widget.get_size(), (50,50),
                         'incorrect default size')

    def test_widget_resize(self):
        self.widget.resize((99,150))
        self.assertEqual(self.widget.get_size(), (100,150),
                         'wrong size after resize')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_default_widget_size'))
    suite.addTest(WidgetTestCase('test_widget_resize'))
    return suite

if __name__ == '__main__':
    unittest.main()
    runner = unittest.TextTestRunner()
    runner.run(suite())

#
# python ./unittest/test_assert2_widget_test_case.py -v