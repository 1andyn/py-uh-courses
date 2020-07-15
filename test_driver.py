import campus
import term
import time

# Time how long it takes to Retrieve Campuses
#start_time = time.time()
#campus.retrieve_campuses()
#("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
#term.ret_terms_for_campus("HAW")
term.ret_terms_for_list(campus.retrieve_campuses())
print("--- %s seconds ---" % (time.time() - start_time))