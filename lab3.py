class Director:
    def __init__(self, constructor):
        self.constructor = constructor

    def build_query(self, columns, table, conditions, limit):
        return (self.constructor
                    .select(columns)
                    .table(table)
                    .where(conditions)
                    .limit(limit)
                    .get_query())

class IQueryConstructor:
    def select(self, columns):
        pass

    def table(self, table):
        pass

    def where(self, conditions):
        pass

    def limit(self, limit):
        pass

    def get_query(self):
        pass

class MySQLConstructor(IQueryConstructor):
    def __init__(self):
        self.query = []

    def select(self, columns):
        self.query.append(f"SELECT {columns}")
        return self

    def table(self, table):
        self.query.append(f"FROM {table}")
        return self

    def where(self, conditions):
        self.query.append(f"WHERE {conditions}")
        return self

    def limit(self, limit):
        self.query.append(f"LIMIT {limit}")
        return self

    def get_query(self):
        return " ".join(self.query) + ";"

class PostgreSQLConstructor(IQueryConstructor):
    def __init__(self):
        self.query = []

    def select(self, columns):
        self.query.append(f"SELECT {columns}")
        return self

    def table(self, table):
        self.query.append(f"FROM {table}")
        return self

    def where(self, conditions):
        self.query.append(f"WHERE {conditions}")
        return self

    def limit(self, limit):
        self.query.append(f"LIMIT {limit}")
        return self

    def get_query(self):
        return " ".join(self.query) + ";"


if __name__ == "__main__":
    postgres_builder = PostgreSQLConstructor()
    postgres_director = Director(postgres_builder)
    postgres_query = postgres_director.build_query("name, age", "Customers", "Bonus_amount > 30", 10)
    print("PostgreSQL ->", postgres_query)

    mysql_builder = MySQLConstructor()
    mysql_director = Director(mysql_builder)
    mysql_query = mysql_director.build_query("name, age", "Customers", "Bonus_amount > 30", 10)
    print("MySQL ->", mysql_query)
