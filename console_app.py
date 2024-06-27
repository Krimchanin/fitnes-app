import os
from datetime import datetime

class WorkoutLog:
    """
    Класс для работы с журналом тренировок.

    Реализует функциональности для добавления новых записей тренировок, отображения существующих записей
    и удаления выбранной записи.
    """

    LOG_FILE = 'workout_log.txt'

    @staticmethod
    def add_workout():
        """
        Добавляет новую запись тренировки в журнал.

        Пользователю предлагается ввести тип упражнения и продолжительность тренировки в минутах.
        Продолжительность переводится в часы и минуты. Запись сохраняется в файл 'workout_log.txt'.
        """
        date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        exercise_type = input("Введите тип упражнения: ")
        duration_minutes = int(input("Введите продолжительность тренировки в минутах: "))
        duration_hours = duration_minutes // 60
        duration_minutes = duration_minutes % 60

        with open(WorkoutLog.LOG_FILE, 'a') as f:
            f.write(f'{date},{exercise_type},{duration_hours} часов {duration_minutes} минут\n')

        print("Тренировка успешно добавлена.")

    @staticmethod
    def show_workouts():
        """
        Отображает все существующие записи тренировок из файла 'workout_log.txt'.

        Если файл существует и содержит записи, выводит их на экран. В противном случае выводит сообщение о отсутствии записей.
        """
        if os.path.exists(WorkoutLog.LOG_FILE):
            with open(WorkoutLog.LOG_FILE, 'r') as f:
                workouts = f.readlines()
            if workouts:
                print("Существующие тренировки:")
                for index, workout in enumerate(workouts):
                    print(f"{index + 1}. {workout.strip()}")
            else:
                print("Нет сохраненных тренировок.")
        else:
            print("Нет сохраненных тренировок.")

    @staticmethod
    def delete_workout():
        """
        Удаляет выбранную запись тренировки из файла 'workout_log.txt'.

        Пользователю предоставляется список существующих тренировок с номерами. После выбора номера
        удаляет соответствующую запись из файла.
        """
        WorkoutLog.show_workouts()
        if os.path.exists(WorkoutLog.LOG_FILE):
            index_to_delete = int(input("Введите номер тренировки для удаления: ")) - 1

            with open(WorkoutLog.LOG_FILE, 'r') as f:
                workouts = f.readlines()

            with open(WorkoutLog.LOG_FILE, 'w') as f:
                for i, line in enumerate(workouts):
                    if i != index_to_delete:
                        f.write(line)

            print("Тренировка успешно удалена.")
        else:
            print("Нет сохраненных тренировок.")

class CalorieCalculator:
    """
    Класс для работы с калькулятором калорий.

    Реализует функциональности для расчета калорийности продуктов и вывода результатов пользователю.
    Использует заранее заданные данные о калорийности продуктов и обрабатывает пользовательские запросы.
    """

    CALORIES_DATA = {
        '1': ('яблоко', 0.52),
        '2': ('банан', 0.89),
        '3': ('апельсин', 0.47)
    }

    @staticmethod
    def calculate_calories():
        """
        Рассчитывает калории для выбранного продукта.

        Пользователю предоставляется список продуктов с номерами для выбора. Затем запрашивается вес
        продукта в граммах. После ввода производит расчет калорий и выводит результат на экран.
        """
        print("Выберите продукт для расчета калорий:")
        for key, (product, calorie_per_gram) in CalorieCalculator.CALORIES_DATA.items():
            print(f"{key}. {product} ({calorie_per_gram} ккал/г)")

        choice = input("Введите номер продукта: ")

        if choice in CalorieCalculator.CALORIES_DATA:
            product, calorie_per_gram = CalorieCalculator.CALORIES_DATA[choice]
            weight = float(input("Введите вес продукта в граммах: "))
            calories = calorie_per_gram * weight
            print(f"Продукт: {product}")
            print(f"Вес: {weight} г")
            print(f"Калории: {calories} ккал")
        else:
            print("Некорректный выбор продукта.")

class BodyMassIndex:
    """
    Класс для работы с расчетом индекса массы тела (BMI).

    Реализует функциональности для расчета BMI на основе введенных пользователем данных о весе и росте.
    """

    @staticmethod
    def calculate_bmi():
        """
        Рассчитывает BMI и определяет категорию веса.

        Пользователю предоставляется ввести свой вес в килограммах и рост в метрах. После ввода
        производит расчет BMI и выводит результаты на экран, включая категорию веса.
        """
        weight = float(input("Введите ваш вес в килограммах: "))
        height = float(input("Введите ваш рост в метрах: "))

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = 'Недостаточный вес'
        elif 18.5 <= bmi < 24.9:
            category = 'Норма'
        elif 25 <= bmi < 29.9:
            category = 'Избыточный вес'
        else:
            category = 'Ожирение'

        print(f"Ваш BMI: {bmi:.2f}")
        print(f"Категория веса: {category}")

class Application:
    """
    Основной класс приложения для управления функциональностью.

    Предоставляет интерфейс командной строки для выбора действий пользователя: калькулятор калорий,
    журнал тренировок, планировщик упражнений, калькулятор BMI и выход из программы.
    """

    def run(self):
        """
        Запускает основной цикл приложения.

        Выводит меню выбора действий, запрашивает у пользователя выбор и вызывает соответствующие методы классов.
        """
        while True:
            print("\nВыберите действие:")
            print("1. Калькулятор калорий")
            print("2. Журнал тренировок")
            print("3. Планировщик упражнений")
            print("4. Калькулятор BMI")
            print("5. Выйти из программы")

            choice = input("Введите номер действия: ")

            if choice == '1':
                CalorieCalculator.calculate_calories()
            elif choice == '2':
                print("\n1. Добавить тренировку")
                print("2. Удалить тренировку")
                print("3. Показать все тренировки")
                sub_choice = input("Введите номер действия: ")
                if sub_choice == '1':
                    WorkoutLog.add_workout()
                elif sub_choice == '2':
                    WorkoutLog.delete_workout()
                elif sub_choice == '3':
                    WorkoutLog.show_workouts()
                else:
                    print("Некорректный ввод. Попробуйте снова.")
            elif choice == '3':
                print("\nПланировщик упражнений в разработке.")
                # Добавить функциональность планировщика упражнений
            elif choice == '4':
                BodyMassIndex.calculate_bmi()
            elif choice == '5':
                print("Программа завершена.")
                break
            else:
                print("Некорректный ввод. Попробуйте снова.")

if __name__ == '__main__':
    # Запуск приложения
    app = Application()
    app.run()
