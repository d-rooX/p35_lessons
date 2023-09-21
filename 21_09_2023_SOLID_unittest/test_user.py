import unittest
import user

# DRY
# Dont Repeat Yourself

class TestUser(unittest.TestCase):
    def setUp(self):
        # Before every testcase
        print('Setting up...')
        self.john = user.User('John', 'Doe', 2000)
        self.sarah = user.User('Sarah', 'Smith', 2500)

    def tearDown(self) -> None:
        print('Tear down...')

    def test_email(self):
        print('Test email...')
        self.assertEqual(self.john.email(), 'John.Doe@gmail.com')
        self.assertEqual(self.sarah.email(), 'Sarah.Smith@gmail.com')

    def test_rise(self):
        print('Test rise...')
        self.john.rise_salary(0.25)
        self.sarah.rise_salary(0.30)

        self.assertEqual(self.john.salary, 2500)
        self.assertEqual(self.sarah.salary, 3250)

    def test_salary(self):
        print('Test salary...')
        self.assertEqual(self.john.salary, 2000)
        self.assertEqual(self.sarah.salary, 2500)


if __name__ == '__main__':
    unittest.main()


