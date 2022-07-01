import email
from django.http import HttpResponse
from django.shortcuts import render
from .models import User, Profile
from .forms import RegistrationForm, LoginForm
from django.contrib import messages, auth

# Email configurations
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template import Context
from django.template.loader import get_template, render_to_string
from django.utils.encoding import force_bytes,force_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
# TOKEN 
from accounts.token import account_activation_token

def feedback(request):
    pass

""" REGISTER USER """
def register(request): 
    print('register page')
    if request.method == 'POST' :     
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            
            # GETTING USER INPUT 
            user.email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            user.set_password(form.cleaned_data['password'])
            user.is_active = False        

            # RAISING VALIDATORS TO CHECK THE DB    
            if User.objects.filter(email = user.email).exists():
                print('email exist')
                messages.warning(request, 'Email Already exists, Please use a different email')
                return redirect('register')
            if password != password2:
                    print('donot match')
                    messages.error(request, 'Password do not match, Please make sure it matches')    
                    return redirect('register') 

            # SAVING TO DB 
            print('success')           
            user.save()

            """ SENT AN EMAIL TO USER """
            current_site = get_current_site(request)
            mail_subject = 'Activate Your Account'            
            html_message = render_to_string('accounts/email/account_activation_email.html', {
                'user': user,
                
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':account_activation_token.make_token(user)
            })
            to = user.email
            send_email = EmailMessage(mail_subject, html_message, to=[to])
            send_email.content_subtype = "html"
            send_email.send()
            messages.success(request, 'Registration successfully')
            return HttpResponse('register successfully and activation send to your email')
        else: 
            print('bad')
            messages.error(request, 'Failed to register')   
            return redirect('register')
    else:
       form = RegistrationForm()         

    context = {
        'form':form
    }   

    return render (request, 'accounts/user/register.html',context)   



""" ACCOUNT ACTIVATION """
def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk = uid)
    except(TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None    
    if user is not None and account_activation_token.check_token(user,token):
        user.is_active = True        
        user.save()
        auth.login(request,user)
        messages.success(request, 'Activation successfully')
        return redirect('dashboard')
    else:
        return HttpResponse('INVALID TOKEN ACTIVATION')
    

''' USER DASHBOARD'''
@login_required
def dashboard(request):    
    return render(request, 'accounts/user/dashboard.html')


""" ACCOUNT LOGIN """
def login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)    
        
        if form.is_valid():
            user = form
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(form=form,email=email, password=password)                                  
            
        if user is not None:            
            auth.login(request,user)
            messages.success(request, 'You are logged in')
            print('success')
            return HttpResponse('LOGIN SUCCESS')
        else:
            form = LoginForm()
            
            messages.error(request, 'Unable to login, Check your email and password')
            return redirect('login')        
    else:
        form = LoginForm()
    context = {
        'form':form
    }    
    return render(request,'accounts/user/login.html',context)