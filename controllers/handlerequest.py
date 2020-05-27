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
            print(form_data)
            return form_data
    
    def process_url(self, form_url):
        # Objects To Return To The Views
        title_tag = None
        link = form_url
        message = None
        num_of_links_found = None
        broken_links = []
        source = requests.get(form_url).text
        print(source)
        # Using BeautifulSoup
        soup = BeautifulSoup(source, 'html.parser')
        title_tag = soup.title
        body_tags = soup.body
        anchor_tags = body_tags.find_all('a')
        num_of_links_found = len(anchor_tags)

        #############################################
        #### Filter The Broken Links ################
        #############################################


        if anchor_tags is not None:
            # Links Ok Count
            count = 0
            not_found_count = 0
            for link in anchor_tags:
                link_details = {link.string:link['href']}
                confirm = self.check_if_link_is_broken(link['href'])
                if confirm == True:
                    count += 1
                elif confirm == False:
                    not_found_count += 1
                    broken_links.append(link_details)
            print(" List Of Broken Links :" + broken_links)
            print("Total Number Of Links Found:" + num_of_links_found)
            print("Total Number Of Broken Links:" + not_found_count)
            print("Total Number Of Links OK" + count)
        else:
            message = "Yah!! No Broken Link Found"
            return message
        print(soup)

    def check_if_link_is_broken(self, link):
        return_bool = None
        res = requests.get(link)
        res_code = res.status_code
        if res_code == 200:
            return_bool = True
        elif res_code == 404:
            return_bool = False
        return return_bool


url = HandleRequest()
url.default_form_url = 'http://127.0.0.1:5000'
expected_url = url.check_url(url.default_form_url)
url.process_url(expected_url)