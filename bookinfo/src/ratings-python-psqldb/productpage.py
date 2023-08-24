from flask import Flask
from flask import jsonify
import sys
import logging
import psycopg2


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%b-%d-%y %H:%M:%S', level=logging.DEBUG)
app = Flask(__name__)


@app.route('/ratings/0', methods=['GET'])
def get_ratings():
    # conn = psycopg2.connect(host='bookinfo1.cluster-cipmtekhijjz.ap-south-1.rds.amazonaws.com', database='test',
    #                         user='bookinfo', password='postgres', port='5432')
    # psqldb should be external service for Aurora posgresql RDS
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
            print(error)


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

