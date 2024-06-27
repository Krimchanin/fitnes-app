from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)


class CalorieCalculator:
    """Класс для работы с калькулятором калорий.

    Реализует функциональности для расчета калорийности продуктов и вывода результатов пользователю.
    Использует заранее заданные данные о калорийности продуктов и обрабатывает пользовательские запросы.
    """

    CALORIES_DATA = {
        'яблоко': 0.52,
        'банан': 0.89,
        'апельсин': 0.47
    }

    @staticmethod
    @app.route('/calorie_calculator', methods=['GET', 'POST'])
    def calorie_calculator():
        """
        Отображает страницу калькулятора калорий и обрабатывает отправленные формы для расчета калорийности.
        При POST-запросе расчитывает калории на основе выбранного продукта или ввода вручную.
        Возвращает шаблон 'calorie_result.html' с результатами расчета калорий.
        """
        if request.method == 'POST':
            method = request.form['method']
            if method == 'select':
                product = request.form['product']
                weight = float(request.form['weight'])
                calories = CalorieCalculator.CALORIES_DATA.get(product, 0) * weight
            elif method == 'manual':
                weight = float(request.form['weight_manual'])
                calorie_per_gram = float(request.form['calorie_per_gram'])
                calories = weight * calorie_per_gram
                product = f'Продукт с калорийностью {calorie_per_gram} ккал/г'
            return render_template('calorie_result.html', product=product, weight=weight, calories=calories)
        products = list(CalorieCalculator.CALORIES_DATA.keys())
        return render_template('calorie_calculator.html', products=products)


class WorkoutLog:
    """Класс для работы с журналом тренировок.

    Реализует функциональности для добавления новых записей тренировок, отображения существующих записей
    и удаления выбранной записи.
    """

    @staticmethod
    @app.route('/workout_log', methods=['GET', 'POST'])
    def workout_log():
        """
        Отображает страницу журнала тренировок и обрабатывает отправленные формы для добавления новых записей.
        При POST-запросе записывает новую тренировку в файл 'workout_log.txt'.
        Возвращает шаблон 'workout_log.html' с существующими записями тренировок.
        """
        if request.method == 'POST':
            date = request.form['date']
            exercise_type = request.form['exercise_type']
            duration = request.form['duration']
            with open('workout_log.txt', 'a') as f:
                f.write(f'{date},{exercise_type},{duration}\n')
            return redirect(url_for('workout_log'))
        with open('workout_log.txt', 'r') as f:
            workouts = [line.strip().split(',') for line in f.readlines()]
        return render_template('workout_log.html', workouts=workouts)

    @staticmethod
    @app.route('/delete_workout/<int:index>')
    def delete_workout(index):
        """
        Удаляет выбранную запись тренировки из файла 'workout_log.txt' на основе переданного индекса.
        Перенаправляет пользователя обратно на страницу журнала тренировок после удаления.
        """
        with open('workout_log.txt', 'r') as f:
            workouts = f.readlines()
        with open('workout_log.txt', 'w') as f:
            for i, line in enumerate(workouts):
                if i != index:
                    f.write(line)
        return redirect(url_for('workout_log'))


class ExercisePlanner:
    """Класс для работы с планировщиком упражнений.

    Реализует функциональности для добавления новых планов упражнений, отображения существующих планов
    и удаления выбранного упражнения.
    """

    @staticmethod
    @app.route('/exercise_planner', methods=['GET', 'POST'])
    def exercise_planner():
        """
        Отображает страницу планировщика упражнений и обрабатывает отправленные формы для добавления новых планов.
        При POST-запросе записывает новый план упражнения в файл 'exercise_planner.txt'.
        Возвращает шаблон 'exercise_planner.html' с существующими планами упражнений.
        """
        if request.method == 'POST':
            day = request.form['day']
            time = request.form['time']
            exercise = request.form['exercise']
            with open('exercise_planner.txt', 'a') as f:
                f.write(f'{day},{time},{exercise}\n')
            return redirect(url_for('exercise_planner'))
        with open('exercise_planner.txt', 'r') as f:
            exercises = [line.strip().split(',') for line in f.readlines()]
        return render_template('exercise_planner.html', exercises=exercises)

    @staticmethod
    @app.route('/delete_exercise/<int:index>')
    def delete_exercise(index):
        """
        Удаляет выбранное упражнение из файла 'exercise_planner.txt' на основе переданного индекса.
        Перенаправляет пользователя обратно на страницу планировщика упражнений после удаления.
        """
        with open('exercise_planner.txt', 'r') as f:
            exercises = f.readlines()
        with open('exercise_planner.txt', 'w') as f:
            for i, line in enumerate(exercises):
                if i != index:
                    f.write(line)
        return redirect(url_for('exercise_planner'))


class BodyMassIndex:
    """Класс для работы с расчетом индекса массы тела (BMI).

    Реализует функциональности для расчета BMI на основе введенных пользователем данных о весе и росте.
    """

    @staticmethod
    @app.route('/bmi', methods=['GET', 'POST'])
    def bmi():
        """
        Отображает страницу калькулятора BMI и обрабатывает отправленные формы для расчета BMI.
        При POST-запросе вычисляет BMI и определяет категорию веса (недостаточный, норма, избыточный, ожирение).
        Возвращает шаблон 'bmi_result.html' с результатами расчета BMI и его категорией.
        """
        if request.method == 'POST':
            weight = float(request.form['weight'])
            height = float(request.form['height'])
            bmi = weight / (height ** 2)
            if bmi < 18.5:
                category = 'Недостаточный вес'
            elif 18.5 <= bmi < 24.9:
                category = 'Норма'
            elif 25 <= bmi < 29.9:
                category = 'Избыточный вес'
            else:
                category = 'Ожирение'
            return render_template('bmi_result.html', bmi=bmi, category=category)
        return render_template('bmi.html')


@app.route('/')
def index():
    """Отображает главную страницу приложения."""
    return render_template('index.html')


if __name__ == '__main__':
    # Проверяем наличие файлов журнала тренировок и планировщика упражнений. Если они не существуют, создаем их.
    log_file = 'workout_log.txt'
    planner_file = 'exercise_planner.txt'

    if not os.path.exists(log_file):
        with open(log_file, 'w'):
            pass

    if not os.path.exists(planner_file):
        with open(planner_file, 'w'):
            pass

    # Запускаем Flask-приложение в режиме отладки.
    app.run(debug=True)
