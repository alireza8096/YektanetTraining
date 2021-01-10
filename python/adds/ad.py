from adds.base_advertising import BaseAdvertising
from adds.advertiser import Advertiser


class Ad(BaseAdvertising):
    def __init__(self, id, title, image_url, link, advertiser):
        super().__init__(id)
        self._title = title
        self._image_url = image_url
        self._link = link
        self._advertiser = advertiser

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @title.deleter
    def title(self):
        del self._title

    @property
    def image_url(self):
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        self._image_url = image_url

    @image_url.deleter
    def image_url(self):
        del self._image_url

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, link):
        self._link = link

    @link.deleter
    def link(self):
        del self._link

    @property
    def advertiser(self):
        return self._advertiser

    @advertiser.setter
    def advertiser(self, advertiser):
        self._advertiser = advertiser

    @advertiser.deleter
    def advertiser(self):
        del self._advertiser

    def inc_clicks(self):
        super().inc_clicks()
        self._advertiser.inc_clicks()
        Advertiser.inc_total_clicks()

    def inc_views(self):
        super().inc_views()
        self._advertiser.inc_views()

    @staticmethod
    def describe_me():
        return "I am Ad class :)"
