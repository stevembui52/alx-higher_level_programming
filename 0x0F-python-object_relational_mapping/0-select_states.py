#!/usr/bin/python3
"""List state database hbtn_0e_0_usa"""

if __name__ == "__main__":

    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(user=argv[1], passwd=argv[2],
                           db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    """Close all cursors"""
    cur.close()
