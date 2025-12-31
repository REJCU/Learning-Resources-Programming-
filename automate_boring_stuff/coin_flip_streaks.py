import random

results = []

number_of_streaks = 0
for experiment_number in range(10000): # Run 100,000 experiments total.
    # Code that creates a list of 100 'heads' or 'tails' values
    results = []
    for i in range(0,100):
        x = random.choice(["H", "T"])
        results.append(x)
    # Code that checks if there is a streak of 6 heads or tails in a row
    has_streak = False
    for i in range(len(results)-6):
        streak = results[i:i+6] 
        if streak == ["H","H","H","H","H","H"] or streak == ['T', 'T', 'T', 'T', 'T', 'T']:
            has_streak = True
            break

    if has_streak:
        number_of_streaks += 1
print('Chance of streak: %s%%' % (number_of_streaks / 100))
