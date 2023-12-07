from django.contrib import admin
from django.urls import path, include

from django.conf import settings  # this is to import the settings configuration
# to import the static in the settings
from django.conf.urls.static import static
# this import communicate with the index.html in the build in React
from django.views.generic import TemplateView


urlpatterns = [
    path('api/admin/', admin.site.urls),
    path('api/', include('account.api.urls')),
    path('api/account/', include('account.urls')),
    path('api/insurance/', include('insurance.urls')),
    path('api/patient/', include('patient.urls')),
    path('api/treatment/', include('treatment.urls')),
    path('api/appointment/', include('appointment.urls')),
    path('api/payment/', include('bill.urls')),
    path('api/clinic/', include('clinic.urls')),
    path('api/expenses/', include('expenses.urls')),
    path('', TemplateView.as_view(template_name='index.html'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
