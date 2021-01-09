
class BaseAdvertising:
    def __init__(self, id=-1):
        self.__id = id
        self.__clicks = 0
        self.__views = 0

    def inc_views(self):
        self.__views += 1

    def inc_clicks(self):
        self.__clicks += 1

    def get_clicks(self):
        return self.__clicks

    def get_views(self):
        return self.__views

    @staticmethod
    def describe_me():
        return "I am BaseAdvertising class :)"


