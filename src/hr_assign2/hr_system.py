import uuid
import csv
import os.path
import datetime


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
    parsed_hire_date = datetime.datetime(
        year=int(hire_date[6:10]), month=int(hire_date[1]), day=int(hire_date[3:5])
    )
    parsed_end_date = datetime.datetime(
        year=int(end_date[6:10]), month=int(end_date[1]), day=int(end_date[3:5])
    )
    parsed_dob = datetime.datetime(
        year=int(dob[6:10]), month=int(dob[1]), day=int(dob[3:5])
    )
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
        "DOB": parsed_dob,
        "Job Title": job_title,
        "Hire Date": parsed_hire_date,
        "End Date": parsed_end_date,
    }
    file_exists = os.path.isfile("employees.csv")
    with open("employees.csv", "a+", newline="") as file:
        field_names = [emp for emp in employees]
        dict_writer = csv.DictWriter(file, fieldnames=field_names)
        if not file_exists:
            dict_writer.writeheader()
        dict_writer.writerow(employees)


def update_emp(filename, ID, **kwargs):
    with open(filename, newline="") as file:
        readData = [row for row in csv.DictReader(file)]
        # print(readData)
        for row in readData:
            if row["ID"] == ID:
                print("Updating employee ID: " + ID)
                row[kwargs] = kwargs


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
    "05-20-2024",
)

add_new_emp(
    "Will",
    "Smith",
    "123 3rd St",
    "Seattle",
    "WA",
    98115,
    123445678,
    "09-23-1992",
    "Developer",
    "04-21-2021",
    "05-12-2022",
)

add_new_emp(
    "Polly",
    "Moon",
    "123 3rd St",
    "Seattle",
    "WA",
    98115,
    123445678,
    "09-23-1992",
    "Developer",
    "04-21-2021",
    "05-12-2040",
)

add_new_emp(
    "Peter",
    "Griffin",
    "123 3rd St",
    "Seattle",
    "WA",
    98115,
    123445678,
    "09-23-1992",
    "Developer",
    "04-21-2021",
    "05-12-2025",
)
create_current_emp_report()
update_emp("employees.csv", "49225")
