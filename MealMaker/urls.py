from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from SearchMeal import views

urlpatterns = [
    # Examples:
    url(r'^$', views.base),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include('SearchMeal.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
