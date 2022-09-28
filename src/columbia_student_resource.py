import pymysql

import os


class ColumbiaStudentResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():

        # usr = os.environ.get("DBUSER")
        # pw = os.environ.get("DBPW")
        # h = os.environ.get("DBHOST")
        #
        # conn = pymysql.connect(
        #     user=usr,
        #     password=pw,
        #     host=h,
        #     cursorclass=pymysql.cursors.DictCursor,
        #     autocommit=True
        # )

        # conn = pymysql.connect(
        #     host="localhost",
        #     port=3306,
        #     user="root",
        #     password="dbuserdbuser",
        #     cursorclass=pymysql.cursors.DictCursor,
        #     autocommit=True
        # )

        conn = pymysql.connect(
            host="yw3912.cvjaygaiwg1r.us-east-1.rds.amazonaws.com",
            port=3306,
            user="admin",
            password="dbuserdbuser",
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )

        return conn

    @staticmethod
    def get_by_key(key):

        # sql = "SELECT * FROM f22_databases.columbia_students where guid=%s"
        sql = "SELECT * FROM f22_databases.columbia_student where uni=%s"
        conn = ColumbiaStudentResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchone()

        return result
