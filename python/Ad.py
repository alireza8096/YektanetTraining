from main import BaseAdvertising


class Add(BaseAdvertising):
    def __init__(self, id, title, image_url, link, advertiser):
        super().__init__(id)
        self.__title = title
        self.__image_url = image_url
        self.__link = link
        self.__advertiser = advertiser

    def inc_clicks(self):
        super().inc_clicks()
        self.__advertiser.inc_clicks()

    def inc_views(self):
        super().inc_views()
        self.__advertiser.inc_views()

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def set_image_url(self, image_url):
        self.__image_url = image_url

    def get_image_url(self):
        return self.__image_url

    def set_link(self, link):
        self.__link = link

    def get_link(self):
        return self.__link

    def get_advertiser(self):
        return self.__advertiser

    def set_advertiser(self, advertiser):
        self.__advertiser = advertiser

    @staticmethod
    def describe_me():
        return "I am Ad class :)"

