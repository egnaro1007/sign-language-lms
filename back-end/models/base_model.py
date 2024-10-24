from abc import abstractmethod


class BaseModel:
    def get_from_database(self, id):
        pass

    def save_to_database(self, id):
        pass   