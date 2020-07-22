"""

Subject (Course Subjects) object

"""
import concurrent.futures
from lxml import html
import requests  # importing the requests library


class Course:

    # Constructor
    def __init__(self):
        self.__sub = ""
        self.__crn = 0
        self.__sec = ""
        self.__course = ""
        self.__c_desc = ""
        self.__arrdays = []
        self.__arrdays2 = []
        self.__arrMiscData = []
        self.__creds = ""  # initialize to zero
        self.__instr = ""
        self.__instr_full = ""
        self.__enroll = 0  # initialize to zero
        self.__seat = 0  # initialize to zero
        self.__wait = 0
        self.__waita = 0
        self.__other = ""
        self.__room = ""
        self.__room_long = ""
        self.__room2 = ""
        self.__room2_long = ""
        self.__start = 0
        self.__start2 = 0
        self.__end = 0
        self.__end2 = 0
        self.__startdate = ""
        self.__startdate2 = ""
        self.__enddate = ""
        self.__enddate2 = ""
        self.__note = ""

    # Print Course Object to ensure results are mapped correctly:
    def print_course(self):
        print("Col 0: Misc: - ", end=" ")
        print(*self.__arrMiscData)
        print("Col 1: CRN: - " + str(self.__crn))
        print("Col 2: Course: - " + self.__course)
        print("Col 3: Section: - " + str(self.__sec))
        print("Col 4: Title: - " + self.__c_desc)
        print("Col 5: Credit: - " + str(self.__creds))
        print("Col 6: Instructor: - " + self.__instr + " - Full: " + self.__instr_full)
        print("Col 7: Enrolled: - " + str(self.__enroll))
        print("Col 8: Seats Avail: - " + str(self.__seat))
        print("Col 9: Waitlisted: - " + str(self.__wait))
        print("Col 10: Waitlisted Avail: - " + str(self.__waita))
        print("Col 11: Days: - ", end=" ")
        print(*self.__arrdays, end=" ")
        print("- Days2: ", end=" ")
        print(*self.__arrdays2)
        print("Col 12: Start: - " + str(self.__start) + " - End: " + str(self.__end))
        print("Col 12.5: Start: - " + str(self.__start2) + " - End: " + str(self.__end2))
        print("Col 13: Room: - " + self.__room + " - Full Room: " + self.__room_long)
        print("Col 13.5: Room2: - " + self.__room2 + " - Full Room: " + self.__room2_long)
        print("Col 14: Start Date: - " + self.__startdate + " - End Date: " + self.__enddate)
        print("Col 14.5: Start Date2: - " + self.__startdate2 + " - End Date: " + self.__enddate2)

    # Returns Course CRN
    def get_crn(self):
        return self.__crn

    def set_crn(self, crn):
        self.__crn = crn

    def get_course(self):
        return self.__course

    def set_course(self, course):
        self.__course = course

    def get_section(self):
        return self.__sec

    def set_section(self, sec):
        self.__sec = sec

    def get_course_desc(self):
        return self.__c_desc

    def set_course_desc(self, desc):
        self.__c_desc = desc

    def get_sub(self):
        return self.__sub

    def set_sub(self, sub):
        self.__sub = sub

    # Get Misc course designation array
    def get_misc(self):
        return self.__arrMiscData

    # Set Misc course designation array
    def set_misc(self, misc_arr):
        self.__arrMiscData = misc_arr

    # Get Days Array
    def get_days(self):
        return self.__arrdays

    # Set Days Array
    def set_days(self, days):
        self.__arrdays = days

    # Get Days Array 2
    def get_days2(self):
        return self.__arrdays2

    # Set Days Array 2
    def set_days2(self, days):
        self.__arrdays2 = days

    # Get Instructor
    def set_instruct(self, ins):
        self.__instr = ins

    # Set Instructor
    def get_instruct(self):
        return self.__instr

    # Get Instructor Full
    def set_instructlong(self, ins_full):
        self.__instr_full = ins_full

    # Set Instructor Full
    def get_instructlong(self):
        return self.__instr_full

    # Set Students Enrolled
    def set_enroll(self, count):
        self._enroll = count

    # Get Students Enrolled
    def get_enroll(self):
        return self.__enroll

    # Get Seats
    def get_seats(self):
        return self.__seat

    # Set Seats
    def set_seats(self, seat):
        self.__seat = seat

    # Get Waitlist
    def get_wait(self):
        return self.__wait

    # Set Waitlist
    def set_wait(self, wait):
        self.__wait = wait

    # Get Wait Avail
    def get_waita(self):
        return self.__waita

    # Set Wait Avail
    def set_waita(self, waita):
        self.__waita = waita

    # get other notes
    def get_other(self):
        return self.__other

    # set other notes
    def set_other(self, other):
        self.__other = other

    # get room
    def get_other(self):
        return self.__room

    # set room
    def set_room(self, room):
        self.__room = room

    # get room 2
    def get_room2(self):
        return self.__room2

    # set room2
    def set_room2(self, room):
        self.__room2 = room

    # get room long
    def get_room_long(self):
        return self.__room_long

    # set room long
    def set_room_long(self, room):
        self.__room_long = room

    # get room 2 long
    def get_room2_long(self):
        return self.__room2_long

    # set room2 long
    def set_room2_long(self, room):
        self.__room2_long = room

    # get time start
    def get_start(self):
        return self.__start

    # set time start
    def set_start(self, start):
        self.__start = start

    # get time end
    def get_end(self):
        return self.__end

    # set time end
    def set_end(self, end):
        self.__end = end

    # get time start
    def get_startdate(self):
        return self.__startdate

    # set time start
    def set_startdate(self, start):
        self.__startdate = start

    # get time end
    def get_enddate(self):
        return self.__enddate

    # set time end
    def set_enddate(self, end):
        self.__enddate = end

    # get time start 2
    def get_start2(self):
        return self.__start2

    # set time start 2
    def set_start2(self, start):
        self.__start2 = start

    # get time end 2
    def get_end2(self):
        return self.__end2

    # set time end 2
    def set_end2(self, end):
        self.__end2 = end

    # get time start 2
    def get_startdate2(self):
        return self.__startdate2

    # set time start 2
    def set_startdate2(self, start):
        self.__startdate2 = start

    # get time end 2
    def get_enddate2(self):
        return self.__enddate2

    # set time end 2
    def set_enddate2(self, end):
        self.__enddate2 = end

    # Get Course Credit Value
    def get_cred(self):
        return self.__creds

    # Set Course Credit Value
    def set_cred(self, cred):
        self.__creds = cred

    # Returns Course Title
    def get_course(self):
        return self.__course

    # Returns Course Section
    def get_section(self):
        return self.__sec

    # Returns Course Description
    def get_desc(self):
        return self.__c_desc

    # Returns School Code
    def get_school(self):
        return self.__sub.get_school()

    # Returns Term Code
    def get_term(self):
        return self.__sub.get_term()

    # Returns Subject Code
    def get_sub(self):
        return self._sub.get_code()

    # Returns Note
    def get_note(self):
        return self.__note

    # Sets Note
    def set_note(self, note):
        self.__note = note


def ret_courses_for_sub(subject):
    # subjects list endpoint

    if subject.get_term()[4:6:] == "10":
        year = str(int(subject.get_term()[0:4:]) - 1)
    else:
        year = subject.get_term()[0:4:]

    URL = "https://www.sis.hawaii.edu/uhdad/avail.classes?i=" + subject.get_school() \
          + "&t=" + subject.get_term() + "&s=" + subject.get_code()

    course = list()
    course_list = list()

    # Retrieve subject list by hitting course availability webpage and making a GET request

    r = requests.get(url=URL)  # school_code, term_code is passed as a parameter

    if r.status_code < 200 or r.status_code > 299:
        print("Unexpected status code, exiting: " + r.status_code)
        return

    data = r.text.replace("<br>", ", ").replace("<br />", ", ")
    # usually r.content but due to inconsistent formating, we have to strip br tags

    tree = html.fromstring(data)

    for elt in tree.xpath('//tr'):
        res = elt.find_class('default')  # finds all TD elements with class "default"
        count = 0

        # create course object for row
        crs = Course()

        # Means the row isn't a course row but is either a :
        # Note above the row
        # Note below the row,
        # A lab/secondary class
        rogue_row = False

        """
        if len(res) > 0:
            print("Col count: " + str(len(res)))
        """

        for s in res:
            # print("Col: " + str(count) + " - " + s.text_content())
            # note = elt.find_class('section-comment-above')

            # Column 0 is
            if count == 0:
                # Attempt to Parse
                if not s.text_content() == " ":
                    misc = s.text_content().split(",")
                    crs.set_misc(misc)

            # Rogue row is detected if the CRN is not populated for the row
            if count == 1:
                if s.text_content() == " ":
                    rogue_row = True
                else:
                    crs.set_crn(int(s.text_content()))

            # Don't set empty info
            if not rogue_row:
                # Course
                if count == 2:
                    crs.set_course(s.text_content())

                # Section
                if count == 3:
                    crs.set_section(s.text_content())

                # Course Description
                if count == 4:
                    crs.set_course_desc(s.text_content())

                # Credit
                if count == 5:
                    crs.set_cred(s.text_content())

                # Column Six is instructor
                if count == 6:
                    crs.set_instruct(s.text_content())

                    # Set full instructor name
                    ins = elt.find_class('abbr')
                    if len(ins) != 0:
                        crs.set_instructlong(ins[0].attrib['title'])

                # Column 7 is enrollment
                if count == 7:
                    crs.set_enroll(int(s.text_content()))

                # Column 8 is seats available
                if count == 8:
                    crs.set_seats(int(s.text_content()))

                # Column 9 is Waitlisted Count
                if count == 9 and len(res) == 15:
                    if s.text_content() != " ":
                        crs.set_wait(int(s.text_content()))

                # Column 10 is waitlisted available
                if count == 10 and len(res) == 15:
                    if s.text_content() != " ":
                        crs.set_waita(int(s.text_content()))

            # 11 or 10 is room
            if count == 11 and len(res) == 15 \
                    or count == 10 and len(res) == 14 \
                    or count == 9 and len(res) == 13:
                # Not empty, attempt to parse
                if s.text_content() != " ":
                    # Rogue Row, set secondary of previous course
                    if s.text_content() == "TBA":
                        days = ["TBA"]
                    # If not TBA, split by character
                    else:
                        days = list(s.text_content())
                    if rogue_row:
                        prev.set_days2(days)
                    else:
                        crs.set_days(days)

            # 12 or 11 is room
            if count == 12 and len(res) == 15 \
                    or count == 11 and len(res) == 14 \
                    or count == 10 and len(res) == 13:
                if not s.text_content() == "TBA":
                    times = s.text_content().split('-')

                    # first value is start
                    # second value is end
                    if times[1][-1] == "p":
                        # second time is PM, transform
                        # increment by 1200 if value is less than 1200 but designated PM time
                        if int(times[1][0:4:]) < 1200:
                            new_end = int(times[1][0:4:]) + 1200
                        else:
                            new_end = int(times[1][0:4:])

                        # if start time is less than end time, we know it is AM (since there aren't any 24 hour courses)
                        if int(times[0]) < int(times[1][0:4:]) < 1200:
                            new_start = int(times[0]) + 1200
                        else:
                            new_start = int(times[0])

                    else:
                        new_start = int(times[0])
                        new_end = int(times[1][0:4:])

                    # Set time based on rogue row indication
                    if rogue_row:
                        prev.set_start2(new_start)
                        prev.set_end2(new_end)
                    else:
                        crs.set_start(new_start)
                        crs.set_end(new_end)

            # 13 or 12 is room
            if count == 13 and len(res) == 15 \
                    or count == 12 and len(res) == 14 \
                    or count == 11 and len(res) == 13:

                if rogue_row:
                    prev.set_room2(s.text_content())
                    # Set full room name
                    rm = elt.find_class('abbr')
                    if len(rm) != 0:
                        prev.set_room2_long(rm[0].attrib['title'])

                else:
                    crs.set_room(s.text_content())
                    # Set full room name
                    rm = elt.find_class('abbr')
                    if len(rm) == 2:
                        crs.set_room_long(rm[1].attrib['title'])

            # 14 or 13 is start / end dates
            if count == 14 and len(res) == 15 \
                    or count == 13 and len(res) == 14 \
                    or count == 12 and len(res) == 13:
                dates = s.text_content().split('-')

                if rogue_row:
                    prev.set_startdate2(dates[0] + "/" + year)
                    # for some reason some courses don't have an end date...
                    if len(dates) == 2:
                        prev.set_enddate2(dates[1] + "/" + year)
                else:
                    crs.set_startdate(dates[0] + "/" + year)
                    if len(dates) == 2:
                        crs.set_enddate(dates[1] + "/" + year)

            """
            # Edge Case: Manoa classes are putting notes at the beginning on a separate TR
            for a in note:  # finds all note elements with "section comment", appears to be used by UH Manoa
                print(a.text_content().strip())
            """
            count += 1

        """
        # Edge Case: Honolulu Community College puts notes at end with TD COLSPAN 13 on a separate TR
        note2 = elt.findall('.//td[@colspan="13"]')
        for b in note2:
            # Hard coded replacement logic since the formatting is just a <br> tag..
            print(b.text_content().strip())
            note_end = b.text_content().strip()
        """

        # Append course to course list
        if not rogue_row and count != 0:
            course_list.append(crs)
            prev = crs  # Tracks previous course so we can manipulate it in the scenario that note2 exists

    """
    for c in course_list:
        c.print_course()
        print("---")
    """

    # print("Courses built: " + str(len(course_list)))

    return course_list


def ret_courses_for_schools(school_list):
    """
    1 thread = 30 sec
    4 threads = 9 sec
    8 threads = 6 sec
    16 threads = 3.5 sec
    32 threads = 2.8 sec [magic number?]
    64 threads = 3.8 sec
    """
    with concurrent.futures.ThreadPoolExecutor(max_workers=32) as executor:
        future_courselist = {executor.submit(ret_courses_for_sub, u): u
                           for s in school_list for t in s.get_terms()
                           for u in t.get_subs()}
        for future in concurrent.futures.as_completed(future_courselist):
            future_courselist[future].set_courses(future.result())
