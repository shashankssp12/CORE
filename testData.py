import random
import faker
import datetime

faker = faker.Faker('en_IN')

def generate_random_date():
    # Generate a random year between 1900 and 2100
    year = random.randint(1900, 2100)
    # Generate a random month between 1 and 12
    month = random.randint(1, 12)
    # Generate a random day between 1 and the maximum number of days in the selected month and year
    max_day = min(28, datetime.date(year, month, 1).replace(day=28).day)
    day = random.randint(1, max_day)
    # Return the date in the "YYYY-MM-DD" format
    return f"{year:04d}-{month:02d}-{day:02d}"

def generate_dummy_data():
    dummy_data = []
    for _ in range(10):
        
        data = {
            "cr_number": faker.random_number(digits=6),
            "reg_date": generate_random_date(),
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "p_age": random.randint(18, 90),
            "p_gender": random.choice(["Male", "Female"]),
            "p_height": random.randint(150, 200),
            "p_weight": random.randint(50, 100),
            "phone_number": faker.phone_number(),
            "p_email": faker.email(),
            "p_address": faker.address(),
            "ecog": random.choice([
                                        "PS 0: Fully active, able to carry on all pre-disease performance without restriction",
                                         "PS 1: Restricted in physically strenuous activity but ambulatory and able to carry out work of a light or sedentary nature, e.g., light house work, office work",
                                         "PS 2: Ambulatory and capable of all selfcare but unable to carry out any work activities; up and about more than 50% of waking hours",
                                         "PS 3: Capable of only limited selfcare; confined to bed or chair more than 50% of waking hours",
                                         "PS 4: Completely disabled; cannot carry on any selfcare; totally confined to bed or chair",
                                        "PS 5: Dead"]),
            
            "comborbidity": random.choice([
                "No Comorbidity",
                "Tuberculosis of lung",
                "Tuberculosis of intrathoracic lymph nodes",
                "Tuberculosis of larynx, trachea and bronchus",
                "Tuberculous pleurisy",]),
            
            "p_id_type": random.choice(["Aadhar", "PAN", "Passport","Voter ID","Citizenship No","Other"]),
            "p_id_no": faker.random_number(digits=8),
            "relative_name": faker.name(),
            
            "p_relationship": random.choice(["Mother","Father","Wife","Husband","Other"]),
            
            "smoking_duration": random.choice(["No", "Yes"]),
            "tobacco_use": random.choice(["Yes", "No"]),
            "alcohol_use": random.choice(["Yes", "No"]),
            "notes": faker.text()
        }
        dummy_data.append(data)
    return dummy_data


if __name__== "__main__":
    pass
# dummy_patient_data = generate_dummy_data()
# for data in dummy_patient_data:
#     print(data)
