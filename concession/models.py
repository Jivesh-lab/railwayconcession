from django.db import models
from django.contrib.auth.hashers import make_password, check_password

#SignUp Model
class SignForm(models.Model):
    login_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    # def set_password(self, raw_password):
    #     """Hashes the password before saving it."""
    #     self.password = make_password(raw_password)

    # def check_password(self, raw_password):
    #     """Verifies the password against the stored hash."""
    #     return check_password(raw_password, self.password) # type: ignore
    
    
#Candidate details Model
class details(models.Model):
    concession_id = models.AutoField(primary_key=True)  
    studentname = models.CharField(max_length=255)
    collegename = models.CharField(max_length=255)
    station1 = models.CharField(max_length=100)
    station2 = models.CharField(max_length=100)
    travel_class = models.CharField(max_length=50)
    validity=models.IntegerField(choices=[(1, "1 Month"), (3, "3 Months")])
    current_date = models.DateField()  # Ensure it stores as DateField
    valid_till_date = models.DateField() 
    login_id = models.ForeignKey(SignForm, on_delete=models.CASCADE)