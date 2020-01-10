from django.urls import path
from AIPOEM import views

urlpatterns = [
  path('signUp',views.sign_up),
  path('emailCheck',views.email_check),
  path('signIn',views.sign_in),
  path('modifyInfo',views.modify_info),
  path('signOut',views.sign_out),
  path('getInfo',views.get_userinfo),
  ]