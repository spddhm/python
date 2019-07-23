import unittest
from eleven_test.two.employee import Employee
class EmployeeTest(unittest.TestCase):
    def test_give_default_raise(self):
        employee = Employee('s', 'd', 7000);
        self.assertEqual(employee.salary, 7000);
    def test_give_custom_raise(self):
        empplyee = Employee('s', 'd', 7000);
        empplyee.give_raise(3000)
        self.assertEqual(empplyee.salary, 10000)
unittest.main()


