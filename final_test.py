import numpy as np
from PIL import Image

# Функция для обратного RSA шифрования
def rsa_decrypt(ciphertext, d, p, q):
    n = p * q
    plaintext = pow(int(ciphertext), d, n)
    return plaintext

# Вставьте свои параметры
d = 
p = 
q = 

# Считываем матрицы изображения
# Вставьте свои фотографии
remainders = np.array(Image.open('remainders.png'))
integer_parts = np.array(Image.open('integer_parts.png'))

# Восстановление первоначальных чисел из матриц целых частей и остатков
original_numbers_matrix = integer_parts * 256 + remainders

# Дешифрование матрицы первоначальных чисел
decrypted_matrix = np.zeros_like(original_numbers_matrix, dtype=np.uint16)
for i in range(original_numbers_matrix.shape[0]):
    for j in range(original_numbers_matrix.shape[1]):
        decrypted_matrix[i, j] = rsa_decrypt(original_numbers_matrix[i, j], d, p, q)

# Сохраняем дешифрованные числа в файл
with open("decrypted_numbers.txt", "w") as file:
    for row in decrypted_matrix:
        for pixel in row:
            file.write(str(pixel) + " ")
        file.write("\n")

print("Дешифрованные числа сохранены в файл decrypted_numbers.txt")



# Преобразуем матрицу в строку символов согласно заданной кодировке
message = ""
for row in decrypted_matrix:
    for pixel in row:
        if pixel == 32:  # пробел
            message += " "
        elif pixel == 10:  # переход на новую строку
            message += "\n"
        else:
            # Восстанавливаем символы русского алфавита
            if pixel >= 224 and pixel <= 255:
                message += chr(pixel - 224 + ord('а'))
            else:
                # Если символ не известен, можно оставить как есть или обработать по необходимости
                message += "?"

# Сохраняем дешифрованный текст в файл
with open("decrypted_text.txt", "w", encoding="utf-8") as file:
    file.write(message)

print("Перевели числа в буквы в файл decrypted_text.txt")
