from atexit import register
from email import message
from multiprocessing import AuthenticationError
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

from accounts.models import user_detail

# Create your views here.


def admn(request):
    
    data = User.objects.all()
    tbl= {
        "details": data
    }
    return render(request,'admn.html',tbl)

def login(request):
    if(request.method == 'POST'):
        username= request.POST['username']
        password= request.POST['password']
        user = auth.authenticate(username=username,password=password)
           
        if user is not None:
            request.session['username']= username
            if user.is_superuser== True:
                return redirect(admn)

            elif user.is_superuser == False:
                auth.login(request, user)
                return redirect('/')
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')  
    else:
        return render(request, 'login.html')  




def register(request):
    if request.method == 'POST':
        f_name = request.POST.get('first_name')
        s_name = request.POST.get('second_name')
        u_name = request.POST.get('user_name')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        email = request.POST.get('email')

        if pass1 == pass2:
            if User.objects.filter(username=u_name).exists():
                messages.info(request,'User name already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'User email already exists')
                return redirect('register')
            else:
                 user = User.objects.create_user(username = u_name, email=email, password=pass1, first_name=f_name,last_name=s_name)
                 user.save();
                 messages.info(request,'User created successfully')
                 return redirect('login')
                 
        else:
            messages.info(request,'password is not match')
            return redirect('register')
            
        return redirect('/')


    else:
       return render(request, 'register.html')

def add(request):
    return render(request, 'add.html') 

def delete(request,id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('admn')

def edit(request,id):
    user = User.objects.get(id=id)
    if request.method == 'POST':
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email    = request.POST['email']
        user.username = request.POST['username']
        #user.password = request.POST['password']
        user.save()
        return redirect('admn')
    tbl={'user':user}
    return render(request,'edit.html',tbl)  



def logout(request):
    
    return render(request,'login.html')  

#def admn(request):
#    search_key = request.GET.get('key') if request.GET.get('key')!=None else ''
 #   if 'user' in request.session:
  #      user_list = User.objects.filter(username_startswith=search_key)
   #     return render(request,'admn.html', {'user':user_list}) 
    #return redirect(login)

    


