# Ratings module backed by database: PostgreSQL or MongoDB Atlas
# Version: 1.0
# Author: Naresh Bandi
from flask import Flask
from flask import jsonify
import sys
import logging
import psycopg2
import pymongo
import os

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%b-%d-%y %H:%M:%S', level=logging.DEBUG)
app = Flask(__name__)

# Env variables
dbType = "psqldb" if (os.environ.get("DB_TYPE") is None) else os.environ.get("DB_TYPE")


@app.route('/ratings/0', methods=['GET'])
def get_ratings():
    if dbType == 'psqldb':
        conn = psycopg2.connect(host='psqldb', database='test', user='bookinfo', password='postgres', port='5432')
        with conn.cursor() as cursor:
            try:
                cursor.execute('SELECT Rating FROM ratings')
                data = cursor.fetchall()
                result = {"id": 0, "ratings": {
                    'Reviewer1': data[0][0],
                    'Reviewer2': data[1][0]
                }}
                return jsonify(result)
            except (Exception, psycopg2.DatabaseError) as error:
                logging.info(error)
    else:
        # DB connection URL
        # conn_str = "mongodb://mongodb:27017/test"
        # Create connection with DB
        conn_str = "mongodb+srv://bookinfo:<password>@cluster0.7ckhkeh.mongodb.net/?retryWrites=true&w=majority"
        conn = pymongo.MongoClient(conn_str)
        # Create DB
        # ratings_db = conn['test']
        # # Create collection (table)
        # ratings_collection = ratings_db['ratings']
        # # Create a Record document in Json format
        # # ratings_data1 = { "rating": 3}
        # # ratings_data2 = { "rating": 1}
        # ratings_list = [3, 1]
        # # Insert the data
        # res = ratings_collection.insert_many(([{'rating': i} for i in ratings_list]))
        # logging.info(res.inserted_ids)
        # logging.info(conn.list_database_names())
        # Reading the document
        db = conn.get_database('test')
        data = db.get_collection('ratings')
        # data.insert_many(([{'rating': i} for i in ratings_list]))
        # logging.info(data)
        res = data.find({})
        result = {"id": 1, "ratings": {
            'Reviewer1': res[0]['rating'],
            'Reviewer2': res[1]['rating']
        }}
        return jsonify(result)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        logging.error("usage: %s port" % (sys.argv[0]))
        sys.exit(-1)

    p = int(sys.argv[1])
    logging.info("start at port %s" % (p))
    # Make it compatible with IPv6 if Linux
    if sys.platform == "linux":
        app.run(host='::', port=p, debug=True, threaded=True)
    else:
        app.run(host='0.0.0.0', port=p, debug=True, threaded=True)
