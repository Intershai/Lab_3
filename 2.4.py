import random


# Функция для случайного перемешивания фрагментов текста
def shuffle_text(text, num_shuffles=5):
    # Разбиваем текст на фрагменты (например, по предложениям или словам)
    fragments = text.split()

    # Выполняем несколько повторных перемешиваний
    for _ in range(num_shuffles):
        random.shuffle(fragments)

    # Собираем перемешанные фрагменты обратно в строку
    shuffled_text = ' '.join(fragments)
    return shuffled_text


# Пример исходного текста
original_text = """
    «Что вершит судьбу человечества в этом мире? 
    Некое незримое существо или закон, 
    подобно длани господней, парящей над миром? 
    По крайней мере, истинно то, 
    что человек не властен даже над своей волей».
"""

# Перемешиваем текст
shuffled_text = shuffle_text(original_text, num_shuffles=10)

# Выводим результаты
print("Исходный текст:")
print(original_text)
print("\nПеремешанный текст:")
print(shuffled_text)