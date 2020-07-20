import campus
import term
import time
import dbdriver
import dns


#test campus retrieval

# Time how long it takes to Retrieve Campuses
start_time = time.time()
campus_list = campus.retrieve_campuses()
print("[Campus Logic] --- %s seconds ---" % (time.time() - start_time))

# test terms retrieval

start_time = time.time()
#term.ret_terms_for_campus("HAW")
term.ret_terms_for_list(campus_list)
print("[Term Logic]--- %s seconds ---" % (time.time() - start_time))

# test mongo driver
start_time = time.time()
connection = dbdriver.Database()
print("[Connect Logic] --- %s seconds ---" % (time.time() - start_time))

# test insert driver for campus
start_time = time.time()
connection.insert_campuses(campus_list)
print("[Insert Campus Logic] --- %s seconds ---" % (time.time() - start_time))

# test insert driver for terms
start_time = time.time()
connection.insert_terms(campus_list)
print("[Insert Term Logic] --- %s seconds ---" % (time.time() - start_time))