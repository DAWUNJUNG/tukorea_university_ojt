text = "AI! 나는 인공지능 로봇 입니다. 나는 'AI 로봇' 입니다."
def max_counts(text):
    skips = ['.', ',', ';', ':', '\'', '!']
    for ch in skips:
        text = text.replace(ch, '')
    counts = {}
    for i in text.split(' '):
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    return counts
print(max_counts(text))