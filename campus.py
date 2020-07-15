"""

Campus (School) Object

"""
from lxml import html
import requests  # importing the requests library

class Campus:
    def __init__(self, school_code, school_desc):
        self.__c_code = school_code
        self.__c_desc = school_desc
        self.__terms = list()

    def getCode(self):
        return self.__c_code

    def getDesc(self):
        return self.__c_desc

    def setTerms(self, term_list):
        self.__terms = term_list

def retrieve_campuses():
    # campuses list endpoint
    URL = "https://www.sis.hawaii.edu/uhdad/avail.classes"

    campuslist = list()

    # Retrieve campus list by hitting course availability webpage and making a GET request
    r = requests.get(url = URL) #no parameters

    if r.status_code < 200 or r.status_code > 299:
        raise("Unexpected status code: ", r.status_code)

    tree = html.fromstring(r.content)

    for elt in tree.xpath('//li'):
        # print(elt.attrib['class'], elt.text_content())
        campuslist.append(Campus(elt.attrib['class'].strip(), elt.text_content().strip()))

    return campuslist



