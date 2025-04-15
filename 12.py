class InvalidRollException(Exception):
    pass

def fee(base_fee, roll_number):
    if len(roll_number) != 7:
        raise InvalidRollException("Roll number must be 7 characters long.")
    
    dept = roll_number[:2]
    year_part = roll_number[2:4]
    program = roll_number[4]
    branch_number = roll_number[5:]

    valid_departments = {'DS', 'CS', 'EE', 'ME'}
    valid_programs = {'1', '2'}
    
    if dept not in valid_departments:
        raise InvalidRollException("Invalid department code.")
    if not year_part.isdigit():
        raise InvalidRollException("Invalid year part.")
    if program not in valid_programs:
        raise InvalidRollException("Invalid program code.")
    if not branch_number.isdigit():
        raise InvalidRollException("Invalid branch number.")
    
    admission_year = 2000 + int(year_part)
    duration = 4 if program == '1' else 2
    last_year = 2022
    end_year = admission_year + duration - 1

    if end_year < 2018:
        raise InvalidRollException("Course ended before 2018.")

    academic_years = min(end_year, last_year) - admission_year + 1

    total_fee = 0
    current_fee = base_fee

    for _ in range(academic_years):
        total_fee += int(current_fee)
        current_fee *= 1.1

    return int(total_fee)

def print_fee(base_fee, roll_number):
    try:
        print(fee(base_fee, roll_number))
    except InvalidRollException:
        print("InvalidRollException")

# ✅ Test calls
print_fee(100000, 'CS20143')   # 331000
print_fee(100000, 'DS18243')   # 210000
print_fee(100000, 'EE16243')   # Invalid
