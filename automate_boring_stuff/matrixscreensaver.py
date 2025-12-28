"""import random, sys, time

WIDTH = 70

try:
    columns = [0] * WIDTH
    while True:
        for i in range(WIDTH):
            if random.random() < 0.02:
                columns[i] = random.randint(4,14)

            if columns[i] == 0:
                print('', end='')
            else:
                print(random.choice([0,1]), end='')
                columns[i] -= 1
        print()
        time.sleep(0.1)
except KeyboardInterrupt:
    sys.exit()"""

import random, sys, time

WIDTH = 500

columns = [0] * WIDTH

try:
    while True:
        for i in range(WIDTH):
            if columns[i] == 0:
                if random.random() < 0.02:
                    columns[i] = random.randint(4, 14)
                
                print(' ', end='')
            else:
                print(random.choice(['0', '1']), end='')
                columns[i] -= 1
        
        print(flush=True)
        time.sleep(0.05)
except KeyboardInterrupt:
    sys.exit()
