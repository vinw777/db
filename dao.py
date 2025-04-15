from employee import Employee
import sqlite3

class EmployeeDAO:
    def __init__(self, db_path):
        self.db_path = db_path
        self.__conn = sqlite3.connect(db_path)
        self.__cursor = self.__conn.cursor()

    def insert(self, emp: Employee):
        query = "INSERT INTO employees (name, position, salary, hire_date) VALUES (?, ?, ?, ?)"
        self.__cursor.execute(query, (emp.get_name(), emp.get_position(), emp.get_salary(), emp.get_hire_date()))
        self.__conn.commit()
        return self.__cursor.lastrowid


    def get_by_id(self, employee_id):
        query = "SELECT * FROM employees WHERE id = ?"
        self.__cursor.execute(query, (employee_id,))
        row = self.__cursor.fetchone()
        if row:
            return Employee(row[1], row[2], row[3], row[4])
        return None

    def get_all(self):
        query = "SELECT * FROM employees"
        self.__cursor.execute(query)
        rows = self.__cursor.fetchall()
        employees = []
        for row in rows:
            employees.append(Employee(row[1], row[2], row[3], row[4]))
        return employees

    def update(self, employee_id, emp: Employee):
        query = "UPDATE employees SET name = ?, position = ?, salary = ?, hire_date = ? WHERE id = ?"
        self.__cursor.execute(query, (emp.get_name(), emp.get_position(), emp.get_salary(), emp.get_hire_date(), employee_id))
        self.__conn.commit()
        return self.__cursor.rowcount

    def delete(self, employee_id):
        query = "DELETE FROM employees WHERE id = ?"
        self.__cursor.execute(query, (employee_id,))
        self.__conn.commit()
        return self.__cursor.rowcount