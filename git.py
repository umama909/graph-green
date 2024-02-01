import os, random

for i in range(50):
    d = str(i) + ' days ago'  # Fixed the assignment for 'd'
    rand = random.randrange(1, 12)  # Fixed the assignment for 'rand'
    with open('test.txt', 'a') as file:
        file.write(d + '\n')
    os.system('git add test.txt')
    os.system('git commit --date="2023-' + str(rand) + '_'+ d + '" -m 1')

os.system('git push -u origin main -f')
