from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=120)
    reg_no = models.CharField(max_length=20, unique=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    # email_is_school = models.BooleanField(default=False)
    portfolio_link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ["reg_no"]

    def __str__(self):
        return f"{self.reg_no} {self.name}"