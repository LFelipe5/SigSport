from django.urls import path
from . import views
app_name = 'codesp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login', views.LoginView.as_view(), name='login'),
    path('redefinirSenha', views.ChangePassword.as_view(), name="redefinirSenha"),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('solicitarMatricula', views.BolsistaView.as_view(), name="solicitarMatricula"),
    path('autorizarMatricula', views.CodespView.as_view(), name="autorizarMatricula"),
    path('solicitarAtuacao', views.solicitarAtuacaoView.as_view(), name='solicitarAtuacao'),
    path('profile', views.ProfileView.as_view(), name="profile"),
    path('frequencia/<int:t>', views.FrequenciaView.as_view(), name='frequencia'),
    path('registrarProfessor', views.RegistrarProfessor.as_view(), name="registrarProfessor"),
    path('registrarBolsista', views.RegistrarBolsista.as_view(), name="registrarBolsista"),
    path('registrarUsoEspaco', views.RegistrarEspaco.as_view(), name="registrarEspaco"),
    path('registrarEspacoAtividade', views.RegistrarEspacoAtividade.as_view(), name="registrarEspacoAtividade"),
    path('registrarModalidade', views.RegistrarModalidade.as_view(), name = "registrarModalidade"),
    path('registrarTurma1', views.RegistrarTurma1.as_view(), name="registrarTurma1"),
    path('registrarTurma2', views.RegistrarTurma2.as_view(), name="registrarTurma2"),
    path('registrarCoordenacao', views.RegistrarCoordenacao.as_view(), name = "registrarCoordenacao"),
    path('autorizarSolicitacoes', views.AutorizarSolicitacoes.as_view(), name ="autorizarSolicitacoes"),
    path('registrarCategoria', views.RegistrarCategoria.as_view(), name = "registrarCategoria"),
    path('detalheMatricula', views.DetalheMatricula.as_view(), name="detalheMatricula"),
    path('detalheAutorizacao', views.DetalheAutorizacao.as_view(), name="detalheAutorizacao"),
    path('detalheEspacoAtividade', views.DetalheEspacoAtividade.as_view(), name="detalheEspacoAtividade"),
    path('detalheTurma', views.DetalheTurma.as_view(), name="detalheTurma"),
    path('detalheFrequencia', views.DetalheFrequencia.as_view(), name="detalheFrequencia"),
    path('editarMatricula/<int:s>/<int:m>', views.EditarMatricula.as_view(), name="editarMatricula"),
    path('editarTurma/<int:t>', views.EditarTurma.as_view(), name="editarTurma"),
    path('editarFrequencia/<int:t>', views.EditarFrequenciaView.as_view(), name="editarFrequencia"),
    path('editarEspacoAtividade/<int:t>', views.EditarEspacoAtividade.as_view(), name="editarEspacoAtividade"),
    path('registrarEspaco', views.RegistrarEspacoModalidade.as_view(), name="registrarEspacoModalidade"),



]
