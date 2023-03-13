weight = 75
height = 175
dist = 9.75
hours = 2
minutes = 2 * 60

calories = (weight * 0.035 + (dist / hours) ** 2 / height * weight * 0.029) * minutes
print(calories)