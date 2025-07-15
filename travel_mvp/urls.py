# Create the main urls.py file
urls_content = '''from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('travel.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''

with open('travel_mvp_urls.py', 'w') as f:
    f.write(urls_content)

print("✅ travel_mvp/urls.py created")