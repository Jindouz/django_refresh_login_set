from . import views
from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('books/',views.books ),
    path('books/<int:id>/', views.books, name='book-detail'),
    path('books/currentuser/', views.books_currentuser),
    path('login', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('register', views.register),
    path('protected', views.getNotes),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

