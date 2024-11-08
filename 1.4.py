def gronsfeld_cipher(message, key):
    # Определяем алфавит
    alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    # Подготавливаем сообщение и ключ
    message = message.replace(" ", "").upper()
    key = [int(digit) for digit in str(key)]
    key_len = len(key)

    # Шифруем сообщение
    encrypted_message = ""
    for i, char in enumerate(message):
        if char in alphabet:
            # Позиция буквы в алфавите
            pos = alphabet.index(char)
            # Цифра из ключа
            shift = key[i % key_len]
            # Новая позиция с учетом сдвига
            new_pos = (pos + shift) % len(alphabet)
            encrypted_message += alphabet[new_pos]
        else:
            # Оставляем символ без изменений, если он не в алфавите
            encrypted_message += char

    return encrypted_message

def gronsfeld_decrypt(encrypted_message, key):
    # Определяем алфавит
    alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

    # Подготавливаем зашифрованное сообщение и ключ
    encrypted_message = encrypted_message.replace(" ", "").upper()
    key = [int(digit) for digit in str(key)]
    key_len = len(key)

    # Дешифруем сообщение
    decrypted_message = ""
    for i, char in enumerate(encrypted_message):
        if char in alphabet:
            # Позиция буквы в алфавите
            pos = alphabet.index(char)
            # Цифра из ключа
            shift = key[i % key_len]
            # Новая позиция с учетом обратного сдвига
            new_pos = (pos - shift) % len(alphabet)
            decrypted_message += alphabet[new_pos]
        else:
            # Оставляем символ без изменений, если он не в алфавите
            decrypted_message += char

    return decrypted_message

# Пример использования
message = "СОВЕРШЕННО СЕКРЕТНО"
key = 314

# Шифрование
encrypted_message = gronsfeld_cipher(message, key)
print(f"Зашифрованное сообщение: {encrypted_message}")

# Дешифрование
decrypted_message = gronsfeld_decrypt(encrypted_message, key)
print(f"Дешифрованное сообщение: {decrypted_message}")
