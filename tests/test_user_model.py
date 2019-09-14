import unittest
from app.models import User  #the uppest layer don`t need to write ..app.models,you can directly use app

class UserModelTestCase(unittest.TestCase):
	def test_password_setting(self): #must use test as the function`s very beginning,or the function will not run.
		u=User(password='cat')
		self.assertTrue(u.password_hash is not None)

	def test_no_password_getter(self):
		u=User(password='cat')
		with self.assertRaises(AttributeError):
			u.password

	def test_password_verification(self):
		u=User(password='cat')
		self.assertTrue(u.verify_password('cat'))
		self.assertFalse(u.verify_password('dog'))

	def test_password_salts_are_random(self):
		u1=User(password='cat')
		u2=User(password='cat')
		self.assertTrue(u1.verify_password!=u2.verify_password)