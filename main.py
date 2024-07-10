#task1
# def factorial(n):
#     if n < 0:
#         raise ValueError("Факторіал не визначено для від'ємних чисел.")
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# def main():
#     try:
#         number = int(input("Введіть число: "))
#         result = factorial(number)
#         print(f"Факторіал числа {number} дорівнює {result}.")
#     except ValueError as e:
#         print(f"Помилка: {e}")

# if __name__ == "__main__":
#     main()
#task2
# def factorial(n):
#     if n < 0:
#         raise ValueError("Факторіал не визначено для від'ємних чисел.")
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# def main():
#     try:
#         number = int(input("Введіть число: "))
#         result = factorial(number)
#         print(f"Факторіал числа {number} дорівнює {result}.")
#     except ValueError as e:
#         print(f"Помилка: {e}")

# if __name__ == "__main__":
#     main()
# def factorial(n):
#     try:
#         if n < 0:
#             raise ValueError("Факторіал не визначено для від'ємних чисел.")
#         result = 1
#         for i in range(1, n + 1):
#             result *= i
#         return result
#     except ValueError as e:
#         return f"Помилка: {e}"

# def main():
#     try:
#         number = int(input("Введіть число: "))
#     except ValueError:
#         print("Помилка: введене значення повинно бути цілим числом.")
#         return
    
#     result = factorial(number)
#     print(result if isinstance(result, str) else f"Факторіал числа {number} дорівнює {result}.")

# if __name__ == "__main__":
#     main()

#task3
# def display_menu():
#     print("\nМеню:")
#     print("1. Відображення списку")
#     print("2. Отримання максимального значення у списку")
#     print("3. Отримання мінімального значення у списку")
#     print("4. Відображення значення елемента за індексом")
#     print("5. Видалення елемента за індексом")
#     print("6. Вихід")

# def display_list(numbers):
#     print("Список чисел:", numbers)

# def get_max_value(numbers):
#     return max(numbers)

# def get_min_value(numbers):
#     return min(numbers)

# def get_element_by_index(numbers, index):
#     return numbers[index]

# def delete_element_by_index(numbers, index):
#     del numbers[index]

# def main():
#     numbers = []

#     while True:
#         user_input = input("Введіть число (або 'stop' для завершення): ")
#         if user_input.lower() == 'stop':
#             break
#         try:
#             number = float(user_input)
#             numbers.append(number)
#         except ValueError:
#             print("Помилка: введіть коректне число.")

#     while True:
#         display_menu()
#         choice = input("Виберіть опцію: ")

#         if choice == '1':
#             display_list(numbers)
#         elif choice == '2':
#             if numbers:
#                 print("Максимальне значення у списку:", get_max_value(numbers))
#             else:
#                 print("Список порожній.")
#         elif choice == '3':
#             if numbers:
#                 print("Мінімальне значення у списку:", get_min_value(numbers))
#             else:
#                 print("Список порожній.")
#         elif choice == '4':
#             if numbers:
#                 try:
#                     index = int(input("Введіть індекс: "))
#                     print("Значення за індексом", index, ":", get_element_by_index(numbers, index))
#                 except (ValueError, IndexError):
#                     print("Помилка: неправильний індекс.")
#             else:
#                 print("Список порожній.")
#         elif choice == '5':
#             if numbers:
#                 try:
#                     index = int(input("Введіть індекс: "))
#                     delete_element_by_index(numbers, index)
#                     print("Елемент за індексом", index, "успішно видалений.")
#                 except (ValueError, IndexError):
#                     print("Помилка: неправильний індекс.")
#             else:
#                 print("Список порожній.")
#         elif choice == '6':
#             print("Вихід з програми.")
#             break
#         else:
#             print("Невірний вибір. Спробуйте ще раз.")

# if __name__ == "__main__":
#     main()

#task4
# def display_list(numbers):
#     print("Список чисел:", numbers)

# def get_max_value(numbers):
#     return max(numbers)

# def get_min_value(numbers):
#     return min(numbers)

# def get_element_by_index(numbers, index):
#     return numbers[index]

# def delete_element_by_index(numbers, index):
#     del numbers[index]

# def main():
#     numbers = []


#     while True:
#         user_input = input("Введіть число (або 'stop' для завершення): ")
#         if user_input.lower() == 'stop':
#             break
#         try:
#             number = float(user_input)
#             numbers.append(number)
#         except ValueError:
#             print("Помилка: введіть коректне число.")

#     while True:
#         print("\nМеню:")
#         print("1. Відображення списку")
#         print("2. Отримання максимального значення у списку")
#         print("3. Отримання мінімального значення у списку")
#         print("4. Відображення значення елемента за індексом")
#         print("5. Видалення елемента за індексом")
#         print("6. Вихід")

#         choice = input("Виберіть опцію: ")

#         if choice == '1':
#             display_list(numbers)
#         elif choice == '2':
#             if numbers:
#                 print("Максимальне значення у списку:", get_max_value(numbers))
#             else:
#                 print("Список порожній.")
#         elif choice == '3':
#             if numbers:
#                 print("Мінімальне значення у списку:", get_min_value(numbers))
#             else:
#                 print("Список порожній.")
#         elif choice == '4':
#             if numbers:
#                 try:
#                     index = int(input("Введіть індекс: "))
#                     print("Значення за індексом", index, ":", get_element_by_index(numbers, index))
#                 except (ValueError, IndexError):
#                     print("Помилка: неправильний індекс.")
#             else:
#                 print("Список порожній.")
#         elif choice == '5':
#             if numbers:
#                 try:
#                     index = int(input("Введіть індекс: "))
#                     delete_element_by_index(numbers, index)
#                     print("Елемент за індексом", index, "успішно видалений.")
#                 except (ValueError, IndexError):
#                     print("Помилка: неправильний індекс.")
#             else:
#                 print("Список порожній.")
#         elif choice == '6':
#             print("Вихід з програми.")
#             break
#         else:
#             print("Невірний вибір. Спробуйте ще раз.")

# if __name__ == "__main__":
#     main()

# def display_list(numbers):
#     print("Список чисел:", numbers)

# def get_max_value(numbers):
#     try:
#         return max(numbers)
#     except ValueError:
#         return "Помилка: Список порожній."

# def get_min_value(numbers):
#     try:
#         return min(numbers)
#     except ValueError:
#         return "Помилка: Список порожній."

# def get_element_by_index(numbers, index):
#     try:
#         return numbers[index]
#     except IndexError:
#         return "Помилка: неправильний індекс."

# def delete_element_by_index(numbers, index):
#     try:
#         del numbers[index]
#         return f"Елемент за індексом {index} успішно видалений."
#     except IndexError:
#         return "Помилка: неправильний індекс."

# def main():
#     numbers = []


#     while True:
#         user_input = input("Введіть число (або 'stop' для завершення): ")
#         if user_input.lower() == 'stop':
#             break
#         try:
#             number = float(user_input)
#             numbers.append(number)
#         except ValueError:
#             print("Помилка: введіть коректне число.")

#     while True:
#         print("\nМеню:")
#         print("1. Відображення списку")
#         print("2. Отримання максимального значення у списку")
#         print("3. Отримання мінімального значення у списку")
#         print("4. Відображення значення елемента за індексом")
#         print("5. Видалення елемента за індексом")
#         print("6. Вихід")

#         choice = input("Виберіть опцію: ")

#         if choice == '1':
#             display_list(numbers)
#         elif choice == '2':
#             print("Максимальне значення у списку:", get_max_value(numbers))
#         elif choice == '3':
#             print("Мінімальне значення у списку:", get_min_value(numbers))
#         elif choice == '4':
#             if numbers:
#                 index = int(input("Введіть індекс: "))
#                 print("Значення за індексом", index, ":", get_element_by_index(numbers, index))
#             else:
#                 print("Список порожній.")
#         elif choice == '5':
#             if numbers:
#                 index = int(input("Введіть індекс: "))
#                 print(delete_element_by_index(numbers, index))
#             else:
#                 print("Список порожній.")
#         elif choice == '6':
#             print("Вихід з програми.")
#             break
#         else:
#             print("Невірний вибір. Спробуйте ще раз.")

# if __name__ == "__main__":
#     main()
