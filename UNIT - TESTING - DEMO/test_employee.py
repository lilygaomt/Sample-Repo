import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def test_email(self):
        emp_1 = Employee("Lokesh", "Sharma", 50000)
        emp_2 = Employee("John", "Smith", 60000)
        self.assertEqual(emp_1.email, "Lokesh.Sharma@email.com")
        self.assertEqual(emp_2.email, "John.Smith@email.com")
        emp_1.first = "John"
        emp_2.first = "Jane"
        self.assertEqual(emp_1.email, "John.Sharma@email.com")
        self.assertEqual(emp_2.email, "Jane.Smith@email.com")

    def test_fullname(self):
        emp_1 = Employee("Lokesh", "Sharma", 50000)
        emp_2 = Employee("John", "Smith", 60000)
        self.assertEqual(emp_1.fullname, "Lokesh Sharma")
        self.assertEqual(emp_2.fullname, "John Smith")
        emp_1.first = "John"
        emp_2.first = "Jane"
        self.assertEqual(emp_1.fullname, "John Sharma")
        self.assertEqual(emp_2.fullname, "Jane Smith")

    def test_apply_raise(self):
        emp_1 = Employee("Lokesh", "Sharma", 50000)
        emp_2 = Employee("John", "Smith", 60000)
        emp_1.apply_raise()
        emp_2.apply_raise()
        self.assertEqual(emp_1.pay, 55000)
        self.assertEqual(emp_2.pay, 66000)


if __name__ == "__main__":
    unittest.main()
