import pymongo
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://bookinfo:<password>@cluster0.7ckhkeh.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
# client = MongoClient(uri)
conn = pymongo.MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    conn.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    #ratings_db = conn['test']
    #ratings_collection = ratings_db['ratings']
    ratings_list = [3, 1]
    print(conn.list_database_names())
    db = conn.get_database('test')
    data = db.get_collection('ratings')
    #record = data.insert_many(([{'rating': i} for i in ratings_list]))
    #print(record)
    res = data.find({})
    print(res)
    print(res[0]['rating'])
    result = {"id": 0, "ratings": {
        'Reviewer1': res[0]['rating'],
        'Reviewer2': res[1]['rating']
    }}
    print(result)
except Exception as e:
    print(e)
