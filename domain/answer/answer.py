
class Answer:

    def __init__(self,
                 id,
                 user_id,
                 question_id,
                 question_order,
                 choice_id,
                 is_correct,
                 theta,
                 probability_correct,
                 probability_wrong,
                 iif,
                 se):
        self.id = id
        self.user_id = user_id
        self.question_id = question_id
        self.choice_id = choice_id
        self.is_correct = is_correct
        self.question_order = question_order
        self.theta = theta
        self.probability_correct = probability_correct
        self.probability_wrong = probability_wrong
        self.iif = iif
        self.se = se
