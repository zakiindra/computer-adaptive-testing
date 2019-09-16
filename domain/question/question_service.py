from domain.choice.choice import Choice
from domain.question.question import Question


class QuestionService:

    def __init__(self, question_repository, choice_repository):
        self.question_repository = question_repository

    def create_question(self, question_form):
        question = self._to_question(question_form)
        return self.question_repository.create(question)

    def get_all_questions(self):
        return self.question_repository.read_all()

    def get_question_by_id(self, id):
        return self.question_repository.read_by_id(id)

    def update_question(self, question_form, id):
        question = self._to_question(question_form, id)
        return self.question_repository.update(question)

    def delete_question_by_id(self, id):
        return self.question_repository.delete_by_id(id)

    def _to_question(self, question_form, id=None):
        return Question(
            id,
            question_form.description.data,
            float(question_form.difficulty.data),
            float(question_form.discrimination.data),
            float(question_form.pseudoguess.data),
            question_form.choice_1.data,
            question_form.choice_2.data,
            question_form.choice_3.data,
            question_form.choice_4.data,
            question_form.choice_5.data,
            question_form.choice_1_correct.data,
            question_form.choice_2_correct.data,
            question_form.choice_3_correct.data,
            question_form.choice_4_correct.data,
            question_form.choice_5_correct.data,
        )

    # def _to_choices(self, question_form, question_id):
    #     choices = []
    #     choice_1 = Choice(None, question_id, question_form.choice_1.data, question_form.choice_1_correct.data)
    #     choice_2 = Choice(None, question_id, question_form.choice_2.data, question_form.choice_2_correct.data)
    #     choice_3 = Choice(None, question_id, question_form.choice_3.data, question_form.choice_3_correct.data)
    #     choice_4 = Choice(None, question_id, question_form.choice_4.data, question_form.choice_4_correct.data)
    #     choice_5 = Choice(None, question_id, question_form.choice_5.data, question_form.choice_5_correct.data)
