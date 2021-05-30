import hr_assign2.hr_system
import datetime


# def test_add_new_emp():
#     emp_id = 12345
#     hr_assign2.hr_system.add_new_emp()
#     assert employees[emp_id]["First Name"] == "Denin"
#     assert employees[emp_id]["Last Name"] == "Grcic"


def test_generate_unique_id():
    assert (
        hr_assign2.hr_system.generate_unique_id()
        != hr_assign2.hr_system.generate_unique_id()
        != hr_assign2.hr_system.generate_unique_id()
    )


def test_sort_reports():
    readData = [
        {"ID": "5000", "Name": "John"},
        {"ID": "4500", "Name": "Steve"},
        {"ID": "7000", "Name": "Judy"},
    ]

    assert hr_assign2.hr_system.sort_reports(readData) == [
        {"ID": "7000", "Name": "Judy"},
        {"ID": "5000", "Name": "John"},
        {"ID": "4500", "Name": "Steve"},
    ]


def test_update_row():
    readData = [
        {"ID": "5000", "Name": "John"},
        {"ID": "4500", "Name": "Steve"},
        {"ID": "7000", "Name": "Judy"},
    ]
    assert hr_assign2.hr_system.update_row(readData, "5000", "Name", "Henry") == [
        {"ID": "5000", "Name": "Henry"},
        {"ID": "4500", "Name": "Steve"},
        {"ID": "7000", "Name": "Judy"},
    ]


def test_list_current_employees():
    readData = [
        {"ID": "5000", "Name": "John", "End Date": "2025-01-01 00:00:00"},
        {"ID": "4500", "Name": "Steve", "End Date": "2022-01-20 00:00:00"},
        {"ID": "7000", "Name": "Judy", "End Date": "2015-02-11 00:00:00"},
    ]
    assert hr_assign2.hr_system.list_current_employees(readData) == [
        {"ID": "5000", "Name": "John", "End Date": "2025-01-01 00:00:00"},
        {"ID": "4500", "Name": "Steve", "End Date": "2022-01-20 00:00:00"},
    ]
