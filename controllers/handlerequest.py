import requests, urllib.request
from bs4 import BeautifulSoup


class HandleRequest():
    """Class To Handle Request passed from user form"""
    default_form_url = 'https://google.com'

    # Objects To Return To The Views
    title_tag = None
    message = None
    num_of_links_found = None
    not_found_count = None
    count = None
    broken_links = []


    def check_url(self, form_data):
        if form_data is None:
            form_data = self.default_form_url
            print(form_data)
        else:
            print(form_data)
            return form_data
    
    def process_url(self, form_url):
        link = form_url
        source = requests.get(link).text
        print(source)
        # Using BeautifulSoup
        soup = BeautifulSoup(source, 'html.parser')
        self.title_tag = soup.title.string
        body_tags = soup.body
        anchor_tags = body_tags.find_all('a')
        self.num_of_links_found = len(anchor_tags)

        #############################################
        #### Filter The Broken Links ################
        #############################################


        if anchor_tags is not None:
            # Links Ok Count
            self.count = 0
            self.not_found_count = 0
            for link in anchor_tags:
                link_details = {link.string:link['href']}
                confirm = self.check_if_link_is_broken(link['href'])
                if confirm == True:
                    self.count += 1
                elif confirm == False:
                    self.not_found_count += 1
                    self.broken_links.append(link_details)
            print(" List Of Broken Links :" , self.broken_links)
            print("Total Number Of Links Found: {}".format(self.num_of_links_found))
            print("Total Number Of Broken Links: {}".format(self.not_found_count))
            print("Total Number Of Links OK : {}".format(self.count))
        else:
            message = "Yah!! No Broken Link Found"
            return message

    def check_if_link_is_broken(self, link):
        return_bool = None
        res = requests.get(link)
        res_code = res.status_code
        if res_code == 200:
            return_bool = True
        elif res_code == 404:
            return_bool = False
        return return_bool
