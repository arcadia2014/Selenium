import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # Verifica que s.split falle si el separador no es una cadena
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main(verbosity=2)