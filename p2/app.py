from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

STUDENTS = 'students'


class DbEngine():
    db_engine = None

    def createDB(self):
        self.db_engine = create_engine('sqlite:///mydb.sqlite')
        print(self.db_engine)

    def create_db_tables(self):
        metadata = MetaData()
        users = Table(STUDENTS, metadata,
                      Column('id', Integer, primary_key=True),
                      Column('first_name', String),
                      Column('last_name', String)
                      )

        try:
            metadata.create_all(self.db_engine)
            print("Tables created")
        except Exception as e:
            print("Error occurred during Table creation!")
            print(e)

    def print_all_data(self, table='', query=''):
        query = query if query != '' else "SELECT * FROM '{}';".format(table)
        print(query)

        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
            except Exception as e:
                print(e)
            else:
                for row in result:
                    print(row)  # print(row[0], row[1], row[2])
                result.close()

    print("\n")

    def SQLExcute(self):
        query = "SELECT first_name, last_name FROM {TBL_students} WHERE " \
            "last_name LIKE 'M%';".format(TBL_students=STUDENTS)
        self.print_all_data(query=query)

    def sample_insert(self):
        # Insert Data
        query = "INSERT INTO {}(id, first_name, last_name) " \
                "VALUES (3, 'Terrence','Jordan');".format(STUDENTS)
        self.execute_query(query)
        self.print_all_data(STUDENTS)

       # Insert, Update, Delete
    def execute_query(self, query=''):
        if query == '':
            return

        print(query)
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)

    def sample_delete(self):
        # Delete Data by Id
        query = "DELETE FROM {} WHERE id=3".format(STUDENTS)
        self.execute_query(query)
        self.print_all_data(STUDENTS)

        # Delete All Data
        '''
        query = "DELETE FROM {}".format(USERS)
        self.execute_query(query)
        self.print_all_data(USERS)
        '''


def main():
    dbEngine = DbEngine()
    dbEngine.createDB()
    dbEngine.create_db_tables()
    dbEngine.sample_insert()
    dbEngine.SQLExcute()


if __name__ == "__main__":
    main()
