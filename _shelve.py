# coding=utf-8

import shelve

object = someClass()
db = shelve.open('filename')
db['key'] = object                  # save with the 'key'



#
#   in other file
#

import shelve

dbase = shelve.open('filename')
object = dbase['key']               # get object by 'key'