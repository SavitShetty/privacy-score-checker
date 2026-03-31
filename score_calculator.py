def calculate_score(password, two_fa, public_wifi, permissions):
    score = 50

    if password == "strong":
        score += 20
    elif password == "weak":
        score -= 10

    if two_fa == "yes":
        score += 20
    else:
        score -= 10

    if public_wifi == "yes":
        score -= 15

    if permissions == "high":
        score -= 15
    elif permissions == "low":
        score += 10

    return max(0, min(score, 100))