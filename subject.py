"""

Subject (Course Subjects) object

"""
import concurrent.futures

from lxml import html
import requests  # importing the requests library


class Subject:
    def __init__(self, sub_code, sub_desc, term):
        self.__s_code = sub_code
        self.__s_desc = sub_desc
        self.__term = term
        self.__courses = list()

    def get_code(self):
        return self.__s_code

    def get_desc(self):
        return self.__s_desc

    def set_courses(self, course_list):
        self.__courses = course_list

    def get_courses(self):
        return self.__courses

    def get_school(self):
        return self.__term.get_school()


def ret_subs_for_term(term):
    # subjects list endpoint
    URL = "https://www.sis.hawaii.edu/uhdad/avail.classes?i=" + term.get_school() + "&t=" + term.get_code()

    sublist = list()
    subdesc_list = list()

    # Retrieve subject list by hitting course availability webpage and making a GET request

    r = requests.get(url=URL)  # school_code, term_code is passed as a parameter

    if r.status_code < 200 or r.status_code > 299:
        print ("Unexpected status code, exiting: " + r.status_code)
        return

    tree = html.fromstring(r.content)

    # get term descs
    for elt in tree.xpath('//li'):

        subdesc_list.append(elt.text_content().strip().replace("\n", ""))

    # get term codes

    prev = "" #empty string for containing previous code to handle one off dupes

    desc_idx = 0
    for elt in tree.xpath('//a'):
        code_string = elt.attrib['href'].strip()
        idx = code_string.find("&s")  # extract code from hyperlink
        if idx != - 1:
            code = code_string[idx + 3::]  # starts after &s=
            if code != prev:
                #print(code + " - " + subdesc_list[desc_idx])
                sublist.append(Subject(code, subdesc_list[desc_idx], term))
                desc_idx += 1
                prev = code

    return sublist


def ret_subs_for_list(school_list):
    """
    1 thread = 30 sec
    4 threads = 9 sec
    8 threads = 6 sec
    16 threads = 3.5 sec
    32 threads = 2.8 sec [magic number?]
    64 threads = 3.8 sec
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=32) as executor:
        future_termlist = { executor.submit(ret_subs_for_term, t) : t
                            for s in school_list for t in s.get_terms() }
        for future in concurrent.futures.as_completed(future_termlist):
            future_termlist[future].set_subs(future.result())
