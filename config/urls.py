# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework.authtoken.views import obtain_auth_token

# Simple homepage view
def home(request):
    return HttpResponse("Welcome to Routine Tracker API!")

urlpatterns = [
    # Homepage
    path('', home),

    # Admin panel
    path('admin/', admin.site.urls),

    # Token authentication endpoint
    path('api-token-auth/', obtain_auth_token),

    # Include tasks app URLs (we'll create this next)
    path('tasks/', include('tasks.urls')),  # Make sure tasks/urls.py exists
]
