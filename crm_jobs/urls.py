from django.urls import path
from . import views

urlpatterns = [
    path("dashboard", views.Dashboard.as_view(), name="dashboard"),
    path("client/<uuid:pk>", views.ClientDetail.as_view(), name="client-detail"),
    path("client-list", views.ClientList.as_view(), name="client-list"),
    path("client/create/", views.ClientCreate.as_view(), name="client-create"),
    path("client/update/<uuid:pk>", views.ClientUpdate.as_view(), name="client-update"),
    path("client/note/create/<uuid:pk>", views.ClientNoteCreate.as_view(), name="client-note-create"),
    path("client/delete/<uuid:pk>", views.ClientDelete.as_view(), name="client-delete"),
    path("inspection/<uuid:pk>", views.InspectionDetail.as_view(), name="inspection-detail"),
    path("inspection-list", views.InspectionList.as_view(), name="inspection-list"),
    path("inspection/create/<uuid:pk>", views.InspectionCreate.as_view(), name="inspection-create"),
    path("inspection/update/<uuid:pk>", views.InspectionUpdate.as_view(), name="inspection-update"),
    path("nspection/delete/<uuid:pk>", views.InspectionDelete.as_view(), name="inspection-delete")
]
