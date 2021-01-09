from main import BaseAdvertising


class Advertiser(BaseAdvertising):
    __total_clicks = 0

    def __init__(self, id, name):
        super().__init__(id)
        self.__name = name

    @staticmethod
    def help():
        return "I have id, name, clicks and views fields"

    @staticmethod
    def describe_me():
        return "I am advertiser class :)"

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    @staticmethod
    def get_total_clicks():
        return Advertiser.__total_clicks

    @staticmethod
    def inc_total_clicks():
        Advertiser.__total_clicks += 1
