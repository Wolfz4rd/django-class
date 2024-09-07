from django.urls import path
from pagina import views
from pagina.views import HomePagesView

urlpatterns=[

    path("", views.HomePagesView.as_view())
]