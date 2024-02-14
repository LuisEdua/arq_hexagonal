from flask import Flask
from UserManagement.Infrestructure.Route.UserRoutes import user_blueprint
from Database.SQL import crear

app = Flask(__name__)

app.register_blueprint(user_blueprint, url_prefix="/api/v1/users")

crear()

if __name__ == "__main__":
    app.run(debug=True)

