from django.conf import settings
from django.conf.urls.static import static
from django .urls import path
from . import views

urlpatterns = [
    path(r'',views.home,name='home'),
    path(r'^project/$',views.project,name ='project'),
    path(r'^upload_form/$',views.project,name ='new_project'),
    
    
    
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)