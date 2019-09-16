
class Question:

    # def __init__(self, id, description, difficulty, discrimination, pseudoguess):
    #     self.id = id,
    #     self.description = description
    #     self.difficulty = difficulty
    #     self.discrimination = discrimination
    #     self.pseudoguess = pseudoguess

    def __init__(self,
                 id,
                 description,
                 difficulty,
                 discrimination,
                 pseudoguess,
                 choice_1,
                 choice_2,
                 choice_3,
                 choice_4,
                 choice_5,
                 choice_1_correct,
                 choice_2_correct,
                 choice_3_correct,
                 choice_4_correct,
                 choice_5_correct):
        self.id = id
        self.description = description
        self.difficulty = difficulty
        self.discrimination = discrimination
        self.pseudoguess = pseudoguess
        self.choice_1 = choice_1
        self.choice_2 = choice_2
        self.choice_3 = choice_3
        self.choice_4 = choice_4
        self.choice_5 = choice_5
        self.choice_1_correct = choice_1_correct
        self.choice_2_correct = choice_2_correct
        self.choice_3_correct = choice_3_correct
        self.choice_4_correct = choice_4_correct
        self.choice_5_correct = choice_5_correct
