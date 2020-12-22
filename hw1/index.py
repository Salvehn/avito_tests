import typing


def get_multi_from_level(level: int):
    if not (isinstance(level, int)):
        return None
    if (level < 7) | (level > 17):
        return None
    multi_bonus_level: float = 0
    if level < 10:
        multi_bonus_level = 0.05
    elif 10 <= level < 13:
        multi_bonus_level = 0.1
    elif 13 <= level < 15:
        multi_bonus_level = 0.15
    elif level >= 15:
        multi_bonus_level = 0.2
    else:
        multi_bonus_level = None
    return multi_bonus_level


def get_multi_from_review(review_score: float):
    if not (isinstance(review_score, float) or isinstance(review_score, int)):
        return None
    if (review_score < 1) | (review_score > 5):
        return None
    multi_bonus_review: float = 0
    if (review_score >= 2) & (review_score < 2.5):
        multi_bonus_review = 0.25
    elif (review_score >= 2.5) & (review_score < 3):
        multi_bonus_review = 0.5
    elif (review_score >= 3) & (review_score < 3.5):
        multi_bonus_review = 1
    elif (review_score >= 3.5) & (review_score < 4):
        multi_bonus_review = 1.5
    elif review_score >= 4:
        multi_bonus_review = 2
    return multi_bonus_review





def salary_check(salary):
    if not isinstance(salary, int):
        return None
    if 70000 <= salary <= 750000:
        return salary
    return None


def calculate_bonus(level: int, review: float, salary: int,quartal:int = 3):
    multi_level = get_multi_from_level(level)
    if multi_level is None:
        return "wrong level multi"
    multi_review = get_multi_from_review(review)
    if multi_review is None:
        return "wrong review multi"
    true_salary = salary_check(salary)
    if true_salary is not None:
        bonus = quartal * true_salary * multi_level
        return bonus*multi_review
    else:
        return "wrong salary value"
