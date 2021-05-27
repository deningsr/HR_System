import uuid
import csv
import os
import datetime
from tkinter import messagebox
import pandas as pd

menu = "\n".join(
    (
        "Welcome to the HR System!",
        "Please choose from below options (1/2/3/4):",
        "1 - Add a New Employee",
        "2 - Update an Employee Record",
        "3 - See All Current Employed Employees",
        "4 - See Recently Terminated Employees",
        "5 - quit",
        ">>> ",
    )
)


def add_new_emp():
    while True:
        try:
            first_nane = str(input("Enter First Name: "))
        except ValueError:
            print("Please enter a name")
            continue
        else:
            break
    while True:
        try:
            last_name = str(input("Enter Last Name: "))
        except ValueError:
            print("Please enter a name")
            continue
        else:
            break
    while True:
        try:
            address = str(input("Enter Address: "))
        except ValueError:
            print("Please enter an Address")
            continue
        else:
            break
    while True:
        try:
            city = str(input("Enter a City: "))
        except ValueError:
            print("Please enter city")
            continue
        else:
            break
    while True:
        try:
            state = str(input("Enter State Abb: ")).upper()
        except ValueError:
            print("Please enter a State")
            continue
        else:
            break
    while True:
        try:
            zipcode = str(input("Enter zipcode: "))
            if len(zipcode) != 5:
                raise ValueError
        except ValueError:
            print("Please enter a zipcode")
            continue
        else:
            break
    while True:
        try:
            ssn = str(input("Enter SSN: "))
            if len(ssn) != 9:
                raise ValueError
        except ValueError:
            print("Please enter a SSN")
            continue
        else:
            break
    while True:
        try:
            dob = str(input("Enter DOB (MM-DD-YYYY): "))
        except ValueError:
            print("Please enter a date")
            continue
        else:
            break
    while True:
        try:
            job_title = str(input("Enter a Job Title: "))
        except ValueError:
            print("Please enter a title")
            continue
        else:
            break
    while True:
        try:
            hire_date = str(input("Enter Hire Date (MM-DD-YYYY): "))
        except ValueError:
            print("Please enter a date")
            continue
        else:
            break
    while True:
        try:
            end_date = str(input("Enter Termination Date (MM-DD-YYYY): "))
        except ValueError:
            print("Please enter a date")
            continue
        else:
            break
    parsed_hire_date = datetime.datetime.strptime(hire_date, "%m-%d-%Y")
    # parsed_hire_date = datetime.datetime(
    #     year=int(hire_date[6:10]), month=int(hire_date[1]), day=int(hire_date[3:5])
    # )
    parsed_end_date = datetime.datetime.strptime(end_date, "%m-%d-%Y")
    parsed_dob = datetime.datetime.strptime(dob, "%m-%d-%Y")
    employees = dict()
    emp_id = str(uuid.uuid4().fields[-1])[:5]
    employees = {
        "ID": emp_id,
        "First Name": first_nane,
        "Last Name": last_name,
        "Address": address,
        "City": city,
        "State": state,
        "Zip": zipcode,
        "SSN": ssn,
        "DOB": parsed_dob,
        "Job Title": job_title,
        "Hire Date": parsed_hire_date,
        "End Date": parsed_end_date,
    }
    csv_file = "employees.csv"
    file_exists = os.path.isfile(csv_file)
    try:
        with open("employees.csv", "a+", newline="") as file:
            field_names = [emp for emp in employees]
            dict_writer = csv.DictWriter(file, fieldnames=field_names)
            if not file_exists:
                dict_writer.writeheader()
            dict_writer.writerow(employees)
    except IOError:
        print("I/O error")


def update_emp():
    while True:
        try:
            ID = str(input("Enter ID of employee you want to update:"))
        except ValueError:
            print("Please enter an ID")
            continue
        else:
            break
    while True:
        try:
            updated_field = str(input("What field would you like to update?:"))
        except ValueError:
            print("Please enter a valid field")
            continue
        else:
            break
    while True:
        try:
            updated_value = str(input("What is the new value?:"))
        except ValueError:
            print("Please enter a valid value")
            continue
        else:
            break
    # new_dict = pd.read_csv(
    #     "employees.csv", index_col=0, header=None, squeeze=True
    # ).to_dict()
    # print(new_dict)
    csv_file = "employees.csv"
    file_exists = os.path.isfile(csv_file)
    try:
        with open("employees.csv", "r") as file:
            readData = [row for row in csv.DictReader(file)]

        with open("employees.csv", "a") as file:
            dict_writer = csv.DictWriter(
                file,
                fieldnames=[
                    "ID",
                    "First Name",
                    "Last Name",
                    "Address",
                    "City",
                    "State",
                    "Zip",
                    "SSN",
                    "DOB",
                    "Job Title",
                    "Hire Date",
                    "End Date",
                ],
            )
            for row in readData:
                if row["ID"] == ID:
                    row[updated_field] = updated_value
                    print(readData)

                    if not file_exists:
                        dict_writer.writeheader()
                    dict_writer.writerow(row)

    except FileNotFoundError:
        print("file not found")


def create_current_emp_report():
    with open("employees.csv", newline="") as file:
        readData = [row for row in csv.DictReader(file)]

        sorted_list = []
        for row in readData:
            if row["Hire Date"] <= row["End Date"]:
                sorted_list.append(row)
        sortedlist = sorted(sorted_list, key=lambda row: row["ID"], reverse=True)
        print("Currently employed employees:")
        print(
            "{:20} {:>15} {:>20}".format(
                "ID",
                "First Name",
                "Last Name",
            )
        )
        for key in sortedlist:
            print(
                "{:20} {:>15} {:>20}".format(
                    key["ID"], key["First Name"], key["Last Name"]
                )
            )


def send_review_alerts():
    with open("employees.csv", newline="") as file:
        readData = [row for row in csv.DictReader(file)]

        for row in readData:
            past_date = row["Hire Date"] + str(datetime.timedelta(days=-90))
            if row["Hire Date"] >= past_date:
                messagebox.showinfo(
                    "Remember to schedule reviews with the following employees:",
                    row["First Name"],
                )
            else:
                messagebox.showinfo("No upcoming reviews at this time", "Test")


def create_recent_departure_report():
    with open("employees.csv", newline="") as file:
        readData = [row for row in csv.DictReader(file)]
        sorted_list = []
        for row in readData:
            parsed_hire_date = datetime.datetime.strptime(
                row["Hire Date"], "%m-%d-%Y %M:%S"
            )

            past_date = parsed_hire_date + datetime.timedelta(days=-30)

            if row["Hire Date"] >= past_date:
                sorted_list.append(row)
        sortedlist = sorted(sorted_list, key=lambda row: row["ID"], reverse=True)
        print(
            "{:20} {:>15} {:>20}".format(
                "ID",
                "First Name",
                "Last Name",
            )
        )
        for key in sortedlist:
            print(
                "{:20} {:>15} {:>20}".format(
                    key["ID"], key["First Name"], key["Last Name"]
                )
            )


def main():
    # send_review_alerts()
    while True:
        response = input(menu)
        if response == "1":
            add_new_emp()
        if response == "2":
            update_emp()
        if response == "3":
            create_current_emp_report()
        if response == "4":
            create_recent_departure_report()
        if response == "5":
            verify = input("Would you like to quit (yes/no)?")
            if verify == "no":
                continue
            if verify == "yes":
                print("Thank you for visiting!")
            break


if __name__ == "__main__":
    main()
