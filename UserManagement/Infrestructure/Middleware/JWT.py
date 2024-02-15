import jwt
import datetime

SECRET_KEY = 'your-secret-key'


def create_token(user_id):
    exp = datetime.datetime.now() + datetime.timedelta(hours=24)

    token = jwt.encode({'user_id': user_id, 'exp': exp}, SECRET_KEY, algorithm='HS256')

    return token

def verify_token(token):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])

        user_id = data['user_id']

        return user_id
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None