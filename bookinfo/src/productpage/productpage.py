from flask import Flask
from flask import jsonify
import sys
import logging
import mysql.connector


app = Flask(__name__)

@app.route('/ratings/0', methods=['GET'])
def get_ratings():
    c1 = mysql.connector.connect(user='root', password='password',
                                 host='mysqldb', port='3306',
                                 database='test')
    cursor = c1.cursor()
    cursor.execute('SELECT Rating FROM ratings')

    data = cursor.fetchall()
    print(data)
    print()
    print(type(data))
    print(type(data[0][0]))

    result = {"id": 0, "ratings": {
        'Reviewer1': data[0][0],
        'Reviewer2': data[1][0]
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

