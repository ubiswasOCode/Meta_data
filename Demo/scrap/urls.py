from django.urls import path,include
from scrap import views
urlpatterns = [
    path('', views.Scraping,name="Scraping"),
    # path('Scra',views.Scraping,name='Scraping'),
]
