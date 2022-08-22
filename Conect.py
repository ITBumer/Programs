import pymysql


connection = pymysql.connect (
                             host='localhost',
                             user='rubin',
                             password='3Ptz#5Xv*ZHH',
                             database='rubin_ra',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor
                             )
