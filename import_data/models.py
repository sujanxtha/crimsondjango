from django.db import models

class MyData(models.Model):
    busy_po_no = models.IntegerField()
    party_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    qty_main = models.IntegerField()
    class Meta:
        app_label = 'import_data'

   
