from django.urls import path
from . import views
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import (
    
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('',views.getData),
    path('user/register/',views.register, name='user_register'),
    path('addrecipe/',views.addrecipe,name='add_recipe'),
    path('updaterecipe/',views.updaterecipe,name='update_recipe'),
    path('getuserdashboard/',views.get_user_dashboard,name='get_user_dashboard'),
    path('gosearch/',views.gosearch,name='go_search'),
    path('recipedelete/<str:id>',views.recipe_delete,name='recipe_delete'),
    path('getusername/<str:email>',views.getUsername,name='get_username'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('userrecipe/<str:id>',views.user_recipe,name="user_recipe"),
    path('updatevote/id=<str:id>&vote=<str:type>',views.updatevote,name="upvote_recipe"),
    path('getrecipies/<str:item>',views.getRecipies,name='get_recipies'),
    path('availableveg/',views.availableVeg,name='available_vegetables'),
    path('userdetails/<str:username>',views.userdetails,name='user_details'),
    path('userrecipes/<str:username>',views.userrecipes,name='user_recipes'),
    path('updateuserinfo/<str:username>',views.updateuserinfo,name='update_userinfo'),
]
