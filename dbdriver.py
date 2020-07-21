import pymongo
import datetime
import auth
import dns


class Database:
    def __init__(self):
        client = pymongo.MongoClient("mongodb+srv://" + auth.c_sr + ":" + auth.c_pa + "@" + auth.c_co +
                                     "/arg_react_sch?authSource=admin&retryWrites=true&w=majority")
        self.__mgdbClient = client
        self.__db = client.arg_react_sch

    # returns database object for arg react sch
    def get_database(self):
        return self.__db

    # prints collections in database
    def print_collections(self):
        col_list = self.__db.list_collection_names()
        for col in col_list:
            print(col)

    # inserts campus list to campus collection
    def insert_campuses(self, campus_list):

        collection = self.__db["campuses"]
        doc = []
        for campus in campus_list:
            doc.append({"strSchoolCode": campus.get_code(),
                        "strSchoolDesc": campus.get_desc(),
                        "dtmCreated": datetime.datetime.utcnow()})

        res = collection.insert_many(doc)

    def insert_terms(self, campus_list):

        collection = self.__db["semester"]
        doc = []

        for campus in campus_list:
            for term in campus.get_terms():
                doc.append({"strSchoolCode": campus.get_code(),
                            "strTermCode": term.get_code(),
                            "strTermDesc": term.get_desc(),
                            "dtmCreated": datetime.datetime.utcnow()})

        res = collection.insert_many(doc)

    def insert_subjects(self, campus_list):
        collection = self.__db["subjects"]
        doc = []

        for campus in campus_list:
            for term in campus.get_terms():
                for sub in term.get_subs():
                    doc.append({"strSchoolCode": campus.get_code(),
                                "strTermCode": term.get_code(),
                                "strTermDesc": term.get_desc(),
                                "strSubCode" : sub.get_code(),
                                "strSubDesc" : sub.get_desc(),
                                "dtmCreated": datetime.datetime.utcnow()})

        res = collection.insert_many(doc)

    def insert_courses(self):
        return

    def rebuild_campus(self):
        collection = self.__db["campuses"]
        collection.drop()
        rebuilt_col = self.__db["campuses"]
        print("Campus table rebuilt")

    def rebuild_term(self):
        collection = self.__db["semester"]
        collection.drop()
        rebuilt_col = self.__db["semester"]
        print("Semester table rebuilt")