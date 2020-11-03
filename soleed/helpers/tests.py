from datetime import datetime, timedelta
import unittest
from soleed import db
from config import Config
from soleed.soleed import create_app
from soleed.models import User, School

class TestConfig(Config):
  TESTING = True
  SQLALCHEMY_DATABASE_URI = 'sqlite://' 

class UserModelCase(unittest.TestCase):
  def setUp(self):
    self.app = create_app(TestConfig)
    self.app_context = self.app.app_context
    self.app_context.push()
    db.create_all()

  def tearDown(self):
    db.session.remove()
    db.drop_all()
    self.app_context.pop()

  def test_password_hashing(self):
    u = User(username='Maria')
    u.set_password('cat')
    self.assertFalse(u.check_password('dog'))
    self.assertTrue(u.check_password('cat'))

  def test_avatar(self):
    u = User(username='John', email='john@example.com')
    self.assertEqual(u.avatar(80), ('https://www.gravatar.com/avatar/'
                                         'd4c74594d841139328695756648b6bd6'
                                         '?d=retro&s=80'))


if __name__ == '__main__':
  unittest.main(verbosity=2)
