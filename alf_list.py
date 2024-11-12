def sort_strings(strings):
    sorted_strings = sorted(strings, key=lambda x: (-len(x), x[::-1]))
    return sorted_strings


strings = input("Введите слова через пробел: ").split()
sorted_list = sort_strings(strings)
print("Отсортированный список:", sorted_list)
