import unittest
from validate_password import password_strength
from validate_password import validate_password

class TestPassword(unittest.TestCase):
    def test_length(self):
        password="P@$w0rd"
        self.assertEqual(validate_password(password),False)
    
    def test_validation(self):
        self.assertEqual(validate_password("P@$$w0rd00*!"),True)

    def test_correct_data_type(self):
        password=12345
        with self.assertRaises(TypeError):
            validate_password(password)
    
    def test_empty_input(self):
        with self.assertRaises(ValueError):
            validate_password("")

class TestStreangth(unittest.TestCase):
    def test_strong(self):
        self.assertEqual(password_strength("P@$$w0rd00*!"),"Strong")

    def test_moderate(self):
        self.assertEqual(password_strength("Password"),"Moderate")
    
    def test_weak(self):
        self.assertEqual(password_strength("hello"),"Weak")
    
    def test_correct_type(self):
        with self.assertRaises(TypeError):
            password_strength(7)
    def test_empty_parameter(self):
        with self.assertRaises(ValueError):
            password_strength("")





if __name__=="__main__":
    unittest.main
