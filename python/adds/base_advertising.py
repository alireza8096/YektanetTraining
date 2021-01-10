
class BaseAdvertising:
    def __init__(self, id=-1):
        self._id = id
        self._clicks = 0
        self._views = 0

    def inc_views(self):
        self._views += 1

    def inc_clicks(self):
        self._clicks += 1

    @property
    def clicks(self):
        return self._clicks

    @property
    def views(self):
        return self._views

    @staticmethod
    def describe_me():
        return "I am BaseAdvertising class :)"


