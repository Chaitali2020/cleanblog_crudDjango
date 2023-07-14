from django.db import models
from datetime import datetime,date
from django import forms
from django.core.exceptions import ValidationError

# Create your models here.
def validate_date_format(value):
    try:
        # Attempt to parse the date using the desired format
        datetime.datetime.strptime(value, '%Y-%m-%d')
    except ValueError:
        # If the date format is invalid, raise a validation error
        raise ValidationError('Date must be in the format YYYY-MM-DD.')
    
class blog_model(models.Model):
    bhead=models.CharField(max_length=50)
    bcat=models.CharField(max_length=50)
    bdesc=models.TextField()
    bname=models.CharField(max_length=50)
    bdate=models.DateField(validators=[validate_date_format])
    