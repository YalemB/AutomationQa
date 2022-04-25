import pymongo
import dns

# client = pymongo.MongoClient(
#     "mongodb+srv://yalem:Yalem1994@cluster0.6yhzq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client['arsenal_squad']
# col = db['players']

class MongoDB():
    def __init__(self,db,col):
        self.client = pymongo.MongoClient(
            "mongodb+srv://yalem:Yalem1994@cluster0.6yhzq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.client[db]
        self.col = self.db[col]
    def find(self,q=""):
        for i in self.col.find(q):  # fetch all doc records
            print(i)












# dic = {"player_name":"Temmy Abraham","player_shirt_num":99,"positon":"Striker"} # add one new value to doc
#
# x = col.insert_one(x)


# dic2 = {"player_name":"Laczet"} # delete one value from doc
# y = col.delete_one(dic)
# print(x)

# z = col.find_one() # fetch fire doc value
# print(x)

# for i in col.find(): # fetch all doc records
#     print(i)

# for i in col.find({'player_shirt_num':{"$gt":16}}, {'_id': 0, 'birthdate': 0}):  #fetch all squad players name shirt number and position
#     print(i)
