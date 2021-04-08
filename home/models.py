from django.db import models

# Create your models here.
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name + ' - ' + self.email


class Customer(models.Model):
    name = models.CharField(max_length=122)
    email = models.EmailField()
    account_no = models.CharField(max_length=122)
    ifsc_code = models.CharField(max_length=122)
    amount = models.IntegerField()

    def __str__(self):
        return self.name + ' - ' + self.account_no

class Transaction(models.Model):
    source_name = models.CharField(max_length=122)
    source_acc_no = models.CharField(max_length=122)
    money_transfer = models.IntegerField()
    destination_name = models.CharField(max_length=122)
    destination_acc_no = models.CharField(max_length=122)
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.source_name + ' -> ' + self.destination_name

