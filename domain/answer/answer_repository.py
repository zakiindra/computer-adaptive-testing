import mysql.connector as mysql

from domain.answer.answer import Answer


class AnswerRepository:

    def __init__(self, config):
        self.db = mysql.connect(
            host=config.MYSQL_HOST,
            database=config.MYSQL_DATABASE,
            user=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD
        )

    def create(self, answer):
        cursor = self.db.cursor()
        cursor.execute("""
            INSERT INTO answer(user_id, question_id, question_order, theta, probability_correct, probability_wrong, iif, se)
            VALUE (%s, %s, %s, %s, %s, %s, %s, %s)""",
            (answer.user_id, answer.question_id, answer.question_order, answer.theta, answer.probability_correct, answer.probability_wrong, answer.iif, answer.se))
        cursor.close()
        return answer

    def read_all(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM answer ORDER BY id")
        rows = cursor.fetchall()
        cursor.close()

        answers = []
        for row in rows:
            answers.append(self._row_to_answer(row))
        return answers

    def read_by_id(self, id):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM answer WHERE id = %s" % id)
        row = cursor.fetchone()
        return self._row_to_answer(row)

    def update_by_id(self, answer):
        cursor = self.db.cursor()
        cursor.execute("""
            UPDATE answer
            SET user_id = %s, question_id = %s, question_order = %s, theta = %s, probability_correct = %s, probability_wrong = %s, iif = %s, se = %s
            WHERE id = %s""",
            (answer.user_id, answer.question_id, answer.question_order, answer.theta, answer.probability_correct, answer.probability_wrong, answer.iif, answer.se))
        cursor.close()
        return answer

    def delete_by_id(self, id):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM answer WHERE id = %s" % id)
        cursor.close()
        return id

    def _row_to_answer(self, row):
        return Answer(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
