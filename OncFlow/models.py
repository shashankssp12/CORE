from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class Patient_Data(models.Model):
    cr_number= models.CharField(max_length=50, unique=True)
    reg_date=models.CharField(max_length = 12)
    full_name= models.CharField(max_length=120)
    p_age= models.IntegerField(null=True)
    p_gender=models.CharField(null=True,max_length=200)
    p_height= models.IntegerField(null=True)
    p_weight= models.IntegerField(null=True)
    phone_number = models.CharField(
        max_length=20, 
        # validators=[
        #     RegexValidator(
        #         regex=r'^\+?1?\d{10,13}$',
        #         message="Phone number must be entered in the format: '999999999'."
        #     )
        # ] 
        null=True
    ) 
    p_email= models.EmailField(unique=True,null=True)
    p_address= models.TextField(max_length=200,null=True)
    ecog=models.TextField(null=True)
    comborbidity=models.TextField(null=True)
    p_id_type= models.TextField(null=True)
    p_id_no= models.CharField(unique=True,null=True,max_length=100)
    relative_name= models.CharField(null=True,max_length=200)
    p_relationship= models.CharField(null=True,max_length=200) 
    # Addictions
    smoking_duration= models.CharField(default='UNK',null=True,max_length=200)
    tobacco_use= models.CharField(default='UNK',null=True,max_length=200)
    alcohol_use= models.CharField(default='UNK',null=True,max_length=200)
    notes= models.TextField(null=True)

     #for better formatting in python shell 
    def __str__(self) -> str:
        return self.cr_number
#cr_number
# reg_date
# full_name = first_name + last_name
# p_age
# p_gender
# p_height
# p_weight
# phone_number
# p_email
# p_address
# ecog
# comborbidity
# p_id_type
# p_id_no
# relative_name
# p_relationship
#smoking_duration
# tobacco_use
# alcohol_use
# notes