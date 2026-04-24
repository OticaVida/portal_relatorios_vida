from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from relatorios import views as rel_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # LOGIN / LOGOUT
    path('login/', auth_views.LoginView.as_view(template_name='relatorios/login.html'), name='login'),
    # Forçando o redirecionamento pós-logout aqui:
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    # TELA DE BOAS VINDAS (Raiz do site)
    path('', rel_views.dashboard, name='dashboard'), 
    # RELATÓRIOS
    path('relatorio-vendas/', rel_views.relatorio_vendas, name='relatorio_vendas'),
    path('duplicidade-nf/', rel_views.relatorio_duplicidade_nf, name='duplicidade_nf'),
    path('usuarios/', rel_views.painel_usuarios, name='painel_usuarios'),
    path('contracheque/', rel_views.relatorio_contracheque, name='relatorio_contracheque'),
]