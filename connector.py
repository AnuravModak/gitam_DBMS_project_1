import mysql.connector
from mysql.connector import Error

def connector(name,email,mobile,password):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='gitam',
                                             user='root',
                                             password='')
        if connection.is_connected():
            db_Info = connection.get_server_info()

            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            # SQL query to move to database
            record = cursor.fetchone()  # this will fetch gitam database name
            print("You're connected to database: ", record)
            query = "INSERT INTO registration VALUES('{}','{}','{}','{}')".format(name,email,mobile,password)
            print(query)
            cursor.execute(query)
            connection.commit()
            print(cursor.rowcount, "Record inserted successfully into Laptop table")
            cursor.close()

    except Error as e:
        return  e
    finally:
        if connection.is_connected():
            connection.close()
            return "Your data is stored in database"


if __name__ == '__main__':
    print(connector("a","anuravmodak1@gmail.com","","d"))