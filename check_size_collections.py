#!/usr/bin/python
#-*- coding: utf-8 -*-

from pymongo import MongoClient
db = MongoClient('HOST').your_database

collections = db.collection_names()
collections.sort()
total_size = 0
all_desc = ''

for collection in collections:
    stats = db.command('collStats', collection)
    size_in_mb = round((stats['size']/(1024*1024)), 2)
    desc = '{:.<50} {} MB\n'.format(collection, size_in_mb)
    all_desc += desc
    total_size += size_in_mb

all_desc += '\n{:.<50} {} MB\n'.format('TOTAL', round(total_size, 2))
print(all_desc)
