from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views.generic import FormView

from bpsc.common import SCUserCreationForm


class UserRegistrationView(FormView):
    template_name = 'user_registration.html'
    form_class = SCUserCreationForm
    success_url = reverse_lazy('home')
