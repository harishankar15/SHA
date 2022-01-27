from django.db import models


class addproductModel(models.Model):
    hsnCode = models.IntegerField()
    productname = models.CharField(max_length=20)
    productprice = models.IntegerField()
    def __str__(self):
        return self.productname
  
