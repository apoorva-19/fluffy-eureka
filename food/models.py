from django.db import models

class Item(models.Model):

    def __str__(self):
        return self.item_name
    item_name = models.CharField(max_length=20)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://lh3.googleusercontent.com/proxy/XY2-s8N-sBqJVpUns28STtU0Y3B_Nygv3dE4W3I5KX_RIAibk63DtSGrEv-1Lk5Aitg-dEgUpnoGYge93n4euRZZTQc2rxODrhNZna3FCCCJ0W2DctKGVBf5c3tW")