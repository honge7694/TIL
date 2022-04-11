words = input().upper()
word_list = list(set(words))

words_count = []
for i in word_list:
    cnt = words.count(i)
    words_count.append(cnt)

if words_count.count(max(words_count)) >= 2:
    print("?")
else:
    max_index = words_count.index(max(words_count))
    print(word_list[max_index])



