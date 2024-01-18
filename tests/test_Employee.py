from unittest import TestCase

from tasks.Employee import Employee


class TestEmployee(TestCase):
    def test_calculate_emp_salary(self):
        employee: Employee = Employee(1, "Coach", "Facilitators")
        self.assertEqual(90, employee.calculate_emp_salary(9))

    def test_employee_assigned_department(self):
        employee: Employee = Employee(1, "Coach", "Facilitators")
        self.assertEqual("Facilitators", employee.emp_assign_department())

    def test_employee_details(self):
        employee: Employee = Employee(1, "Coach", "Facilitators")
        result = f"""
        id = 1
        name = 'Coach'
        department = 'Facilitators'
        """
        self.assertEqual(result, employee.print_employee_details())
