# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from django.shortcuts import render

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from braces.views import LoginRequiredMixin

# from .forms import UserForm
# from .models import User


def index(request):
    data_from_django = "hi there this is django"
    context = {'data_from_django': data_from_django}
    return render(request, 'base.html', context)
#
# class UserDetailView(LoginRequiredMixin, DetailView):
#     model = User
#     # These next two lines tell the view to index lookups by username
#     slug_field = "username"
#     slug_url_kwarg = "username"
#
#
# class UserRedirectView(LoginRequiredMixin, RedirectView):
#     permanent = False
#
#     def get_redirect_url(self):
#         return reverse("users:detail",
#                        kwargs={"username": self.request.user.username})
#
#
# class UserUpdateView(LoginRequiredMixin, UpdateView):
#
#     form_class = UserForm
#
#     # we already imported User in the view code above, remember?
#     model = User
#
#     # send the user back to their own page after a successful update
#     def get_success_url(self):
#         return reverse("users:detail",
#                        kwargs={"username": self.request.user.username})
#
#     def get_object(self):
#         # Only get the User record for the user making the request
#         return User.objects.get(username=self.request.user.username)
#
#
# class UserListView(LoginRequiredMixin, ListView):
#     model = User
#     # These next two lines tell the view to index lookups by username
#     slug_field = "username"
#     slug_url_kwarg = "username"
