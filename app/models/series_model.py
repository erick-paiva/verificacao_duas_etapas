from app.models import DatabaseConnector
from psycopg2 import sql


class Serie(DatabaseConnector):

    series_columns = [
        "_id",
        "serie",
        "seasons",
        "released_date",
        "genre",
        "imdb_rating",
    ]

    def __init__(self, data) -> None:
        self.serie = data["serie"]
        self.seasons = data["seasons"]
        self.released_date = data["released_date"]
        self.genre = data["genre"]
        self.imdb_rating = data["imdb_rating"]

    @classmethod
    def create_table_if_not_exits(self):
        self.get_conn_cur()
        query = """
            create table if not exists ka_series(
                id BIGSERIAL PRIMARY key,
                serie VARCHAR(100) NOT NULL unique,
                seasons INTEGER NOT null,
                released_date DATE NOT null,
                genre VARCHAR(50) NOT null,
                imdb_rating FLOAT NOT NULL
            )
        """
        self.cur.execute(query)

        self.commit_and_close()

    @classmethod
    def serialize(cls, data: tuple):
        return dict(zip(cls.series_columns, data))

    def create_serie(self):

        self.get_conn_cur()

        query = """
            INSERT INTO ka_series
                (serie, seasons, released_date, genre, imdb_rating)
            VALUES
                (%s, %s, %s, %s, %s)
            RETURNING *
        """

        query_values = tuple(self.__dict__.values())

        self.cur.execute(query, query_values)

        serie_inserida = self.cur.fetchone()

        self.commit_and_close()

        return serie_inserida

    @classmethod
    def obter_uma_ou_varias_series(self, id=None):

        self.get_conn_cur()
        if id:

            sql_user_id = sql.Literal(id)
            
            query = sql.SQL("""
                SELECT * FROM ka_series WHERE id = {id_serie};
            """).format(id_serie=sql_user_id)

        else:
            query = """
                SELECT * FROM ka_series;
            """

        self.cur.execute(query)

        todas_series_ou_uma = self.cur.fetchone() if id else self.cur.fetchall()

        self.commit_and_close()

        return todas_series_ou_uma
