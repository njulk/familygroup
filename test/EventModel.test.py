import sys
sys.path.append('..')

from model.EventModel import *

print(list(getEvents()))

print(getEventById(1))

# print(postEvent({'createuserid': 1, 'groupid': 1, 'eventname': 'red'}))

print(putEvent(1,{'eventname': 'green'}))

print(deleteEvent(1))