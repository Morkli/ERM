from django.db import models
from django.utils import timezone
from django.core.validators import validate_email
import string
import random

mem_id = 0


def id_no(size=7, chars=string.digits):
    nums = ''.join(random.choice(chars) for _ in range(size))
    asd = "ASD"
    return asd + nums


class Members(models.Model):
    gender_choices = (('Male', 'Male'), ('Female', 'Female'),)
    reg_choices = (('Y', 'Yes'), ('N', 'No'),)
    dues_choices = (('Paid', 'Paid'), ('UnPaid', 'Unpaid'),)
    operation_choices = (
            ('Importer', 'Importer'),
            ('ImportRtl', 'Importer & Retailer'),
            ('Retailer', 'Retailer'),
            ('Wholesaler', 'Wholesaler'),
        )
    marital_choices = (('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'),)

    region_choices = (
        ('GR', 'Greater Accra'),
        ('ER', 'Eastern'),
        ('CR', 'Central'),
        ('WR', 'Western'),
        ('AR', 'Ashanti'),
        ('VR', 'Volta'),
        ('OT', 'Oti'),
        ('NR', 'Northern'),
        ('SR', 'Savannah'),
        ('NE', 'North East'),
        ('UE', 'Upper East'),
        ('UW', 'Upper West'),
        ('WN', 'Western North'),
        ('BA', 'Brong Ahafo'),
        ('BE', 'Bono East'),
        ('AF', 'Ahafo'),

    )
    Image = models.ImageField(blank=True, null=True, upload_to="images/")
    Full_name = models.CharField(blank=True, null=True, max_length=100)
    Date_of_Birth = models.DateField(blank=True, null=True)
    Gender = models.CharField(null=True, max_length=10, choices=gender_choices)
    Marital_Status = models.CharField(blank=True, null=True, max_length=10, choices=marital_choices)
    Home_Address = models.TextField(blank=True, null=True,)
    Mobile_Number = models.CharField(blank=True, null=True, max_length=10)
    Email = models.EmailField(blank=True, null=True, validators=[validate_email])
    region = models.CharField(blank=True, null=True, max_length=2, choices=region_choices)
    Dues_Payment = models.CharField(null=True, max_length=6, choices=dues_choices)
    member_id = models.CharField(primary_key=True, max_length=10, default=id_no)

    Shop_Name = models.TextField(blank=True, null=True)
    RGD_Registered = models.CharField(null=True, max_length=1, choices=reg_choices)
    Tin_number = models.CharField(blank=True, null=True, max_length=20)
    Business_Registration_No = models.CharField(blank=True, null=True, max_length=20)
    Operation_Location = models.CharField(blank=True, null=True, max_length=100)
    Principal_Activity = models.CharField(blank=True, null=True, max_length=200)
    Business_Details = models.TextField(blank=True, null=True,)
    Operation_Mode = models.CharField(blank=True, null=True, max_length=15, choices=operation_choices)
    Date_registered = models.DateField(default=timezone.now)

    class Meta:
        ordering = ('Date_registered',)

    def __str__(self):
        return self.Full_name
