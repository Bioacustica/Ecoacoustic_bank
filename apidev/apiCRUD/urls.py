from django import urls
from django.contrib import admin
from django.urls import path, include
from apiCRUD import views
from .views import ChangePasswordView, registration
from rest_framework_jwt.views import   obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from apiCRUD.views import MyObtainTokenView
from rest_framework.routers import DefaultRouter
# Aqui creamos las urls con un sobrenombre memotecnico
# apuntando a su vista correspondiente

router = DefaultRouter()
router.register("Funding", views.FundingsView)
router.register("Case", views.CaseView)
router.register("Catalogue", views.CatalogueView)
router.register("CatalogueObs", views.CatalogueObsView)
router.register("Datum", views.DatumView)
router.register("Evidence", views. EvidenceView)
router.register("Format", views.FormatView)
router.register("HSerial", views.HSerialView)
router.register("Habitat", views.HabitatView)
router.register("Hardware", views.HardwareView)
router.register("Label", views.LabelView)
router.register("Labeled", views.LabeledView)
router.register("Memory", views.MemoryView)
router.register("PhotoPath", views.PhotoPathView)
router.register("Precision", views.PrecisionView)
router.register("Project", views.ProjectView)
router.register("Record", views.RecordView)
router.register("RecordObs", views.RecordObsView)
router.register("RecordPath", views.RecordPathView)
router.register("Sampling", views. SamplingView)
router.register("Season", views.SeasonView)
router.register("Supply", views.SupplyView)
router.register("Type", views.TypeView)
router.register("User", views.UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_jwt_token),
    path('token/verify/', verify_jwt_token),
    path('token/refresh/', refresh_jwt_token),
    path('register/', registration, name='register'),
    path('change-password/',ChangePasswordView.as_view(), name='change-pwd'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('password_reset/confirm/', include('django_rest_passwordreset.urls', namespace='password_reset_confirm'))
]
