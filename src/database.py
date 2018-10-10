from config.settings import DB_NAME, DB_USER, DB_USER_PASSWORD
import psycopg2


class DataBase:
    def __init__(self):
        """
        Init connection to database
        """
        self.db_name = DB_NAME
        self.db_user = DB_USER
        self.db_user_password = DB_USER_PASSWORD
        self.conn = psycopg2.connect(database=self.db_name, user=self.db_user, host='localhost',
                                     password=self.db_user_password)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS nafta_users (id serial PRIMARY KEY, user_id integer, group_name varchar(100));")
        self.conn.commit()

    def add_user(self, user_id: int, group_name: str):
        """
        Add user to database with group name
        :param user_id: id of user
        :param group_name: name of group max_len=10
        """
        self.cursor.execute(
            f"INSERT INTO public.nafta_users (id, user_id, group_name) VALUES (DEFAULT, {user_id}, '{group_name}');")
        self.conn.commit()

    def change_group_name(self, user_id: int, group_name: str):
        """
        Change group in user
        :param user_id: id of user
        :param group_name: name of group max_len=10
        """
        self.cursor.execute(f"UPDATE public.nafta_users SET group_name = '{group_name}' WHERE user_id = {user_id}")
        self.conn.commit()

    def get_group_name(self, user_id) -> str:
        """
        Function get group name by user id
        :param user_id: id of user
        :return: group name
        """
        self.cursor.execute(f"SELECT group_name FROM nafta_users where user_id = {user_id}")
        return self.cursor.fetchone()[0]

    def user_id_exists(self, user_id):
        self.cursor.execute(f"SELECT group_name FROM nafta_users where user_id = {user_id}")
        return self.cursor.fetchone() is not None

    def delete_user(self, user_id: int):
        """
        Delete user from database
        :param user_id: id of user
        """
        self.cursor.execute(
            f"DELETE FROM public.nafta_users WHERE user_id = {user_id};")
        self.conn.commit()

    def close(self):
        """
        Close connection with database
        """
        self.conn.close()
