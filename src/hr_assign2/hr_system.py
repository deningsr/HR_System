import uuid
import csv
import os.path


def add_new_emp(
    first_nane,
    last_name,
    address,
    city,
    state,
    zipcode,
    ssn,
    dob,
    job_title,
    hire_date,
    end_date="N/A",
):
    employees = dict()
    emp_id = str(uuid.uuid4().fields[-1])[:5]
    employees = {
        "ID": emp_id,
        "First Name": first_nane,
        "Last Name": last_name,
        "Address": address,
        "city": city,
        "State": state,
        "Zip": zipcode,
        "SSN": ssn,
        "DOB": dob,
        "Job Title": job_title,
        "Hire Date": hire_date,
        "End Date": end_date,
    }
    file_exists = os.path.isfile("employees.csv")
    with open("employees.csv", "a+", newline="") as file:
        field_names = [emp for emp in employees]
        dict_writer = csv.DictWriter(file, fieldnames=field_names)
        if not file_exists:
            dict_writer.writeheader()
        dict_writer.writerow(employees)


def update_emp(filename, ID):
    with open(filename, newline="") as file:
        readData = [row for row in csv.DictReader(file)]
        # print(readData)
        for row in readData:
            if row["ID"] == ID:
                print(row)


update_emp("employees.csv", "49225")
