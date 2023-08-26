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
dbType = "mongodb" if (os.environ.get("DB_TYPE") is None) else os.environ.get("DB_TYPE")
psqldbHost = "bookinfo1-instance-1.cipmtekhijjz.ap-south-1.rds.amazonaws.com" if (os.environ.get("PDB_HOST") is None) else os.environ.get("PDB_HOST")
psqldbName = "test" if (os.environ.get("PDB_NAME") is None) else os.environ.get("PDB_NAME")
psqldbUser = "bookinfo" if (os.environ.get("PDB_USER") is None) else os.environ.get("PDB_USER")
psqldbPasswd = "postgres" if (os.environ.get("PDB_PASSWD") is None) else os.environ.get("PDB_PASSWD")
psqldbPort = "5432" if (os.environ.get("PDB_PASSWD") is None) else os.environ.get("PDB_PASSWD")
mongodbUrl = "mongodb+srv://bookinfo:postgres@cluster0.7ckhkeh.mongodb.net/?retryWrites=true&w=majority" if (os.environ.get("MONGODB_URL") is None) else os.environ.get("MONGODB_URL")


@app.route('/ratings/0', methods=['GET'])
def get_ratings():
    if dbType == 'psqldb':
        conn = psycopg2.connect(host=psqldbHost, database=psqldbName, user=psqldbUser, password=psqldbPasswd, port=psqldbPort)
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
        conn = pymongo.MongoClient(mongodbUrl)
        # Reading the document
        try:
            db = conn.get_database('test')
            data = db.get_collection('ratings')
            res = data.find({})
            result = {"id": 0, "ratings": {
                'Reviewer1': res[0]['rating'],
                'Reviewer2': res[1]['rating']
            }}
            return jsonify(result)
        except Exception as error:
            logging.info(error)


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
