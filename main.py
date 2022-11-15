# создаем переменные для подсчета правельных ответов и баллов пользователя
number_of_correct_answers = 0
score = 0

#Выводим приветствующее сообщение
welcome_message = print('Привет! Предлагаю проверить свои знания английского!')

#Просим пользователя ввести свое имя
user_name = input("Расскажи, как тебя зовут!")

#Извещение о начале тренировки
print (f"Привет, {user_name}, начинаем тренировку!")

#Первый вопрос
the_first_question = "My name ___ Vova."
the_first_correct_answer = "is"
print(the_first_question)

#Переменная, которая хранит ответ пользователя на первый вопрос
the_first_answer = input("Какое слово пропущено?")

#Сравниваем ответ пользователя с правельным ответом
if the_first_answer == the_first_correct_answer:
    print("Ответ верный!\nВы получаете 10 баллов!")
    number_of_correct_answers += 1
    score += 10
else:
    print(f"Неправильно.\nПравильный ответ: {the_first_correct_answer}")

#Второй вопрос
the_second_question = "I ___ a coder."
the_second_correct_answer = "am"
print(the_second_question)

#Переменная, которая хранит ответ пользователя на второй вопрос
the_second_answer = input("Какое слово пропущено?")

#Сравниваем ответ пользователя с правельным ответом
if the_second_answer == the_second_correct_answer:
    print("Ответ верный!\nВы получаете 10 баллов!")
    number_of_correct_answers += 1
    score += 10
else:
    print(f"Неправильно.\nПравильный ответ: {the_second_correct_answer}")

#Третий вопрос
the_third_question = "I live ___ Moscow."
the_third_correct_answer = "in"
print(the_third_question)

#Переменная, которая хранит ответ пользователя на третий вопрос
the_third_answer = input("Какое слово пропущено?")

#Сравниваем ответ пользователя с правельным ответом
if the_third_answer == the_third_correct_answer:
    print("Ответ верный!\nВы получаете 10 баллов!")
    number_of_correct_answers += 1
    score += 10
else:
    print(f"Неправильно.\nПравильный ответ: {the_third_correct_answer}")

# Считаем колличество правельных ответов в процентах
percentage_of_correct_answers = int(100/3 * number_of_correct_answers)

# Выводим итоговое сообщения прохождения теста
print(f"Вот и все, {user_name}!\nВы ответили на {number_of_correct_answers} вопросов из 3 верно.\nВы заработали {score} баллов.\nЭто {percentage_of_correct_answers} процентов." )
