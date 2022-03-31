from app.models import DatabaseConnector
from psycopg2 import sql


class Email(DatabaseConnector):

    def __init__(self, code: int, email: str) -> None:
        self.code = code
        self.email = email

    @classmethod
    def create_table_if_not_exits(self):
        self.get_conn_cur()
        query = """
            create table if not exists emails_para_verificar(
                code        INTEGER         NOT NULL,
                email       VARCHAR(100)    NOT NULL unique,
                tentativas  INTEGER         DEFAULT 3
            )
        """
        self.cur.execute(query)

        self.commit_and_close()

    def create_user(self):

        self.get_conn_cur()

        query = """
            INSERT INTO emails_para_verificar
                (code, email)
            VALUES
                (%s, %s)
            RETURNING *
        """

        query_values = tuple(self.__dict__.values())

        self.cur.execute(query, query_values)

        user_inserido = self.cur.fetchone()

        self.commit_and_close()

        return user_inserido

    # @classmethod
    # def serialize(cls, data: tuple):
    #     return dict(zip(cls.series_columns, data))

    @classmethod
    def obter_codigo_ou_tentativas_por_email(self, email, payload: list = ["code"]):
        self.get_conn_cur()

        columns = [sql.Identifier(key) for key in payload]


        email_user = sql.Literal(email)

        query = sql.SQL("""
            SELECT {columns} FROM emails_para_verificar WHERE email = {email};
        """).format(
            email=email_user,
            columns=sql.SQL(",").join(columns)
        )

        self.cur.execute(query)

        codigo_do_email = self.cur.fetchone()

        self.commit_and_close()
        if codigo_do_email:
            return dict(codigo_do_email)

        return codigo_do_email

    @classmethod
    def atualizar_code_por_email(self, email: str, payload: dict):
        self.get_conn_cur()

        columns = [sql.Identifier(key) for key in payload.keys()]
        values = [sql.Literal(value) for value in payload.values()]
        email_update_code = sql.Literal(email)
        # values = sql.Literal(code)

        query = sql.SQL(
            """
            UPDATE
                emails_para_verificar
            SET
                ({columns}) = ROW({values})
            WHERE
                email = {email}
            RETURNING *;
            """
        ).format(
            columns=sql.SQL(",").join(columns),
            values=sql.SQL(",").join(values),
            email=email_update_code
        )

        self.cur.execute(query)

        self.commit_and_close()
        # return code
