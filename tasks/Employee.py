class Employee:

    def __init__(self, emp_id: int, emp_name: str, emp_department: str):
        self.__emp_id = emp_id
        self.__emp_name = emp_name
        self.__emp_department = emp_department
        self.__hourly_rate = 10

    def calculate_emp_salary(self, number_of_hours_worked):
        return number_of_hours_worked * self.__hourly_rate

    def emp_assign_department(self):
        return self.__emp_department

    def print_employee_details(self):
        return f"""
        id: {self.__emp_id}
        name: {self.__emp_name}
        department: {self.__emp_department}    
        """
