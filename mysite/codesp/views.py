from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import Modalidade, SolicitarMatricula, AtividadeEspaco,Frequencia, Bolsista, Codesp, Professor, Coordenacao, CategoriaModalidade, EspacoModalidade, Turma, AlunoTurma, FreAluno, SolicitarModalidade
from django.db.models import Count, Q
from itertools import groupby


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/profile')
        else:
            return render(request, 'codesp/index.html')


class ChangePassword(View):
    def get(self, request, *args, **kwargs):
        form_senha = PasswordChangeForm(request.user, request.GET)
        return render(request, 'codesp/mudancaSenha.html', {'form_senha': form_senha})
    def post(self, request, *args, **kwargs):
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('/logout')
        else:
            return render(request, 'codesp/mudancaSenha.html', {'form_senha': form_senha, 'msg': 'g'})



class LoginView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/profile')
        else:
            return render(request, 'codesp/login.html')
    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')


        try:
            name = User.objects.get(email = email).username
        except:
            return render(request, 'codesp/login.html', {'erro':"Email ou senha incorretos"})

        user = authenticate(username=name, password=password)
        path_redirect = request.get_full_path().split('?login=',1)

        if user:
            login(request, user)
            if '?login=' in request.get_full_path():# Redirecting After Login
                return redirect(path_redirect[1])

            elif hasattr(request.user, 'professor'):
                return redirect('/profile')
            elif hasattr(request.user, 'bolsista'):

                return redirect('/profile')
            elif hasattr(request.user, 'coordenacao'):
                return redirect('/profile')

        else:
            return render(request, 'codesp/login.html', {'erro':"Email ou senha incorretos", 'path':path_redirect})

class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('/login')


@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class ProfileView(View):
     def get(self, request, *args, **kwargs):
        if hasattr(request.user, 'coordenacao'):
            contexto = {'autorizacoes': Codesp.objects.all().count()}
            return render(request, 'codesp/codesp/index.html', contexto)
        elif hasattr(request.user, 'professor'):
            try:
                professor = SolicitarModalidade.objects.filter(professor_id = request.user.professor.id)[0]

                turmas = Turma.objects.filter(professor_id=professor)
                dados = []
                atuacao = SolicitarModalidade.objects.filter(professor_id = request.user.professor.id)
                for turma in turmas:
                    dados.append({'alunos':AlunoTurma.objects.filter(turma_id = turma.id).count(), 'turma':turma})

                contexto = {'dados': dados, 'atuacao':atuacao.count()}
                return render(request, 'codesp/professor/index.html', contexto)
            except:

                return render(request, 'codesp/professor/index.html')
        elif hasattr(request.user, 'bolsista'):
            contexto = {'atividade':AtividadeEspaco.objects.all().count(),'matricula': SolicitarMatricula.objects.all().count(), 'professor':Professor.objects.all().count(), 'bolsista':Bolsista.objects.all().count(), 'path': request.path == "/profile"}
            return render(request, 'codesp/bolsista/index.html', contexto)

        else:
            redirect('/logout')

@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class DetalheTurma(View):
    def get(self, request, *args, **kwargs):
        professor = SolicitarModalidade.objects.filter(professor_id=request.user.professor.id)[0]
        return render(request, 'codesp/professor/detalheTurma.html', {'turmas': Turma.objects.filter(professor_id = professor.id)})

# @method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
# class DetalheTurmaCodesp(View):
#     def get(self, request, *args, **kwargs):
#         return render(request, 'codesp/professor/detalheTurma.html', {'turmas': Turma.objects.all()})

@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class DetalheFrequencia(View):
    def get(self, request, *args, **kwargs):
        solic = SolicitarModalidade.objects.filter(professor_id=request.user.professor)[0]
        turmas = Turma.objects.filter(professor=solic)



        ctx = {'turmas':turmas}
        return render(request, 'codesp/professor/detalheFrequencia.html',ctx)


@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class RegistrarEspaco(View):
    def get(self, request, *args, **kwargs):

        return render(request, 'codesp/bolsista/registrarEspaco.html')

@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class RegistrarEspacoAtividade(View):
    def get(self, request, *args, **kwargs):
        turma = Turma.objects.all()
        return render(request, 'codesp/bolsista/registrarEspacoAtividade.html', {'turmas':turma })
    def post(self, request, *args, **kwargs):
        turma = request.POST.get('turma')
        date = request.POST.get('data')
        confirmacao = request.POST.get('confirmacao')
        if turma and confirmacao and date:
            if confirmacao == "true":
                confirmacao = True
            else:
                confirmacao = False
            data = AtividadeEspaco(presenca = confirmacao, turma_id = turma, bolsista_id = request.user.bolsista.id, data = date)
            data.save()

            return redirect('/profile')
        else:
            turma = Turma.objects.all()
            return render(request, 'codesp/bolsista/registrarEspacoAtividade.html', {'turmas':turma })

@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class EditarEspacoAtividade(View):
    def get(self, request, *args, **kwargs):
        turma = AtividadeEspaco.objects.get(id=int(kwargs['t']))
        turmas = Turma.objects.all()
        return render(request, 'codesp/bolsista/registrarEspacoAtividade.html', {'turma':turma.turma.id, 'data': turma.data, 'sol':'g', 'turmas':turmas, "conf": turma.presenca })

    def post(self, request, *args, **kwargs):
        atv = AtividadeEspaco.objects.get(id=int(kwargs['t']))
        turma = request.POST.get('turma')

        data = request.POST.get('data')

        if turma:
            if atv.turma.id != turma:
                turma = Turma.objects.get(id=turma)
                atv.turma = turma

            if atv.data != data:
                atv.data = data

            atv.save()
            return redirect('/detalheEspacoAtividade')
        else:
            turma = AtividadeEspaco.objects.get(id=int(kwargs['t']))
            turmas = Turma.objects.all()
            return render(request, 'codesp/bolsista/registrarEspacoAtividade.html', {'turma':turma.turma.id, 'data': turma.data, 'sol':'g', 'turmas':turmas, "conf": turma.presenca, 'erro':"erro ao editar os campos" })
        #if turma and data:


@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class DetalheEspacoAtividade(View):
    def get(self, request, *args, **kwargs):
        ctx = {'atividades': AtividadeEspaco.objects.all()}
        return render(request, 'codesp/bolsista/detalheEspacoAtividade.html', ctx)
    def post(self, request, *args, **kwargs):
        atividades = request.POST.getlist('atividade')

        for atividade in atividades:
            AtividadeEspaco.objects.get(pk=atividade).delete()

        return redirect("/detalheEspacoAtividade")
@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class DetalheMatricula(View):
    def get(self, request, *args, **kwargs):
        ctx = {'solicitacoes': SolicitarMatricula.objects.all()}
        return render(request, 'codesp/bolsista/detalheMatricula.html', ctx)

    def post(self, request, *args, **kwargs):
        solicitacoes = request.POST.getlist('solicitacao')
        if solicitacoes:
            for solicitacao in solicitacoes:
                SolicitarMatricula.objects.get(pk=solicitacao).delete()

            return redirect("/detalheMatricula")


@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class DetalheAutorizacao(View):
    def get(self, request, *args, **kwargs):
        ctx = {'autorizacoes': Codesp.objects.all()}
        return render(request, 'codesp/codesp/detalheAutorizacao.html', ctx)

    def post(self, request, *args, **kwargs):
        autorizacoes = request.POST.getlist('autorizacao')
        if autorizacoes:
            for autorizacao in autorizacoes:
                Codesp.objects.get(pk=autorizacao).delete()

            return redirect("/detalheAutorizacao")

@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class EditarTurma(View):
    def get(self, request, *args, **kwargs):
        turma = Turma.objects.get(id=int(kwargs['t']))
        modalidade = SolicitarModalidade.objects.filter(professor_id = turma.professor.professor.id)[0]
        mod = modalidade.modalidade.id
        contexto = {'turma': turma, 'modalidade':modalidade, 'sol':"ok", 'professores': SolicitarModalidade.objects.all(),
        'modalidades':Modalidade.objects.all(), 'espacos': EspacoModalidade.objects.all(), 'categorias': CategoriaModalidade.objects.all(), 'mod':mod}
        return render(request, 'codesp/codesp/registrarTurma1.html', contexto)

    def post(self, request, *args, **kwargs):
        turma = Turma.objects.filter(id=int(kwargs['t']))[0]
        modalidade = SolicitarModalidade.objects.filter(professor_id = turma.professor.professor.id)[0]

        nomeT = request.POST.get('nome')
        turnoTurma = request.POST.get('turno')
        espMod = request.POST.get('espaco')
        mod = modalidade.modalidade.id
        prof = request.POST.get('professor')
        cat = request.POST.get('categoria')

        if turma:
            if nomeT and turnoTurma and espMod and mod and prof and cat:

                if turma.nomeTurma != nomeT:
                    turma.nomeTurma = nomeT

                if turma.turno != turnoTurma:
                    turma.turno = turnoTurma

                if turma.espaco.id != espMod:
                    esp = EspacoModalidade.objects.get(id=espMod)
                    turma.espaco = esp

                if modalidade.modalidade.id != mod:
                    mod = modalidade.objects.get(id=mod)
                    modalidade.modalidade = mod

                if turma.professor.professor.id != prof:
                    prof = Professor.objects.get(id=prof)
                    turma.professor.professor = prof

                if modalidade.categoria.id != cat:
                    cat =  CategoriaModalidade.objects.get(id=cat)
                    modalidade.categoria = cat

                turma.save()
                modalidade.save()

                return redirect('/profile')
        else:
            contexto = {'turma': turma, 'modalidade':modalidade, 'sol':"ok", 'professores': Professor.objects.all(),
        'modalidades':Modalidade.objects.all(), 'espacos': EspacoModalidade.objects.all(), 'categorias': CategoriaModalidade.objects.all()}
        return render(request, 'codesp/codesp/registrarTurma1.html', contexto)
@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class EditarMatricula(View):
    def get(self, request, *args, **kwargs):
        matricula = SolicitarMatricula.objects.get(id=int(kwargs['s']))
        categoria = CategoriaModalidade.objects.get(id = matricula.tipoCategoria.id)
        contexto = {'criarModalidade': Modalidade.objects.get(id=int(kwargs['m'])),
        'SolicitarMatricula': matricula,
        'sol':'ok', 'Categorias': CategoriaModalidade.objects.all(), 'criarModalidade2' : Modalidade.objects.exclude(id=int(kwargs['m'])), 'categoria':categoria}
        return render(request, 'codesp/bolsista/solicitarMatricula.html', contexto)
    def post(self, request, *args, **kwargs):

        aluno_nome = request.POST.get('nome_aluno')
        aluno_matricula = request.POST.get('matricula_aluno')
        modalidade = request.POST.get('modalidade_id')
        #modalidade = SolicitarModalidade.objects.get(id=modalidade)



        categoria = request.POST.get('categoria_id')

        #valorBol = Bolsista.objects.filter(email = request.user.email)[0]
        valorMod = Modalidade.objects.get(id = modalidade)
        solicitacao = SolicitarMatricula.objects.get(id=int(kwargs['s']))
        if aluno_nome and modalidade and categoria and aluno_matricula:

            #SolicitarMatricula(nomeAluno = aluno_nome, matricula = aluno_matricula,
            #tipoCategoria=categoria,bolsista_id= valorBol.id, modalidade = valorMod)
            if solicitacao.nomeAluno != aluno_nome:
                solicitacao.nomeAluno = aluno_nome

            if solicitacao.matricula != aluno_matricula:
                solicitacao.matricula = aluno_matricula

            if solicitacao.modalidade != valorMod:
                solicitacao.modalidade = valorMod

            if solicitacao.tipoCategoria.id != categoria:
                categoria = CategoriaModalidade.objects.filter(id=categoria)[0]
                solicitacao.tipoCategoria = categoria
            """
            if solicitacao.bolsista.id != valorBol.id:
                solicitacao.bolsista.id = valorBol.id
            """
            solicitacao.save()

            return redirect('/detalheMatricula')
        else:
            contexto = {'criarModalidade': Modalidade.objects.get(id=int(kwargs['m'])),
        'SolicitarMatricula':SolicitarMatricula.objects.get(id=int(kwargs['s'])),
        'sol':'ok', 'Categorias': CategoriaModalidade.objects.all(), 'criarModalidade2' : Modalidade.objects.exclude(id=int(kwargs['m']))}
        return render(request, 'codesp/bolsista/solicitarMatricula.html', contexto)

@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class RegistrarBolsista(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'codesp/codesp/registrarBolsista.html')

    def post(self, request, *args, **kwargs):
        nome = request.POST.get('nome')
        matricula = request.POST.get('matricula')
        email = request.POST.get('email')

        usuario = User.objects.filter(username = nome).first()
        if usuario:
            return render(request, 'codesp/codesp/registrarBolsista.html', {'erro' : 'Usuário já existe.'})
        else:
            if nome and matricula and email:
                usuario = User.objects.create_user(username=nome, email=email, password=f'{matricula}bolsista' )
                novo = Bolsista(nome=nome, matricula=matricula, email=email, user = usuario)
                usuario.save()
                novo.save()
                return redirect('/registrarBolsista', {'erro':"Usuário criado"})
            else:
                return render(request, 'codesp/codesp/registrarBolsista.html', {'erro' : 'Preencha os campos por completo.'})


@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class RegistrarTurma1(View):
    def get(self, request, *args, **kwargs):
        ctx = {'espacos': EspacoModalidade.objects.all(), 'professores': SolicitarModalidade.objects.all(), 'modalidades': Modalidade.objects.all(), 'categorias':CategoriaModalidade.objects.all()}
        return render(request, 'codesp/codesp/registrarTurma1.html', ctx)
    def post(self, request, *args, **kwargs):
        nomeT = request.POST.get('nome')
        turnoTurma = request.POST.get('turno')
        espMod = request.POST.get('espaco')
        prof = request.POST.get('professor')
        cat = request.POST.get('categoria')

        if nomeT and turnoTurma and espMod and prof and cat:
            mod = SolicitarModalidade.objects.filter(professor_id = int(prof))[0]
            mod = mod.id
            novaTurma = Turma(nomeTurma = nomeT, turno = turnoTurma, espaco_id = espMod, professor_id = mod)
            novaTurma.save()
            ctx = {'modalidade': mod, 'categoria': cat, 'turmaNome': nomeT, 'professor': prof}
            request.session['espaco'] = espMod
            request.session['modalidade'] = mod
            request.session['categoria'] = cat
            request.session['turmaNome'] = nomeT
            request.session['professor'] = prof

            return redirect('/registrarTurma2')
        else:
            ctx = {'erro': "preencha os campos corretamente.",'espacos': EspacoModalidade.objects.all(), 'professores': Professor.objects.all(), 'modalidades': SolicitarModalidade.objects.all(), 'categorias':CategoriaModalidade.objects.all()}
            return render(request, 'codesp/codesp/registrarTurma1.html', ctx)

@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class RegistrarTurma2(View):
    def get(self, request, *args, **kwargs):

        contexto = {'SolicitarMatricula' : SolicitarMatricula.objects.filter(autorizado = 'True').filter(modalidade = request.session.get('modalidade')).filter(tipoCategoria = request.session.get('categoria'))}
        #contexto = {'AutorizadoMatricula' : request.session.get('categoria')}
        return render(request, 'codesp/codesp/registrarTurma2.html',contexto)
    def post(self, request, *args, **kwargs):
        list_autorizados = request.POST.getlist('autorizado_id')

        if list_autorizados:
            for autorizados in list_autorizados:
                aluno = Codesp.objects.get(solicitacao_id = autorizados)
                #aluno = Codesp.objects.all().filter(solicitacao_id=autorizados)[0]
                #turma = Turma.objects.filter(nomeTurma = request.session.get('turmaNome'))[0]
                turma = Turma.objects.get(nomeTurma = request.session.get('turmaNome'))
                cadastroTurma = AlunoTurma(alunos = aluno, turma = turma)
                cadastroTurma.save()
            return redirect("/profile")
        else:
            return redirect("/profile")



@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class RegistrarModalidade(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'codesp/codesp/registrarModalidade.html')
    def post(self, request, *args, **kwargs):
        modalidade = request.POST.get('nomeModalidade')
        desc = request.POST.get('descricao')


        if modalidade and desc:
            novo = Modalidade(nomeModalidade = modalidade, descricao = desc)
            novo.save()
            return redirect('/profile')
        else:
            contexto = {'erro': "Preencha os campos corretamente."}
            return render(request, 'codesp/codesp/registrarModalidade.html', contexto)


@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class RegistrarProfessor(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'codesp/codesp/registrarProfessor.html')

    def post(self, request, *args, **kwargs):

        nome = request.POST.get('nome')
        matricula = request.POST.get('matricula')
        email = request.POST.get('email')

        usuario = User.objects.filter(username = nome).first()
        if usuario:
            return render(request, 'codesp/codesp/registrarProfessor.html', {'erro' : 'Usuário já existe.'})
        else:
            if nome and matricula and email:
                usuario = User.objects.create_user(username=nome, email=email, password=f'{matricula}prof')
                novo = Professor(nome=nome, matricula=matricula, email=email, user = usuario)
                usuario.save()
                novo.save()
                return redirect('/registrarProfessor', {'erro':"Usuário criado"})
            else:
                return render(request, 'codesp/codesp/registrarProfessor.html', {'erro' : 'Preencha os campos por completo.'})

@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class ProfessorLogin(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'codesp/professor/login.html')

    def post(self, request, *args, **kwargs):

        nome = request.POST.get('nome')
        matricula = request.POST.get('matricula')
        email = request.POST.get('email')

        if nome and matricula and email:
            novo = SolicitarMatricula(nome=nome, matricula=matricula, email=email)
            usuario = User.objects.create_user(nome, email, f'{matricula}prof')
            usuario.save()
            novo.save()
            return redirect('/login')


@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class ProfessorView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'codesp/professor/index.html')




@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class BolsistaView(View):
    def get(self, request, *args, **kwargs):
        contexto = {'criarModalidade': Modalidade.objects.all(), 'SolicitarMatricula':SolicitarMatricula.objects.all(),
        'Bolsista':Bolsista.objects.all(), 'Categorias': CategoriaModalidade.objects.all()}
        return render(request, 'codesp/bolsista/solicitarMatricula.html', contexto)

    def post(self, request, *args, **kwargs):
        aluno_nome = request.POST.get('nome_aluno')
        aluno_matricula = request.POST.get('matricula_aluno')
        modalidade = request.POST.get('modalidade_id')
        #modalidade = SolicitarModalidade.objects.get(id=modalidade)

        # valorMod = SolicitarModalidade.objects.get(id = modalidade)


        categoria = request.POST.get('categoria_id')

        valorBol = Bolsista.objects.filter(email = request.user.email)[0]

        #bolsista = Bolsista.objects.get('bolsista')
        if aluno_nome and aluno_matricula and modalidade and categoria:
            novo = SolicitarMatricula(nomeAluno = aluno_nome, matricula = aluno_matricula, tipoCategoria_id=categoria,bolsista_id= valorBol.id, modalidade_id = modalidade)
            novo.save()
            return redirect('/profile',{'msg':"Matricula solicitada com sucesso"})

        else:
            return render(request, 'codesp/bolsista/solicitarMatricula.html',{'Bolsista':Bolsista.objects.all(),'criarModalidade': SolicitarModalidade.objects.all(), 'SolicitarMatricula':SolicitarMatricula.objects.all(), 'error': "Erro ao solicitar, tente novamente"})


@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class CodespView(View):
    def get(self, request, *args, **kwargs):
        contexto = {'SolicitarMatricula' : SolicitarMatricula.objects.filter(autorizado = 'False')}
        return render(request, 'codesp/codesp/autorizarMatricula.html', contexto)

    def post(self, request, *args, **kwargs):
        list_solicitacao = request.POST.getlist('solicitacao_id')
        #coordI = request.POST.get('coordenacao')

        if list_solicitacao:
            for solicitacao in list_solicitacao:
                aluno = SolicitarMatricula.objects.get(id=solicitacao)
                coordenacao = Coordenacao.objects.get(nome = request.user.username)
                aluno.autorizado = True
                aluno.save()
                novo = Codesp(solicitacao = aluno, coordenacao = coordenacao)
                novo.save()
            return redirect('/profile')

        else:
            return redirect('/solicitarMatricula',{'Bolsista':Bolsista.objects.all(),'criarModalidade': SolicitarModalidade.objects.all(), 'SolicitarMatricula':SolicitarMatricula.objects.all()})


@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class AutorizarSolicitacoes(View):
    def get(self, request, *args, **kwargs):
        contexto = {'SolicitarModalidade' : SolicitarMatricula.objects.filter(autorizado = 'False')}
        return render(request, 'codesp/codesp/autorizarMatricula.html', contexto)

    def post(self, request, *args, **kwargs):
        list_solicitacao = request.POST.getlist('solicitacao_id')
        coordI = request.POST.get('coordenacao')
        coord = Coordenacao.objects.get(nome = coordI)
        if list_solicitacao:
            for solicitacao in list_solicitacao:
                aluno = SolicitarMatricula.objects.get(id=solicitacao)
                aluno.autorizado = True
                aluno.save()
                novo = Codesp(solicitacao = aluno, coordenacao = coord)
                novo.save()
            return redirect('/autorizarMatricula', {'SolicitarMatricula' : SolicitarMatricula.objects.all()})

        else:
            return redirect('/solicitarMatricula',{'Bolsista':Bolsista.objects.all(),'criarModalidade': SolicitarModalidade.objects.all(), 'SolicitarMatricula':SolicitarMatricula.objects.all()})




@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class solicitarAtuacaoView(View):

    def get(self, request, *args, **kwargs):
        contexto = {'criarModalidade': Modalidade.objects.all(), 'u':request.user.username}
        return render(request, 'codesp/professor/solicitarAtuacao.html', contexto)

    def post(self, request, *args, **kwargs):
        horarioInicial = request.POST.get('horarioInicial')
        horarioFinal = request.POST.get('horarioFinal')
        justificativa = request.POST.get('justificativa')
        modalidade = request.POST.get('modalidade_id')
        categoria = request.POST.get('categoria')
        categoriaMod = CategoriaModalidade.objects.get(categoria = categoria)
        list_dias = request.POST.getlist('dias')
        dias = ''
        if list_dias:
            for d in list_dias:
                dias += d
        if horarioInicial and horarioFinal and justificativa and categoria and modalidade and dias:

            novo = SolicitarModalidade(horarioInicial=horarioInicial, horarioFinal=horarioFinal, justificativa=justificativa,professor_id=request.user.professor.id, modalidade_id=modalidade, categoria=categoriaMod, diasDaSemana=dias)
            novo.save()
            return render(request, 'codesp/professor/solicitarAtuacao.html', { 'criarModalidade': SolicitarModalidade.objects.all()})

        else:
            return render(request, 'codesp/professor/solicitarAtuacao.html',{ 'criarModalidade': SolicitarModalidade.objects.all()})



@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class FrequenciaView(View):
    def get(self, request, *args, **kwargs):
        ctx = {'alunos':AlunoTurma.objects.filter(turma_id=int(kwargs['t']))}
        return render(request, 'codesp/professor/frequencia.html', ctx)
    def post(self, request, *args, **kwargs):
        data =  request.POST.get('data')
        descricao = request.POST.get('descricao')
        alunos =  request.POST.getlist('alunos')

        presenca = request.POST.get('presenca')

        if data and descricao and alunos:
            dado = Frequencia(descricaoAula = descricao, data = data)
            dado.save()

            for aluno in alunos:

                dado1 = FreAluno(aluno_id=aluno, frequencia_id=dado.id, presenca = presenca)
                dado1.save()
            return redirect('/profile')
        else:
            return redirect('/frequencia')

@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class EditarFrequenciaView(View):
    def get(self, request, *args, **kwargs):

        aluno = AlunoTurma.objects.filter(turma_id=int(kwargs['t']))[0]
        alunos = FreAluno.objects.filter(aluno_turma_id =kwargs['t'])

        frequencia = FreAluno.objects.get(aluno_id = aluno.id)
        frequencia1 = Frequencia.objects.get(id = frequencia.id)

        ctx = {'alunos':alunos, 'frequencia': frequencia1, 'sol':"g"}
        return render(request, 'codesp/professor/frequencia.html', ctx)
    def post(self, request, *args, **kwargs):
        aluno = AlunoTurma.objects.filter(turma_id=int(kwargs['t']))[0]


        frequencia = FreAluno.objects.get(aluno_id = aluno.id)
        frequencia1 = Frequencia.objects.get(id = frequencia.id)

        data =  request.POST.get('data')
        descricao = request.POST.get('descricao')
        alunos1 =  request.POST.getlist('alunos')

        if data and descricao and alunos1:

            # for aluno in alunos1:
            #     alunos = FreAluno.objects.filter(aluno_id =aluno.id)

            if frequencia1.data != data:
                frequencia1.data =  data
            if frequencia1.descricaoAula != descricao:
                frequencia1.descricaoAula = descricao
            frequencia1.save()

            # dado = Frequencia(descricaoAula = descricao, data = data)
            # dado.save()

            # for aluno in alunos:

            #     dado1 = FreAluno(aluno_id=aluno, frequencia_id=dado.id, presenca = 2)
            #     dado1.save()
            return redirect('/detalheFrequencia')
        else:
            return redirect('/frequencia')




@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class RegistrarCategoria(View):
    def get(self, request, *args, **kwargs):
        # ctx = {'value':CategoriaSolicitarModalidade.objects.filter(id=1)[0]}
        return render(request, 'codesp/codesp/registrarCategoria.html')
    def post(self, request, *args, **kwargs):
        tipoCategoria = request.POST.get("categoria")
        desc = request.POST.get("descricao")

        if tipoCategoria and desc:
            categoria = CategoriaModalidade(categoria = tipoCategoria, descricao = desc)
            categoria.save()
            return redirect('codesp:login')
        else:
            return render(request, 'codesp/codesp/registrarCategoria.html', {'erro' : 'Preencha os campos corretamente.'})





@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class RegistrarCoordenacao(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'codesp/codesp/registrarCoordenacao.html')
    def post(self, request, *args, **kwargs):
        nomeCoordenacao = request.POST.get('nome')
        matriculaCoord = request.POST.get('matricula')
        emailCoord = request.POST.get('email')

        usuario = User.objects.filter(username = nomeCoordenacao).first()
        if usuario:
             return render(request, 'codesp/codesp/registrarCoordenacao.html', {'erro' : 'Usuário já existe.'})
        else:
            if nomeCoordenacao and matriculaCoord and emailCoord:
                usuario = User.objects.create_user(username= nomeCoordenacao, email=emailCoord, password=f'{matriculaCoord}coord')
                novo = Coordenacao(nome=nomeCoordenacao, matricula=matriculaCoord, email=emailCoord, user = usuario)
                usuario.save()
                novo.save()
                return redirect('codesp:profile')
            else:
                return render(request, 'codesp/codesp/registrarCoordenacao.html', {'erro' : 'Preencha os campos corretamente.'})



@method_decorator(login_required(login_url="/login", redirect_field_name="login"), name='dispatch')
class RegistrarEspacoModalidade(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'codesp/codesp/registrarEspacoModalidade.html')

    def post(self, request, *args, **kwargs):
        nomeEspaco = request.POST.get('nome')
        desc = request.POST.get('descricao')

        if nomeEspaco and desc:
            espaco = EspacoModalidade(nome = nomeEspaco, descricao = desc)
            espaco.save()
            return redirect('/profile')
        else:
            return render(request, 'codesp/codesp/registrarEspacoModalidade.html', {'erro' : 'Preencha os campos corretamente.'})
