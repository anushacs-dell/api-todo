from django.db import models

class Create(models.Model):
    name=models.CharField(max_length=100)
    product_num=models.IntegerField()
    regular_price=models.IntegerField()
    sales_price=models.IntegerField()

    def __str__(self):
        return self.name
    
