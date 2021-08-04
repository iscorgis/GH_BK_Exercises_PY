import unittest
import Calcular as c


class TestCalculadora(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass() -> OK')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass() -> OK')

    def setUp(self):
        print('setUp() -> OK')

    def test_suma(self):
        """
        Test that it can sum a list of integers
        """
        result = c.sumar(8, 78)
        self.assertEqual(result, 86)
        print('test_suma() -> OK')

    def teardown(self):
        print('tearDown() -> OK')


if __name__ == '__main__':
    unittest.main()
