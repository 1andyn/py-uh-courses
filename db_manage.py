import campus
import term
import time
import dbdriver
import dns

# test mongo driver
start_time = time.time()
connection = dbdriver.Database()
connection.rebuild_term()
connection.rebuild_campus()
connection.rebuild_subject()