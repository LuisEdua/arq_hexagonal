from Database.MongoDB import MongoDB


class UserMongoModel:
    def __init__(self):
        self.db = MongoDB("uri", "nombre").get_db()
        self.collection = self.db['users']

    def insert_user(self, user):
        return self.collection.insert_one(user)

    def find_user(self, query):
        return self.collection.find_one(query)

    def update_user(self, query, new_values):
        return self.collection.update_one(query, new_values)