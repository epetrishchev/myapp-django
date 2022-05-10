

from datetime import date


def get_count_weeks_year(date: date):
    """
    Функция для получения номера недели в текущем году от начала года до даты полученной функцией в качестве аргумента. Аргумент '%U' метода strftime указывает, что начало недели - воскресенье.
    Args:
        date (object): Объект класса date модуля datetime
    Returns:
        int: номер недели
    """
    return int(date.strftime('%U')) + 1


def get_total_count_weeks_year(year: int):
    """
    Функция для получения количества недель в году. Аргумент '%U' метода strftime указывает, что начало недели - воскресенье.
    Args:
        year (int): год в формате yyyy
    Returns:
        int: количество недель
    """
    return int(date(year, 12, 31).strftime('%U')) + 1


def get_total_count_weeks(user_date: date, start_date: date):
    """
    Функция для получения номера недели за период от START до date
    Args:
        date (object): Объект класса date модуля datetime
    Returns:
        int: номер недели
    """
    # определяем период за который нам необходимо получить номер недели
    period = user_date.year - start_date.year
    # формируем список в котором каждый элемент это количество недель в году. Количество элементов зависит от количества полных лет в периоде.
    total_weeks = [get_total_count_weeks_year(
        start_date.year + i) for i in range(period)]
    # добавляем в список номер недели от начала года до date
    total_weeks.append(get_count_weeks_year(user_date))
    return sum(total_weeks)
