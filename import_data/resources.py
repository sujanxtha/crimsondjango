from import_export import resources
from .models import MyData
class MyDataResource(resources.ModelResource):
    class Meta:
        model = MyData