from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string 
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.conf import settings
from django.contrib.auth import logout
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from .forms import UserRegistrationForm, UserLoginForm

User = get_user_model()


def homepage(request):
    return render(request, 'homepage.html')

def welcome_email(to_email):
    if not to_email:
        return False
                
    try:
        send_mail(
            subject="خوش آمدید!",
            message="از اینکه عضو سایت ما شدید خوشحالیم 🌹",
            from_email=None,
            recipient_list=[to_email],
        )
    except BadHeaderError:
        return HttpResponse("Invalid header found")
    
    return True

def register(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()

            # email user with activation link
            current_site = get_current_site(request)
            mail_subject = "Activate your account."

            # the message will render what is written in authentication/email_activation/activate_email_message.html
            message = render_to_string('authentication/email_activation/activate_email_message.html', {
                    'user': form.cleaned_data['username'],
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':  default_token_generator.make_token(user),
                })
            to_email = form.cleaned_data['email']
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            messages.success(request, 'Account created successfully. Please check your email to activate your account.')
            return redirect('login')
        else:
            messages.error(request, 'Account creation failed. Please try again.')
        
    return render(request, 'authentication/register.html',{
        'form': form
    })


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active=True
        user.save()
        
        print("🟢 Activation successful for:", user.email)
        welcome_email(user.email)

        return render(request, 'authentication/email_activation/activation_successful.html')
    
    else:
        return render(request, 'authentication/email_activation/activation_unsuccessful.html')


def login(request):
    if request.method == "POST":
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect(request.POST.get('next') or request.get('next') or settings.LOGIN_REDIRECT_URL)
        else:
            form = UserLoginForm(request)
        
        return render(request, 'authentication/login.html', {'form': form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("homepage")
    return render(request, "authentication/logout.html")
