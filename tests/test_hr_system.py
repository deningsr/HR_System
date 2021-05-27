import hr_assign2.hr_system


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
