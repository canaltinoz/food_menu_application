from django.db import models

class Item(models.Model):

    item_name=models.CharField(max_length=50)
    item_desc=models.CharField(max_length=200)
    item_price=models.IntegerField()
    item_img=models.ImageField(default='default_food.jpg',blank=True,editable=True,null=True)

    def __str__(self):
        return self.item_name