"""
Modulo de las URLS ,Se agregan todos los endopoints que seran consumidos por la api del Frontend
"""
from __future__ import barry_as_FLUFL

__author__ = "Victor Torres"
__version__ = "0.1"
__license__ = "GPL"
__status__ = "Development"
__maintainer__ = "Victor Torres"


from django.urls import path, include
from apiCRUD import views

from .views import (ChangePasswordView, registration, filtered_record_view, user_delete_view, my_obtain_token_view,
                    downolad_record_views_csv,
                    download_records_files,
                    lista_filtros
                    )
from rest_framework_simplejwt.views import (
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
    path("down/", downolad_record_views_csv, name="download"),
    path("donwloadzip/", download_records_files, name="zip_file"),
    path("change-password/", ChangePasswordView.as_view(), name="change-pwd"),
    path(
        "password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
    path(
        "password_reset/confirm/",
        include("django_rest_passwordreset.urls",
                namespace="password_reset_confirm"),
    ),
    path("delete/<int:id_user>/", views.user_delete_view, name="delete_user"),
    path("lista_filtros/", views.lista_filtros, name="lista_filtros"),
    path("get_users/", views.get_users, name="get_users"),
    path("add_user/", views.add_user, name="add_user"),
    path("update_user/<int:user_id>/", views.update_user, name="update_user"),
    path("delete_user/<int:user_id>/", views.delete_user, name="delete_user"),
    path("get_hardwares/", views.get_hardwares, name="get_hardwares"),
    path("get_recorders/", views.get_recorders, name="get_recorders"),
    path("add_recorder/", views.add_recorder, name="add_recorder"),
    path("update_recorder/<int:id_h_serial>/", views.update_recorder, name="update_recorder"),
    path("load_master_tables/", views.load_master_tables,
         name="load_master_tables"),
    path("load_udas/", views.load_udas,
         name="load_udas"),
    path("load_labelfile/", views.load_labelfile,
         name="load_labelfile"),
    path("contactanos/", views.contactanos_view, name="contacto"),
    # URL VISTA AUDIOS PÚBLICOS
    path("public-records/", views.public_record_view, name="public_records"),
]
