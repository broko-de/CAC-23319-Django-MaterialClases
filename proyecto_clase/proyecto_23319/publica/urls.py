from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='inicio'),
    path('quienes_somos/',views.quienes_somos,name='quienes_somos'),
    path('proyectos/',views.proyectos,name="proyectos"),
    path('api_proyectos/',views.api_proyectos,name="api_proyectos"),
    path('cursos/',views.ver_cursos,name="cursos"),

    #autenticacion
    path('cuentas/registrarse', views.cac_registrarse, name='registrarse'),
    # path('cuentas/login', views.cac_login, name='login'),
    # path('cuentas/logout/',
    #      auth_views.LogoutView.as_view(template_name='cac/publica/index.html'), name='logout'),
    
    #por defecto de django    
    path('accounts/login/', auth_views.LoginView.as_view(
            template_name='publica/login.html',
            extra_context={'variable':'TEST'},
        )),
    path('accounts/logout/',
         views.CacLogoutView.as_view(), name='logout'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(success_url="/"), name='password_change'), 
    path('accounts/', include('django.contrib.auth.urls')),


    path('hola_mundo', views.hola_mundo, name='hola'),
    path('saludar/<str:nombre>/', views.saludar, name='saludar'),
    
    path('proyectos/2023/04/', views.ver_proyectos_04_2023, name='ver_proyectos_04_2023'),
    path('proyectos/<int:anio>/', views.ver_proyectos_uno, name='ver_proyectos'),
    path('proyectos/<int:anio>/<int:mes>/', views.ver_proyectos, name='ver_proyectos'),
    
] 