from dao import EmployeeDAO
from employee import Employee

dao = EmployeeDAO("/Users/madinagabbazova/python/employee_database/employee_db.sqlite")
emp1 = Employee(name="Madina Gabbazova", position="Software Engineer", salary=85000, hire_date="2025-04-01")
emp2 = Employee(name="Ayana Osmonalieva", position="Data Analyst", salary=65000, hire_date="2025-03-15")
emp3 = Employee(name="Kirill Donetskov", position="Product Manager", salary=95000, hire_date="2025-02-20")
emp4 = Employee(name="Argen Samoilov", position="UX Designer", salary=72000, hire_date="2025-01-10")

# Inserting 
dao.insert(emp1)
dao.insert(emp2)
dao.insert(emp3)
dao.insert(emp4)

# Retrieving by id
print(dao.get_by_id(2))

print("-----------------------------------")

# Retrieving all employees
emps = dao.get_all()
for emp in emps:
    print(emp)

# Updating 
upd_emp = Employee(name="Nurai Baktybekova", position="Senior Software Engineer", salary=95000, hire_date="2025-04-01")
dao.update(4, upd_emp)

# Deleting
dao.delete(4)