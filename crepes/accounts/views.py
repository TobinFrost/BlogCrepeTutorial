from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from django.views.generic import UpdateView

from accounts.forms import SignUpForm, ProfileForm
from accounts.models import Profile
from blog.views import ListeArticleView, liste_personne


def listeRegisteredUser(request):
    users = User.objects.order_by("username")
    return render(request, 'accounts/list.html', locals())


@login_required
def home(request):
    return render(request, 'accounts/home.html')


class UserRegistrationView(CreateView):
    model = User
    template_name = 'accounts/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy(listeRegisteredUser)

    def form_valid(self, form):
        self.object = form.save()
        self.object.refresh_from_db()  # load the profile instance created by the signal
        self.object.profile.birth_date = form.cleaned_data.get('birth_date')
        self.object.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)

        return HttpResponseRedirect(self.get_success_url())

class UserProfileUpdate(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/update.html'
    success_url = reverse_lazy(home)

