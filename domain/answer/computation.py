import math

SCALE_FACTOR = 1.7


def compute_theta(difficulty, discrimination, pseudoguess):
    return difficulty + (1 / (SCALE_FACTOR * discrimination)) * math.log(0.5 * (1 + math.sqrt(1 + 8 * pseudoguess)))


def compute_probability_correct(theta, difficulty, discrimination, pseudoguess):
    exponential = math.exp(SCALE_FACTOR * discrimination * (theta - difficulty))
    return pseudoguess + (((1 - pseudoguess) * exponential) / (1 + exponential))


def compute_probability_wrong(probability_correct):
    return 1 - probability_correct


def compute_iif(probability_correct, probability_wrong):
    return probability_correct * probability_wrong


def compute_se(iifs):
    sum_iifs = 0
    for value in iifs:
        sum_iifs = sum_iifs + value
    return 1 / (math.sqrt(sum_iifs))
