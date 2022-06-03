import sqlite3, json

class Entity(list):

    @staticmethod
    def __loadAll__(conn, query):
        try:
            # conn.row_factory = 
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()

            return rows
        except Exception as ex:
            return list()

    @staticmethod
    def __load__(conn, query):
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchone()
            cursor.close()

            return rows
        except Exception as ex:
            return list()

    @staticmethod
    def __toList__(t, rows):
        _list = list()

        try:
            for row in rows:
                try:
                    obj = t(**row)
                    _list.append(obj.__dict__)
                except Exception as ex:
                    print(ex)

            return _list
        except Exception as ex:
            _list = list()

        return _list

    @staticmethod
    def __toObject__(t, rows):
        _obj = None

        try:
            _obj = t(**rows)
            _obj = _obj.__dict__
        except Exception as ex:
            _obj = None

        return _obj

    @staticmethod
    def Execute(conn, query):

        try:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()
        except Exception as ex:
            print(ex)
