from django.urls import path
from django.contrib.auth.views import LoginView, auth_login
from django.contrib.auth.views import LogoutView

from .forms import AuthenticationForm
from . import views

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'accounts/login/', LoginView.as_view(template_name='login.html', authentication_form=AuthenticationForm), name='login'),
    path(r'accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
    # path(r'accounts/login/', LoginView, {
    #     'template_name': 'login.html',
    #     'authentication_form': AuthenticationForm
    # }, name='login'),
    # path(r'accounts/logout/', LogoutView, {
    #     'next_page': '/'
    # }, name='logout')
    path(r'accounts/signup/', views.signup, name='signup'),
    path(r'games-list/highlighted/', views.show_all_highlighted_games),
    path(r'games-list/all/', views.show_all_games),
    path(r'cart/', views.ShoppingCartEditView.as_view(), name='user-cart'),
    path(r'cart/add/<int:game_id>/', views.add_to_cart),
]
