bird_pos = []
animals = ['새', '코끼리', '강아지', '새', '강아지', '새']
for i, animals in enumerate(animals):
    if (animals=='새'):
        bird_pos.append(i)
print(bird_pos)