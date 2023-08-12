from django.db import models

class Item(models.Model):

    item_name=models.CharField(max_length=50)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField()
    item_img=models.CharField(max_length=30,blank=False)

    def __str__(self):
        return self.item_name