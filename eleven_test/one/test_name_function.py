import unittest
from eleven_test.one.name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('tom', 'jerry');
        self.assertEqual(formatted_name, 'Tom Jerry');
    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('tom', 'jerry', 'dog');
        self.assertEqual(formatted_name, 'Tom Dog Jerry');
unittest.main();


