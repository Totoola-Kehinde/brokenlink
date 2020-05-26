import requests, urllib.request
from bs4 import BeautifulSoup


class HandleRequest():
    """Class To Handle Request passed from user form"""
    default_form_url = 'https://google.com'

    def check_url(self, form_data):
        if form_data is None:
            form_data = self.default_form_url
            print(form_data)
        else:
            return form_data
    
    def process_url(self, form_url):
        source = requests.get(form_url).text
        # Using BeautifulSoup
        soup = BeautifulSoup(source, 'lxml')
        print(soup)