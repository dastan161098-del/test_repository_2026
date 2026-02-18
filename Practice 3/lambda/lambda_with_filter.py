# Example 1
nums = [1,2,3,4,5,6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# Example 2
nums = [10, 3, 7, 20, 5]
greater_than_5 = list(filter(lambda x: x > 5, nums))
print(greater_than_5)

# Example 3: только положительные
nums = [-2, -1, 0, 3, 5]
positives = list(filter(lambda x: x > 0, nums))
print(positives)

# Example 4: строки длиной >3
words = ["hi","python","cat","code"]
long_words = list(filter(lambda w: len(w) > 3, words))
print(long_words)

# Example 5: нечетные числа
nums = [1,2,3,4,5]
odds = list(filter(lambda x: x % 2 == 1, nums))
print(odds)