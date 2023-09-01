def find_words(idx, word_count, word_by_idx, result):
    if idx >= len(target):
        print(' '.join(result))
        return
    if idx not in word_by_idx:
        return
    for word in word_by_idx[idx]:
        if word_count[word] == 0:
            continue
        result.append(word)
        word_count[word] -= 1
        find_words(idx + len(word), word_count, word_by_idx, result)
        word_count[word] += 1
        result.pop()


sub_strings = input().split(', ')
target = input()

word_count = {}
word_by_idx = {}

for word in sub_strings:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

        try:
            idx = 0
            while True:
                idx = target.index(word, idx)
                if idx not in word_by_idx:
                    word_by_idx[idx] = []
                word_by_idx[idx].append(word)
                idx += len(word)
        except ValueError:
            pass

find_words(0, word_count, word_by_idx, [])
