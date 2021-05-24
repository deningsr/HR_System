import uuid
import csv


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
    with open("employees.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(employees)
        writer.writerow(employees.values())
        # for key, value in employees.items():
        #     writer.writerow([key, value])


add_new_emp(
    "Denin",
    "Grcic",
    "123 3rd St",
    "Seattle",
    "WA",
    98115,
    123445678,
    "09-23-1992",
    "Developer",
    "04-21-2021",
)
