# Yusuf provided this code ... I did not code this code ... fun to run
import random
from tqdm import trange, tqdm
from random import randint

# numlist = []
# for i in range(100):
#     numlist.append(random.randint(1, 1000))
#     print(numlist)

'''
note: If you receive an ImportError, NameError or message stating there is no module named tqdm, run the following in your terminal:
    python -m pip install tqdm
you may also have to run:
    python -c 'import tqdm'

I needed to run the first command only in this comment
'''

# for-loop

heads = 0
tails = 0

for i in tqdm(range(500), desc='Coin Flip Progress'):
    toss = randint(0, 1)
    if toss == 0:
        heads += 1
    else:
        tails += 1
print(heads, tails)
print(f"The difference between heads and tails is " + str(abs(heads - tails)) + " coin tosses.")

# Nested for-loop
num_games = 3

for game in tqdm(range(num_games), desc='Outer Loop Progress'):
    heads = 0
    tails = 0
    
    for j in trange((5000000), desc=f'Game {game+1} Inner Loop Progress'):
        toss = randint(0, 1)
        if toss == 0:
            heads += 1
        else:
            tails += 1
    print(f'Heads: {heads}, Tails: {tails}')
    print(f"The difference between heads and tails is " + str(abs(heads - tails)) + " coin tosses.")