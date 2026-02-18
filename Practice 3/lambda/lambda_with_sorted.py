# Example 1: sort by length
words = ["apple", "kiwi", "banana"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

# Example 2: sort by second element
pairs = [(1, 3), (2, 1), (4, 2)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)

# Example 3: сортировка по последней букве
words = ["apple","banana","kiwi"]
print(sorted(words, key=lambda w: w[-1]))

# Example 4: сортировка чисел по модулю
nums = [-5, 3, -2, 7]
print(sorted(nums, key=lambda x: abs(x)))

# Example 5: сортировка слов по алфавиту (lower)
words = ["Bob", "alice", "Dana"]
print(sorted(words, key=lambda x: x.lower()))