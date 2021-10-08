from django import urls
from django.contrib import admin
from django.urls import path, include
from apiCRUD import views

from .views import ChangePasswordView, registration, filtered_record_view, user_delete_view, my_obtain_token_view ,downolad_record_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

# Aqui creamos las urls con un sobrenombre memotecnico
# apuntando a su vista correspondiente

router = DefaultRouter()
router.register("Funding", views.FundingsView)
router.register("Case", views.CaseView)
router.register("Catalogue", views.CatalogueView)
router.register("CatalogueObs", views.CatalogueObsView)
router.register("Country", views.CountryView)
router.register("Datum", views.DatumView)
router.register("Microphone", views.MicrophoneView)
router.register("Department", views.DepartmentView)
router.register("Evidence", views.EvidenceView)
router.register("FrequencyDetail", views.FrequencyDetailView)
router.register("Format", views.FormatView)
router.register("HSerial", views.HSerialView)
router.register("Habitat", views.HabitatView)
router.register("Hardware", views.HardwareView)
router.register("Label", views.LabelView)
router.register("Labeled", views.LabeledView)
router.register("Locality", views.LocalityView)
router.register("Gain", views.GainView)
router.register("Filter", views.FilterView)
router.register("Measure", views.MeasureView)
router.register("Memory", views.MemoryView)
router.register("Municipality", views.MunicipalityView)
router.register("PhotoPath", views.PhotoPathView)
router.register("Precision", views.PrecisionView)
router.register("Project", views.ProjectView)
router.register("PulseType", views.PulseTypeView)
router.register("Record", views.RecordView)
router.register("RecordObs", views.RecordObsView)
router.register("RecordPath", views.RecordPathView)
router.register("Sampling", views.SamplingView)
router.register("Season", views.SeasonView)
router.register("Software", views.SoftwareView)
router.register("Supply", views.SupplyView)
router.register("TimeDetail", views.TimeDetailView)
router.register("Type", views.TypeView)
router.register("Vereda", views.VeredaView)
router.register("Voucher", views.VoucherView)
router.register("User", views.UserView)

urlpatterns = [
    path("", include(router.urls)),
    path("login/", my_obtain_token_view, name="login"),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("register/", registration, name="register"),
    path("filter/", filtered_record_view, name="filter"),
    path("down/", downolad_record_views, name= "download"),
    path("change-password/", ChangePasswordView.as_view(), name="change-pwd"),
    path(
        "password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
    path(
        "password_reset/confirm/",
        include("django_rest_passwordreset.urls", namespace="password_reset_confirm"),
    ),
    path("delete/<int:id_user>/", views.user_delete_view, name="delete_user"),
]
