import allure
from allure_commons.types import AttachmentType
from django.conf import settings
import os
from pathlib import Path
import django
BASE_DIR = Path(__file__).resolve().parent.parent
from django.test import LiveServerTestCase, TransactionTestCase, TestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from time import sleep
from django.db import transaction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import os
from pathlib import Path
import django
from django.conf import settings
from testData import *
from selenium.webdriver.support.ui import Select


class PatientRegistrationTest(TestCase):

    def setUp(self):
        self.selenium = webdriver.Chrome()
        return super().setUp()


    def testPatientRegister(self):
        selenium = self.selenium
        selenium.get('http://127.0.0.1:5500/frontend/patient-registration.html')
        wait = WebDriverWait(selenium, 10)
        
        # List-data
        data = generate_dummy_data()
        time.sleep(2)
        for i in data :
        # Getting all the fields in the form
            cr_number=selenium.find_element(by=By.NAME , value="cr_number")
            reg_date=selenium.find_element(by=By.NAME , value="reg_date")
            first_name=selenium.find_element(by=By.NAME , value="first_name")
            last_name=selenium.find_element(by=By.NAME , value="last_name")
            p_age=selenium.find_element(by=By.NAME , value="p_age")
            p_gender=Select(selenium.find_element(by=By.NAME , value="p_gender"))
            p_height=selenium.find_element(by=By.NAME , value="p_height")
            p_weight=selenium.find_element(by=By.NAME , value="p_weight")
            phone_number=selenium.find_element(by=By.NAME , value="phone_number")
            p_email=selenium.find_element(by=By.NAME , value="p_email")
            
            p_address=selenium.find_element(by=By.NAME , value="p_address") 
            ecog=Select(selenium.find_element(by=By.NAME , value="ecog") )
            comborbidity=Select(selenium.find_element(by=By.NAME , value="comorbidity"))
            p_id_type=Select(selenium.find_element(by=By.NAME , value="p_id_type") )
            p_id_no=selenium.find_element(by=By.NAME , value="p_id_no")
            relative_name=selenium.find_element(by=By.NAME , value="relative_name") 
            p_relationship=Select(selenium.find_element(by=By.NAME , value="p_relationship") )
            smoking_duration=Select(selenium.find_element(by=By.NAME , value="smoking_duration"))
            tobacco_use=Select(selenium.find_element(by=By.NAME , value="tobacco_use"))
            alcohol_use=Select(selenium.find_element(by=By.NAME , value="alcohol_use"))
            
            notes=selenium.find_element(by=By.NAME, value="notes")
            submit=selenium.find_element(by=By.ID, value="save")
             
            # SENDING DATA TO ALL SELECTED FIELDS
            cr_number.send_keys(i['cr_number'])
            # date and time iss format me aarahi thi datetime.date(2022, 2, 27) and error was--'datetime.date' object is not iterable, 
            # so we used .strftime(---)
            reg_date.send_keys(i['reg_date'])



            first_name.send_keys(i['first_name'])
            last_name.send_keys(i['last_name'])
            p_age.send_keys(i['p_age'])
            p_gender.select_by_visible_text(i['p_gender'])
            p_height.send_keys(i['p_height'])
            p_weight.send_keys(i['p_weight'])
            phone_number.send_keys(i['phone_number'])
            p_email.send_keys(i['p_email'])
            p_address.send_keys(i['p_address'])
            
            ecog.select_by_visible_text(i['ecog'])
            
            comborbidity.select_by_visible_text(i['comborbidity'])
            p_id_type.select_by_visible_text(i['p_id_type'])
            p_id_no.send_keys(i['p_id_no'])
            relative_name.send_keys(i['relative_name'])
            p_relationship.select_by_visible_text(i['p_relationship'])
            smoking_duration.select_by_visible_text(i['smoking_duration'])
            tobacco_use.select_by_visible_text(i['tobacco_use'])
            alcohol_use.select_by_visible_text(i['alcohol_use'])
            notes.send_keys(i['notes'])
        
            submit.send_keys(Keys.RETURN)
            time.sleep(15)
            
        
        selenium.quit()




# py tests.py
# command: py manage.py test


# ---------
# settings.configure(

#     DEBUG=True,
#     INSTALLED_APPS=[
#         'django.contrib.admin',
#         'django.contrib.auth',
#         'django.contrib.contenttypes',
#         'django.contrib.sessions',
#         'django.contrib.messages',
#         'django.contrib.staticfiles',
#         'home',  # Your custom apps
#         'VEG_REC',
#     ],
#     ROOT_URLCONF='core.urls',
#     WSGI_APPLICATION='core.wsgi.application',
#     DATABASES={
#         'default': {
#             'ENGINE': 'django.db.backends.sqlite3',
#             'NAME': BASE_DIR / 'db.sqlite3',
#             # 'NAME': 'testdb.sqlite3',  # Use a separate test database
#         }
#         # 'test': {
#         #                 'ENGINE': 'django.db.backends.sqlite3',
#         #                 'NAME': BASE_DIR / 'testdb.sqlite3'}
#     }
# )
# django.setup()
# applications not registered SOLVED