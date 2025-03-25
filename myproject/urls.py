from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path("admin/", admin.site.urls),
    path("patient/", include("patient.urls")),
    path("", lambda request: redirect("/patient/wizard/", permanent=True)),  # ルートをリダイレクト
]