import unittest
from flask import Flask
from flask_testing import TestCase
from UserManagement.Infrestructure.Route import UserRoutes

class TestUserRoutes(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        app.register_blueprint(UserRoutes.user_blueprint, url_prefix="/api/v1/users")
        return app

    def test_register_user(self):
        with self.client:
            response = self.client.post('/api/v1/users/', json={
                "name": "Test",
                "last_name": "User",
                "cellphone": "1234567880",
                "email": "gamerfigh@gmail.com",
                "password": "password"
            })
            self.assertEqual(response.status_code, 201)
            data = response.get_json()
            self.assertEqual(data['name'], "Test")
            self.assertEqual(data['last_name'], "User")
            self.assertEqual(data['cellphone'], "1234567890")
            self.assertEqual(data['email'], "test@example.com")

    def test_activate_user(self):
        with self.client:
            response = self.client.put('/api/v1/users/test_token/active')
            self.assertEqual(response.status_code, 201)
            data = response.get_json()
            self.assertEqual(data['activation_token'], "test_token")

if __name__ == '__main__':
    unittest.main()