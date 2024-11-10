class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

        def display_details(self):
            print(f"Employee ID:{self.employee_id}, Name: {self.name}, salary: ${self.salary:}")

            def update_salary(self,new_salary):
                self.salary = new_salary
                print(f"{self.name} salary update to ${self.salary:.2f}.")

                # Define the Department class

                class Department:
                    def __init__(self, department_name):
                        self.department_name = department_name
                        self.Employees = []

                        def add_employee(self, employee):
                            self.employee.append(employee)
                            print(f"Employee '{employee.name}' added to department '{self.department_name}")

                            def total_salary_expenditure(self):
                                total_expenditure = sum(employee.salary for employee in self.Employees)
                                print(f"Total salary expenditure department '{self.department_name}':${total expenditure:.2f}")

                                def display_all_employees(self):
                                    if self.employees:
                                        print(f"Employees in department '{self.department_name}':")
                                        for employee in self.employees:
                                            employee.display_details()

                                    else:
                                                print(f"No employees in department '{self.department_name}'.")

                                                #Interactive program for managing departments and employees

                                                def main():

                                                    # Create a department

                                                    department_name = input("Enter the department name:")
                                                    department = Department(department_name)


                                                    while True:
                                                        print("\nDepartment Management System")
                                                        print("1. Add an Employee")
                                                        print("2. Update an Employee's Salary")
                                                        print("3. Display Total Salary Expenditure")
                                                        print("4. Display All Employees")
                                                        print("5.Exit")

                                                        choice = input("Enter your choice (1-5):")

                                                        if choice == "1":
                                                            #Add a new employee
                                                            name = input("Enter employee's name:")
                                                            employee_id = input("Enter employee's ID:")

                                                            try:
                                                                salary = float(input("Enter employee's salary:"))
                                                                employee = Employee(name, employee_id, salary)
                                                                department.add_employee(employee)
                                                            except ValueError:
                                                                    print("Invalid salary input. Please enter a numeric value.")

                                                        elif choice == "2":
                                                                        #Update an employee"s salary
                                                                        employee_id = input("Enter employees's ID to update salary:")
                                                                        employee = next((e for e in department in department.employees if e.employee_id == employee_id), None)
                                                                        if employee:
                                                                            try:
                                                                                new_salary = float(input("Enter the salary:"))
                                                                                employee.update_salary(new_salary)

                                                                            except ValueError:
                                                                                    print("Invalid salary input. Please enter a numeric value.")

                                                                        else:
                                                                                        print(f"Employee with ID '{employee_id}' not found in department '{department.department_name}'.")

                                                                        elif choice == "3":
                                                                                        # Display total salary expenditure

                                                                                        department.total_salary_expenditures()

                                                                        elif choice == "4":
                                                                                        # Display all employees in the department
                                                                                        department.display_all_employees()

                                                                        elif choice == "5":
                                                                                            # Exit the program
                                                                                            print("Exiting the Department Management System.")

                                                                                            break

                                                                        else:
                                                                                                print("Invalid choice. Please try again.")




 