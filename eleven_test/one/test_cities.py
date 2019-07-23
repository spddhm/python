
# from eleven_test.one.city_functions import get_city_name
# def test_city_country():
#     while True:
#         cityname = input("input cityname: ");
#         if cityname == 'q':
#             break;
#         countyname = input("input countyname: ");
#         if countyname == 'q':
#             break;
#         city = get_city_name(cityname,'china');
#         print(city)
#
# test_city_country();


# 练习1
import unittest
from eleven_test.one.city_functions import get_city_name
class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        resultname = get_city_name('shenzhen', 'china');
        self.assertEqual(resultname, 'Shenzhen China');
    def test_city_country_population(self):
        resultname = get_city_name('shenzhen', 'china', '30000000');
        self.assertEqual(resultname, 'Shenzhen, China - population 30000000')
unittest.main();

















