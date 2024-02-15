from flask import Flask
from UserManagement.Infrestructure.Route.UserRoutes import user_blueprint

app = Flask(__name__)

app.register_blueprint(user_blueprint, url_prefix="/api/v1/users")

if __name__ == "__main__":
    app.run(debug=True)

