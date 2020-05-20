import requests


class HandleRequest():
    default_form_url = 'https://google.com'

    def check_url(self, form_data):
        if form_data is None:
            form_data = self.default_form_url
        else:
            return form_data
    
    def process_url(self, form_url):
        pass