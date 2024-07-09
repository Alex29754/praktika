def process_text_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()

    # Подсчет количества строк
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    num_lines = len(lines)

    # Подсчет количества символов
    num_chars = len(text)

    # Подсчет количества слов
    words = text.lower().split()
    num_words = len(words)

    # Удаление пунктуации и подсчет частоты встречаемости слов
    word_counts = {}
    for word in words:
        cleaned_word = ''.join(char for char in word if char.isalnum())
        if cleaned_word:
            if cleaned_word in word_counts:
                word_counts[cleaned_word] += 1
            else:
                word_counts[cleaned_word] = 1

    # Находим 10 наиболее частых слов
    common_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:10]

    # Вывод результатов
    print(f"Имя файла: {file_name}")
    print(f"Количество строк: {num_lines}")
    print(f"Количество слов: {num_words}")
    print(f"Количество символов: {num_chars}")
    print(f"10 наиболее частых слов: {[word for word, count in common_words]}")

if True:
    file_name = input("Введите имя файла: ")
    process_text_file(file_name)
