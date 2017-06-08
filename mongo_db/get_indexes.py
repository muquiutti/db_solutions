from pymongo import MongoClient
db2 = MongoClient('localhost:27017').your_database

collections = db2.collection_names()
indexes = {}
keys = {}


def lower_case(boolean):
    string = str(boolean)
    return string.lower()

i = 0
for collection in collections:
    indexes.update({collection: db2[collection].index_information()})
    print(collection)
    print('//--------------')

    for index in indexes[collection].iterkeys():
        dic_keys = {}
        dic_properties = {}

        for key in indexes[collection][index]['key']:
            dic_keys.update({key[0]: key[1]})

        if 'unique' in indexes[collection][index]:
            dic_properties.update({'unique': lower_case(indexes[collection][index]['unique'])})
        if 'sparse' in indexes[collection][index]:
            dic_properties.update({'sparse': lower_case(indexes[collection][index]['sparse'])})
        if 'expireAfterSeconds' in indexes[collection][index]:
            dic_properties.update({'expireAfterSeconds': lower_case(indexes[collection][index]['expireAfterSeconds'])})

        print ('db.%s.createIndex(%s, %s)' % (collection, dic_keys, dic_properties))

    print('//---------------')
