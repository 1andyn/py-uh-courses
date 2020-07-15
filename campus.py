"""

Campus (School) Object

"""
from lxml import html
import requests  # importing the requests library

class Campus:
    def __init__(self, school_code, school_desc):
        self.__code = school_code
        self.__desc = school_desc

    def getCode(self):
        return self.__code

    def getDesc(self):
        return self.__desc

def retrieve_campuses():
    # campuses list endpoint
    URL = "https://www.sis.hawaii.edu/uhdad/avail.classes"

    campuslist = list()

    # Retrieve campus list by hitting course availability webpage and making a GET request
    r = requests.get(url = URL) #no parameters
    tree = html.fromstring(r.content)

    for elt in tree.xpath('//li'):
        # print(elt.attrib['class'], elt.text_content())
        campuslist.append(Campus(elt.attrib['class'], elt.text_content()))

    return campuslist



