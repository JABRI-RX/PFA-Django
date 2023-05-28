 
from django.urls import path
from Product.views import detail

app_name = "Product"
urlpatterns = [
     path("<int:pk>/",detail,name="detail")
]