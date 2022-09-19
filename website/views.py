from django.shortcuts import render, redirect
from test_site.settings import EMAIL_HOST_USER
from website.forms import ContactForm, PasswordResetForm
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth.forms import SetPasswordForm

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        modified_request = request.POST.copy()
        modified_request['name'] = 'Unknown'
        form = ContactForm(modified_request)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your ticket submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, "Your ticket didn't submitted")
    form = ContactForm()
    return render(request, 'website/contact.html', {'form':form})

def password_reset_view(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data.get('email')
            users = User.objects.filter(Q(email=mail))
            if users.exists():
                for user in users:
                    subject="reset password",
                    message="passwords/template_email.txt",
                    c = {
                    'username':user.username,
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
                    email = render_to_string(message, c)
                    try:				
                        send_mail(
                            subject,
                            email,
                            from_email=EMAIL_HOST_USER,
                            recipient_list=[mail],
                            fail_silently=False
                        )
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect('/password_reset/done')
            else:
                messages.add_message(request, messages.ERROR, "No such email in database.")

    form = PasswordResetForm()
    return render(request, 'passwords/password_reset.html', {'form':form})


def password_reset_done_view(request):
    return render(request, 'passwords/password_reset_done.html')

def password_reset_confirm_view(request, username, uidb64, token):
    user = User.objects.get(username=username)
    print (user)
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            return redirect('/password_reset/complete')
        else:
            messages.add_message(request, messages.ERROR, "Your password is not as per password policy.")
    form = SetPasswordForm(user)
    context = {'form':form, 'username':username, 'uidb64':uidb64, 'token':token}
    return render(request, 'passwords/password_reset_confirm.html', context)

def password_reset_complete_view(request):
    return render(request, 'passwords/password_reset_complete.html')


