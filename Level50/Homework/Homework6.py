def categorize_members(members):
    result = []
    for age, handicap in members:
        if age >= 55 and handicap > 7:
            result.append("Senior")
        else:
            result.append("Open")
    return result

