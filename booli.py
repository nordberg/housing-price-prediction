import requests
import dotenv

class Booli:
    def __init__(self):
        self.url = 'https://api.booli.se/sold'

    def __get_sold__(self, area):
        r = requests.get(self.url + '?q=södermalm&')
        print(r.content)
        pass

    def train(self, area):
        sold_list = self.__get_sold__(area)
        pass

    def predict(self, house):
        pass
