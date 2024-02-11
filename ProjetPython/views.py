from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required  # Importez cette décoration
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from ProjetPython.forms import SessionForm, FormSubmissionForm
from ProjetPython.models import Session, FormSubmission
from django.shortcuts import render

def formulaire_client(request):
    return render(request, 'client.html')


@login_required
def session_list(request):
    sessions = Session.objects.all()
    return render(request, 'templates/session_list.html', {'sessions': sessions})

@login_required
def create_session(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            session = form.save()
            return redirect('session_detail', pk=session.pk)
    else:
        form = SessionForm()
    return render(request, 'create_session.html', {'form': form})

@login_required
def session_detail(request, pk):
    session = get_object_or_404(Session, pk=pk)
    form_submissions = FormSubmission.objects.filter(session=session)
    return render(request, 'session_detail.html', {'session': session, 'form_submissions': form_submissions})

@login_required
def submit_form(request, session_pk):
    session = get_object_or_404(Session, pk=session_pk)
    if session.form_status == 'closed':
        return HttpResponseForbidden("Le formulaire est fermé.")
    if request.method == 'POST':
        form = FormSubmissionForm(request.POST)
        if form.is_valid():
            form_submission = form.save(commit=False)
            form_submission.student = request.user.student
            form_submission.session = session
            form_submission.save()
            return redirect('session_detail', pk=session_pk)
    else:
        form = FormSubmissionForm()
    return render(request, 'submit_form.html', {'form': form, 'session': session})

@csrf_exempt
def submit_response_view(request):
    if request.method == 'POST':
        # Vérifier le token dans la requête
        token = request.POST.get('token')
        if token != 'votre_token_secret':
            return HttpResponseForbidden("Accès refusé: Token invalide.")
        # Code pour gérer la soumission de réponses
        return HttpResponse("Réponse soumise avec succès")
    else:
        return HttpResponseForbidden("Méthode de requête non autorisée.")

@login_required
def login_view(request):
    if request.method == 'POST':
        # Gérer la logique d'authentification ici
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Rediriger l'utilisateur vers une page appropriée après la connexion
            return redirect('home')  # Remplacez 'home' par le nom de votre vue après la connexion
        else:
            # Afficher un message d'erreur de connexion invalide
            return render(request, 'login.html', {'error_message': 'Identifiant ou mot de passe incorrect'})
    else:
        return render(request, 'login.html')


