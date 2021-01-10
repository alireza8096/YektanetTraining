from adds.base_advertising import BaseAdvertising


class Advertiser(BaseAdvertising):
    _total_clicks = 0

    def __init__(self, id, name):
        super().__init__(id)
        self._name = name

    @staticmethod
    def help():
        return "I have id, name, clicks and views fields"

    @staticmethod
    def describe_me():
        return "I am advertiser class :)"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @name.deleter
    def name(self):
        del self._name

    @staticmethod
    def get_total_clicks():
        return Advertiser._total_clicks

    @staticmethod
    def inc_total_clicks():
        Advertiser._total_clicks += 1
