from django.urls import include, path

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('items/', include('items.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]