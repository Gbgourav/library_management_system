
from django.contrib import admin
from django.urls import path, include
from home import views
from home.forms import LoginForm
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('BookEntryAPI', views.BookEntryModelViewSet, basename = 'bookEntry')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name='home'),
    path("home/", views.index, name='home'),
    path("about/", views.about, name='about'),
    path("bookEntry", views.bookEntry, name='bookEntry'),
    path("profile/", views.bookEntry, name='bookEntry'),
    path('signup/', views.SignUpFormView.as_view(), name="signup"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout' ),
    path('api/', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace= 'rest_framework')),
    
]

# I used Router for 'api/' to auto config the urls.Routers provides a simple, quick and consistent way of wiring ViewSet logic to a set of URLs. 
# views.SignUpFormView.as_view() is calling a static method on the SignUpFormView class, which constructs and returns an 
# instance of SignUpFormView if we see in views.py we have func SignUpFormView so if someone will hit the /signup then SignUpFormView will run.
# I used auth_views.LoginView.as_view to show the login form and perform the actions in it. Its a builtin funcation. We import LoginForm from froms.py to perform the actions.
# I used auth_views.LogoutView.as_view to get message if user is logout and user can rederct to the "login.html" if user is logout. its a builtin funcation.


