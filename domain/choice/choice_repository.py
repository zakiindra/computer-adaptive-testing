import mysql.connector as mysql

from domain.choice.choice import Choice


class ChoiceRepository:

    def __init__(self, config):
        self.db = mysql.connect(
            host=config.MYSQL_HOST,
            database=config.MYSQL_DATABASE,
            user=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD
        )

    def create(self, choice):
        cursor = self.db.cursor()
        cursor.execute("""
            INSERT INTO choice(question_id, description, is_correct)
            VALUE (%s, %s, %s)""",
            (choice.question_id, choice.description, choice.is_correct))
        cursor.close()
        return choice

    def bulk_create(self, choices):
        cursor = self.db.cursor()
        cursor.executemany("""
            INSERT INTO choice(question_id, description, is_correct)
            VALUE (%s, %s, %s)""",
            choices)
        cursor.close()
        return choices

    def read_by_question_id(self, id):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM choice WHERE question_id = %s" % id)
        rows = cursor.fetchall()
        cursor.close()

        choices = []
        for row in rows:
            choices.append(self._row_to_choice(row))
        return choices

    def update_by_id(self, choice):
        cursor = self.db.cursor()
        cursor.execute("""
            UPDATE choice
            SET question_id = %s, description = %s, is_correct = %s
            WHERE id = %s""",
            (choice.question_id, choice.description, choice.is_correct))
        cursor.close()
        return choice

    def delete_by_id(self, id):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM choice WHERE id = %s" % id)
        cursor.close()
        return id

    def _row_to_choice(self, row):
        return Choice(row[0], row[1], row[2], row[3])
