from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, UpdateView
from .forms import ProfileForm
from .models import Profile


# @login_required
# def profile(request):
#     return render(request, 'accounts/profile.html')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'


profile = ProfileView.as_view()


@login_required
def profile_edit(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = None
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        
        if form.is_valid:
            form.save(commit=False)
            profile.user = request.user
            profile.save()

            return redirect('profile')
        
        else:
            form = ProfileForm(instance=profile)
        return render(request, 'accounts/profile_form.html',{
            'form': form,
        })
