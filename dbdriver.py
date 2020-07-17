import pymongo
import dns

class Database:
    def __init__(self):
        f = open("auth", "r")
        c_pa = f.readline().strip()
        c_sr = f.readline().strip()
        c_co = f.readline().strip()
        client = pymongo.MongoClient("mongodb+srv://" + c_sr + ":" + c_pa + "@" + c_co +
                                     "/arg_react_sch?authSource=admin&retryWrites=true&w=majority")
        self.__mgdbClient = client
        self.__db = client.arg_react_sch

    def getDatabases(self):
        self.__mgdbClient.list_database_names()

    def getCollections(self):
        self.__mgdbClient.list_collection_names()

    def getmgdbClient(self):
        return self.__mgdbClient

def insertCampuses():
    return


def insertTerms():
    return


def insertCourses():
    return
