import mysql.connector as mysql

from domain.question.question import Question


class QuestionRepository:

    def __init__(self, config):
        self.db = mysql.connect(
            host=config.MYSQL_HOST,
            database=config.MYSQL_DATABASE,
            user=config.MYSQL_USER,
            password=config.MYSQL_PASSWORD
        )
        self.db.autocommit = True

    # def create(self, question):
    #     print(question.description)
    #     print(question.difficulty)
    #     print(question.discrimination)
    #     print(question.pseudoguess)
    #     print('Inserting question ({}, {}, {}, {})'.format(question.description, question.difficulty, question.discrimination, question.pseudoguess))
    #     cursor = self.db.cursor()
    #     cursor.execute("""
    #         INSERT INTO question(`description`, `difficulty`, `discrimination`, `pseudoguess`)
    #         VALUE (%s, %s, %s, %s)""",
    #         (question.description, question.difficulty, question.discrimination, question.pseudoguess))
    #     insert_id = cursor.lastrowid
    #     cursor.close()
    #     print(insert_id)
    #     print('Insertion done')
    #     return question

    def create(self, question):
        print('Inserting question:'
              ' ({}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(question.description,
                                                                                 question.difficulty,
                                                                                 question.discrimination,
                                                                                 question.pseudoguess,
                                                                                 question.choice_1,
                                                                                 question.choice_2,
                                                                                 question.choice_3,
                                                                                 question.choice_4,
                                                                                 question.choice_5,
                                                                                 question.choice_1_correct,
                                                                                 question.choice_2_correct,
                                                                                 question.choice_3_correct,
                                                                                 question.choice_4_correct,
                                                                                 question.choice_5_correct,
                                                                                 ))
        cursor = self.db.cursor()
        cursor.execute("""
            INSERT INTO question(description, difficulty, discrimination, pseudoguess, choice_1, choice_2, choice_3, choice_4, choice_5, choice_1_correct, choice_2_correct, choice_3_correct, choice_4_correct, choice_5_correct)
            VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""",
            (question.description,
             question.difficulty,
             question.discrimination,
             question.pseudoguess,
             question.choice_1,
             question.choice_2,
             question.choice_3,
             question.choice_4,
             question.choice_5,
             question.choice_1_correct,
             question.choice_2_correct,
             question.choice_3_correct,
             question.choice_4_correct,
             question.choice_5_correct
             ))
        cursor.close()
        print('Insertion done')
        return question

    def read_all(self):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM question ORDER BY id")
        rows = cursor.fetchall()
        cursor.close()

        questions = []
        for row in rows:
            questions.append(self._row_to_question(row))
        return questions

    def read_by_id(self, id):
        cursor = self.db.cursor()
        cursor.execute("SELECT * FROM question WHERE id = %s" % id)
        row = cursor.fetchone()
        return self._row_to_question(row)

    def update(self, question):
        cursor = self.db.cursor()
        cursor.execute("""
            UPDATE question
            SET description = %s, difficulty = %s, discrimination = %s, pseudoguess = %s
            WHERE id = %s""",
                       (question.description, question.difficulty, question.discrimination, question.pseudoguess,
                        question.id))
        cursor.close()
        return question

    def delete_by_id(self, id):
        cursor = self.db.cursor()
        cursor.execute("DELETE FROM question WHERE id = %s" % id)
        cursor.close()
        return id

    def _row_to_question(self, row):
        return Question(row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6],
                        row[7],
                        row[8],
                        row[9],
                        row[10],
                        row[11],
                        row[12],
                        row[13],
                        row[14])
