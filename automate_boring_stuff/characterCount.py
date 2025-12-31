messsage = "It was a bright and cold day in april, and the clocks were ticking to thirteen."
count = {}

for character in messsage:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

print(count)
