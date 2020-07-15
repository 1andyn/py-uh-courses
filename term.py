"""

Term (Semester) object

"""
from lxml import html
import requests  # importing the requests library


class Term:
    def __init__(self, term_code, term_desc):
        self.__t_code = term_code
        self.__t_desc = term_desc
        self.__subs = list()

    def getCode(self):
        return self.__t_code

    def getDesc(self):
        return self.__t_desc

    def setTerms(self, sub_list):
        self.__subs = sub_list


def ret_terms_for_campus(school_code):
    # terms list endpoint
    URL = "https://www.sis.hawaii.edu/uhdad/avail.classes?i="

    termlist = list()
    termdesc_list = list()

    # Retrieve campus list by hitting course availability webpage and making a GET request
    r = requests.get(url=URL + school_code)  # school_code is passed as a parameter

    if r.status_code < 200 or r.status_code > 299:
        raise ("Unexpected status code: ", r.status_code)

    tree = html.fromstring(r.content)

    # get term descs
    for elt in tree.xpath('//li'):
        termdesc_list.append(elt.text_content().strip().replace("\n", ""))

    # get term codes
    desc_idx = 0
    for elt in tree.xpath('//a'):
        code_string = elt.attrib['href'].strip()
        idx = code_string.find("&t")  # extract code from hyperlink
        if idx != - 1:
            code = code_string[idx + 3::]  # starts after &t=
            #print(code + " " + termdesc_list[desc_idx])
            termlist.append(Term(code, termdesc_list[desc_idx]))
            desc_idx += 1

    return termlist


def ret_terms_for_list(school_list):
    for s in school_list:
        termlist = ret_terms_for_campus(s.getCode())  # create term list for school code
        s.setTerms(termlist)
