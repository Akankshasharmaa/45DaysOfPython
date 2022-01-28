"""Frogger"""
def latest(scores):
    """
    return latest entry
    """
    return scores[-1]

def personal_best(scores):
    """
    return max score
    """
    return max(scores)

def personal_top_three(scores):
    """
    return list of highest score
    """
    if len(scores) < 2:
        return scores
    if len(scores) <= 3:
        return list(reversed(sorted(scores)))

    high_score = []
    while len(high_score) < 3:
        m = max(scores)
        n = scores.index(m)
        high_score.append(m)
        scores.pop(n)
    return high_score
