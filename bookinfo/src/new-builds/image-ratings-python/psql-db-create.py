import psycopg2

conn = psycopg2.connect(host='bookinfo1.cluster-cipmtekhijjz.ap-south-1.rds.amazonaws.com', database='template1',
                        user='bookinfo', password='postgres', port='5432')

conn.autocommit = True

with conn.cursor() as cur:
    try:
        cur.execute("CREATE DATABASE test")
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

# statements = ["CREATE TABLE ratings (ReviewID INT NOT NULL, Rating INT, PRIMARY KEY (ReviewID))", "INSERT INTO ratings (ReviewID, Rating) VALUES (1, 2)", "INSERT INTO ratings (ReviewID, Rating) VALUES (2, 4)"]
#
# with conn.cursor() as cur:
#     try:
#         for statement in statements:
#             cur.execute(statement)
#         conn.commit()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print(error)