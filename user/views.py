from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DeleteView, DetailView
from django.contrib.auth.views import LoginView as DjangoLoginView
from user.forms import SignUpForm, LoginForm, UserForm, ProfileForm
from user.models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()
from manage_post.models import Article
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'login/register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()

        user = authenticate(
            self.request,
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
        )

        if user:
            login(self.request, user)

        return redirect('index')

class LoginView(DjangoLoginView):
    form_class = LoginForm
    template_name = 'login/login.html'
    redirect_authenticated_user = True


class UserUpdateView(LoginRequiredMixin, TemplateView):

    template_name = 'login/profile.html'

    #Retornar al login si no esta autenticado

    login_url = 'login'

    #Formularios
    user_form = UserForm
    profile_form = ProfileForm

    def post(self, request):

        #Verificar si se añadió un archivo o se realizó una solicitud post

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():

            #Aplicar cambios

            user_form.save()
            profile_form.save()

            return redirect('index')

        #Enviar los formularios como contexto

        context = self.get_context_data(
            user_form=user_form,
            profile_form=profile_form
        )
        return render(request, self.template_name, context)

    #Crear perfil si no lo tiene

    def get(self, request, *args, **kwargs):
        if not Profile.objects.filter(user=request.user).exists():
            Profile.objects.create(user=request.user)

        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

        context = {
            'user_form': user_form,
            'profile_form': profile_form
        }

        return render(request, self.template_name, context)

class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user

class ViewProfile(DetailView):
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Article.objects.filter(user_id=self.object)
        return context

