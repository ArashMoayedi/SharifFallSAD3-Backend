from django.urls import include, path, re_path
from rest_framework_jwt.views import obtain_jwt_token
from rest_auth.registration.views import VerifyEmailView, RegisterView
from allauth.account.views import confirm_email

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('items/', include('items.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('registration/', RegisterView.as_view(), name='account_signup'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$', confirm_email, name='account_confirm_email'),
    re_path(r'^account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('token-auth/', obtain_jwt_token),
]