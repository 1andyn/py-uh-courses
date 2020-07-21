"""

Term (Semester) object

"""
import concurrent.futures

import requests  # importing the requests library
from lxml import html


class Term:
    def __init__(self, term_code, term_desc, school):
        self.__t_code = term_code
        self.__t_desc = term_desc
        self.__school = school
        self.__subs = list()

    def get_code(self):
        return self.__t_code

    def get_desc(self):
        return self.__t_desc

    def get_school(self):
        return self.__school.get_code()

    def set_subs(self, sub_list):
        self.__subs = sub_list

    def get_subs(self):
        return self.__subs

def ret_terms_for_campus(school):
    school_code = school.get_code()

    # terms list endpoint
    URL = "https://www.sis.hawaii.edu/uhdad/avail.classes?i="

    termlist = list()
    termdesc_list = list()

    # Retrieve campus list by hitting course availability webpage and making a GET request
    r = requests.get(url=URL + school_code)  # school_code is passed as a parameter

    if r.status_code < 200 or r.status_code > 299:
        print ("Unexpected status code, exiting: " + r.status_code)
        return

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
            termlist.append(Term(code, termdesc_list[desc_idx], school))
            desc_idx += 1

    return termlist


def ret_terms_for_list(school_list):
    # 1 thread = 1.8-2 seconds, 4 threads, .6 seconds
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        future_termlist = { executor.submit(ret_terms_for_campus, s) : s for s in school_list }
        for future in concurrent.futures.as_completed(future_termlist):
            future_termlist[future].set_terms(future.result())
