employees = {}

while True:
    print("\nEmployee Directory System")
    print("1. Add Employee")
    print("2. Delete Employee")
    print("3. Search Employee")
    print("4. View All Employees")
    print("5. Sort Employees by Name")
    print("6. Filter Employees by Department")
    print("7. Exit")
    
    choice = input("Enter your choice: ").strip()

    if choice == '1':
        # Add Employee
        employee_id = input("Enter employee ID: ").strip()
        name = input("Enter employee name: ").strip()
        department = input("Enter department: ").strip()
        position = input("Enter position: ").strip()
        salary = float(input("Enter salary: ").strip())

        if employee_id in employees:
            print(f"Employee with ID {employee_id} already exists.")
        else:
            employees[employee_id] = {
                "name": name,
                "department": department,
                "position": position,
                "salary": salary
            }
            print(f"Employee {name} added successfully.")

    elif choice == '2':
        # Delete Employee
        employee_id = input("Enter employee ID to delete: ").strip()
        
        if employee_id in employees:
            removed_employee = employees.pop(employee_id)
            print(f"Employee {removed_employee['name']} removed successfully.")
        else:
            print("Employee not found.")

    elif choice == '3':
        # Search Employee
        name = input("Enter employee name to search: ").strip()
        
        found = False
        for employee_id, employee in employees.items():
            if name.lower() in employee['name'].lower():
                print(f"ID: {employee_id}, Name: {employee['name']}, Department: {employee['department']}, Position: {employee['position']}, Salary: ${employee['salary']}")
                found = True
        
        if not found:
            print("No employee found with that name.")

    elif choice == '4':
        # View All Employees
        if not employees:
            print("No employees in the directory.")
        else:
            print("\nEmployee Directory:")
            for employee_id, employee in employees.items():
                print(f"ID: {employee_id}, Name: {employee['name']}, Department: {employee['department']}, Position: {employee['position']}, Salary: ${employee['salary']}")

    elif choice == '5':
        # Sort Employees by Name
        sorted_employees = sorted(employees.items(), key=lambda emp: emp[1]['name'])
        print("\nSorted Employees by Name:")
        for employee_id, employee in sorted_employees:
            print(f"ID: {employee_id}, Name: {employee['name']}, Department: {employee['department']}, Position: {employee['position']}, Salary: ${employee['salary']}")

    elif choice == '6':
        # Filter Employees by Department
        department = input("Enter department to filter: ").strip()
        
        filtered_employees = {emp_id: emp for emp_id, emp in employees.items() if department.lower() in emp['department'].lower()}
        
        if not filtered_employees:
            print("No employees found in that department.")
        else:
            print("\nFiltered Employees by Department:")
            for employee_id, employee in filtered_employees.items():
                print(f"ID: {employee_id}, Name: {employee['name']}, Department: {employee['department']}, Position: {employee['position']}, Salary: ${employee['salary']}")

    elif choice == '7':
        # Exit
        print("Exiting Employee Directory System.")
        break

    else:
        print("Invalid choice. Please try again.")
