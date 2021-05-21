from django import urls
from django.contrib import admin
from django.urls import path, include
from apiCRUD import views
from rest_framework.routers import DefaultRouter
# Aqui creamos las urls con un sobrenombre memotecnico
# apuntando a su vista correspondiente

# router = DefaultRouter()
# router.register('Fundings', viewset=views.FundingsPG)

urlpatterns = [
    # path('',include(router.urls)),
    path('', views.FundingsPG.as_view()),
    path("<int:id_funding>", views.FundingsPD.as_view())
]
