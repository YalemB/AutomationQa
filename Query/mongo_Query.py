from Base.Mongo.mongoconnect import MongoDB

x = MongoDB('test', 'test1')

# MongoDB('arsenal_squad', 'players').find()

# print(x.db.list_collection_names())

# inserting one value
# to_insert = {"name": "damian marley", "occupation": "Reggae"}
# print(x.col.insert_one(to_insert).inserted_id)

#inserting multiple values
#
# to_insert = [
#     {"name": "akon", "occupation": "pop singer"},
#     {"name": "lil wayne", "occupation": "Rapper"},
#     {"name": "drake", "occupation": "Pop-star"},
#     {"name": "j cole", "occupation": "Rapper"},
#     {"name": "burna boy", "occupation": "Afro-beat"}
#
# ]
# print(x.col.insert_many(to_insert).inserted_ids)