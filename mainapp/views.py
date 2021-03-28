from django.shortcuts import render,HttpResponse,redirect
from mainapp.forms import Create_User, Register_Form, File_Form
from mainapp.models import User_Data,Drive_Data
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.conf import settings 
from django.core.mail import send_mail
# Create your views here.

def register(request):
    flag="success"
    if request.method=="POST":
        form1=Create_User(request.POST)
        form2=Register_Form(request.POST,request.FILES)
        if form1.is_valid() :
            form1.save()
            form2.save()
            return redirect("login")
        else:
            flag="fail"
    form1=Create_User()
    form2=Register_Form()
    context={'form1':form1,'form2':form2,'flag':flag}
    return render(request,"mainapp/index.html",context)

def loginpage(request):
    flag="success"
    if request.method== "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request, username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            flag="fail"
    data={
        'flag':flag
    }
    return render(request,"mainapp/login.html",data)

def logoutuser(request):
    logout(request)   
    return redirect('login')

def filesize(size):
        x = size
        y = 512000
        if x < y:
            value = round(x/1000, 2)
            ext = ' kb'
        elif x < y*1000:
            value = round(x/1000000, 2)
            ext = ' Mb'
        else:
            value = round(x/1000000000, 2)
            ext = ' Gb'
        return str(value)+ext

def upload(request):
    if request.method == "POST":
        email=request.user.email
        filen=request.POST['filename']
        file=request.FILES['files']
        description=request.POST['description']
        filename = file.name
        ext="nothing"
        fsize=filesize(file.size)
        if filename.endswith('.mp3' ):
            ext="audio"
        if filename.endswith('.zip'):
            ext="zip"
        if filename.endswith('.exe'):
            ext="execute"
        if filename.endswith('.jpg'):
            ext="image"
        if filename.endswith('.ppt'):
            ext="present"  
        if filename.endswith('.xls'):
            ext="excel"  
        if filename.endswith('.mp4'):
            ext="video"  
        if filename.endswith('.doc'):
            ext="word"
        if filename.endswith('.pdf'):
            ext="pdf"    
        savedata=Drive_Data(demail=email,description=description,filename=filen,files=file,ext=ext,fsize=fsize)
        print(filename)
        if savedata:
            savedata.save()
            return redirect('dashboard')
        else:
            return HttpResponse("Unsuccessful")
    form=File_Form()
    data={
        'form':form
    }
    return render(request,"mainapp/uploadfile.html",data)

def dashboard(request):
    if request.method == "POST":
        search=request.POST.get("search")
        filesdata=Drive_Data.objects.filter(files__contains=search)
        data={
            'fdata':filesdata
        }
        return render(request,"mainapp/dashboard.html",data)
    filesdata=Drive_Data.objects.filter(demail=request.user.email).order_by('-id')
    data={
        'fdata':filesdata
    }
    return render(request,"mainapp/dashboard.html",data)

def homepage(request):
    return render(request,"mainapp/homepage.html")

def delete(request,id):
    info=Drive_Data.objects.get(id=id)
    info.delete()
    return redirect("dashboard")

def forgot(request):
    flag="success"
    
    if request.method== "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username,password)
        try:
            update=User.objects.get(username=username)
        except:
            update=None
        if update:
            update.set_password(password)
            update.save()
            return redirect('login')
        else:
            flag="fail"
    data={
        'flag':flag
    }
    return render(request,"mainapp/forgotpwd.html",data)

def profile(request):
    tuser=User_Data.objects.get(temail=request.user.email)
    countfiles=Drive_Data.objects.filter(demail=request.user.email).count()
    data={
        'user':tuser,
        'countfiles':countfiles
    }
    return render(request,"mainapp/profile.html",data)

def updateprofile(request):
    if request.method=="POST":
        firstname=request.POST.get("first_name")
        lastname=request.POST.get("last_name")
        mobile_number=request.POST.get("mobile_number")
        gender=request.POST.get("gender")
        update=User.objects.get(email=request.user.email)   
        update.first_name=firstname
        update.last_name=lastname
        update1=User_Data.objects.get(temail=request.user.email)
        update1.mobile_number=mobile_number
        update1.gender=gender
        update.save()
        update1.save()
        return redirect('profile')
    tuser=User_Data.objects.get(temail=request.user.email)
    form1=Create_User()
    form2=Register_Form()
    data={
        'user':tuser,
        'form1':form1,
        'form2':form2
    }
    return render(request,"mainapp/updateprofile.html",data)

def changepic(request):
    flag="success"
    user_profile = User_Data.objects.get(temail=request.user.email)
    if request.method == "POST":
        try:
            user_profile.image = request.FILES['image']
            user_profile.save()
            return redirect('profile')
        except:
            flag="fail"
    form=Register_Form()
    data={
        'form':form,
        'flag':flag
    }
    return render(request,"mainapp/changepic.html",data)


def changepassword(request):
    flag="success"
    if request.method== "POST":
        password=request.POST.get("password")
        try:
            update=User.objects.get(username=request.user.username)
        except:
            update=None
        if update:
            update.set_password(password)
            update.save()
            return redirect('login')
        else:
            flag="fail"
    data={
        'flag':flag
    }
    return   render(request,"mainapp/changepassword.html",data)

def contactus(request):
    if request.method== "POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        msg=request.POST.get("message")
        subject = 'User Contact'
        message ='name=' +name + '   email='+email+'   msg='+msg 
        email_from = settings.EMAIL_HOST_USER 
        recipient_list = ['tushargangurde405@gmail.com']
        try: 
            send_mail( subject, message, email_from, recipient_list )
            return redirect('homepage')
        except:
            return HttpResponse("unsuccessful") 
    return render(request,"mainapp/contactus.html")