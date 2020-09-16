from datetime import datetime, timedelta
import unittest
from soleed import app, db
from soleed.models import User, School

class UserModelCase(unittest.TestCase):
  def setUp(self):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
    db.create_all()

  def tearDown(self):
    db.session.remove()
    db.drop_all()

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
