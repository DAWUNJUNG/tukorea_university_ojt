people = ['홍', '홍', '김', '이', '홍', '김']
def max_count(people):
    counts = {}
    for i in people:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts
counts = max_count(people)

first = []
max_num = max(counts.values())
for name, count in counts.items():
    print(name, ':', count, '번')
    if count == max_num:
        first.append(name)
print('1등:', first)