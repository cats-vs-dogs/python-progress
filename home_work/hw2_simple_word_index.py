text = 'apple and banana one apple one banana a red apple and a green apple'
words_list = text.split()
print(words_list, '\n', '-'*108)

print('\n', 'FOR LOOP:', '\n')

words = {}
for w in words_list:
    if w not in words:
        words[w] = 1
    else:
        words[w] += 1
for k, v in words.items():
    print('| {:6s} |  {}  |'.format(k, v))


print('\n', 'COUNTER:', '\n')

from collections import Counter
words_count = Counter(words_list)
for k, v in words_count.items():
    print('| {:6s} |  {}  |'.format(k, v))