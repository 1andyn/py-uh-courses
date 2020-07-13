"""

Campus (School) Object

"""

class Campus:
    def __init__(self, school_code, school_desc):
        self.code = school_code
        self.desc = school_desc

def retrieve_campuses():
    import xml.etree.ElementTree as ET # importing the xml parse library
    import requests # importing the requests library

    # campuses list endpoint
    URL = "https://www.sis.hawaii.edu/uhdad/avail.classes"

    campuslist = list()
    # Retrieve campus list by hitting course availability webpage and making a GET request




