from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime



if __name__ == '__main__':
    current_datetime = datetime.now()
    print(current_datetime)
    calculate_salary()
    get_employees()