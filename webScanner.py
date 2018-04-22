import requests
from bs4 import BeautifulSoup
from tld import get_tld

class Image:

    # Constructing the object
    def __init__(self, width, height, title, link):
        self.width = width
        self.height = height
        self.title = title
        self.link = link

    # Geting the width parameter
    def getWidth(self):
        return self.width

    # Geting the height parameter
    def getHeight(self):
        return self.height

    # Geting the title parameter
    def getTitle(self):
        return self.title

    # Geting the link parameter
    def getLink(self):
        return self.link

class Scanner:

    # Constructing the object
    def __init__(self, url):
        try:
            # Return base url e.g www.pexels.com
            self.baseurl = url

            # Return 200 Requests only for check
            self.url = requests.get(self.baseurl)
            # Returns HTML in bs
            self.bs = BeautifulSoup(self.url.text, 'html.parser')

            # Check is OK...
            if self.url.status_code is 200:
                print("Status: 200")
            else:
                print("Status: Not OK")

        except EnvironmentError:
            print("Exception on set Url")
            raise EnvironmentError

    # To see the baseurl
    def getBaseUrl(self):
        return self.baseurl

    # Set search on baseUrl over pages, reconstructing the object
    def setSearchWordUrl(self, search):
        tmp = "{}/search/{}".format(self.getBaseUrl(), search)
        self.baseurl = "https://www." + get_tld(tmp)+"/search/" + search
        return "Set: " + search

    # Get the <title> element in HTML code
    def getPageTitle(self):
        tmp_str = str(self.bs.title.text)
        tmp_str = tmp_str.split(" · ")
        return tmp_str[0]

    # Get the data from specific page
    def getSpecificData(self, type1="article", type2="img"):

        data = []
        for i in self.bs.find_all(type1):

            t = i.select(type2)[0].get('alt')
            l = i.select(type2)[0].get('data-big-src')
            w = 300
            h = 300
            img = Image(w, h, t, l)
            data.append(img.__dict__)

        return data

"""
if __name__ == '__main__':


    URL = "https://www.pexels.com"

    s1 = Scanner(URL)
    print(s1.getBaseUrl())
    #s1.setSearchWordUrl('adventure')
    #print(s1.getBaseUrl())
    print(s1.getSpecificData())

    s2 = Scanner(URL+"/search/sunset/")
    s2.setSearchWordUrl('love')
    print(s2.getBaseUrl())
    print(s2.getSpecificData())
"""