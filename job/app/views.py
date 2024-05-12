from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from . models import jobs

# Create your views here.

def home(request):
    user=request.user
    show=request.user.groups.filter(name='superadmin').exists()
    job=jobs.objects.all()
    return render(request,'index.html',{'objs': job, 'showbutton': show,'user':user})
@login_required
def enroll_jobs(request):
    if request.method=='POST':
        jrole=request.POST['jobrole']
        jtitle=request.POST['jobTitle']
        jloc=request.POST['jobLocation']
        jsal=request.POST['salaryPackage']
        jdesc=request.POST['jobDescription']
        jimage=request.FILES.get('jobImage')
        joburl = request.POST.get('url')
        jeduc=request.POST['education']
        jexp=request.POST['experiance']
        enroll_jobs=jobs(jobrole=jrole,title=jtitle,address=jloc,salary=jsal,desc=jdesc,image=jimage,website_url=joburl,education=jeduc,experiance=jexp)
        enroll_jobs.save()
        return redirect('enroll_jobs')
    return render(request,'enroll_jobs.html')
@login_required
def edit(request,id):
    if request.method=="POST":
        obj=jobs.objects.get(id=id)
        obj.jobrole=request.POST['jobrole']
        obj.title=request.POST['jobTitle']
        obj.address=request.POST['jobLocation']
        obj.salary=request.POST['salaryPackage']
        obj.image=request.FILES.get('jobImage')
        obj.desc=request.POST['jobDescription']
        obj.website_url = request.POST.get('url')
        obj.education=request.POST['education']
        obj.experiance=request.POST['experiance']
        obj.save()
        return redirect("/")
    product=jobs.objects.get(id=id)
    return render(request,'edit.html',{'product':product})
@login_required
def search(request):
     if request.method=="POST":
        jobrole=request.POST['jobrole']
        results = jobs.objects.filter(jobrole=jobrole)
        if results:
            return render(request, 'search.html', {'results': results})
        else:
                # Handle case when no jobs found
            return render(request, 'index.html', {'error_message': 'No jobs found'})
     else:
        return redirect('/') 
             
       
@login_required
def delete_product(request,id):
    product=jobs.objects.filter(id=id)
    product.delete()
    return redirect("/")

def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=="POST":
        name1=request.POST["firstName"]
        name2=request.POST["lastName"]
        username=request.POST["username"]
        password1=request.POST["password"]
        password2=request.POST["confirmPassword"]
        email=request.POST['email']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username already exists! Please try another one.")
                return render(request,"register.html")
            elif User.objects.filter(email=email).exists():
                 messages.error(request,"email already exists! Please try another one.")
                 return render(request,"register.html")
            else:
                user=User.objects.create_user(first_name=name1,last_name=name2,username=username,password=password1,email=email)
                user.save()
                messages.success(request,"Registration Successful! You can now login.")
                return redirect('login')                
        else:
            messages.error(request,"Password didn't match with Confirmpassword")
    return render(request,'register.html')
@login_required
def about_us(request):
        return render(request,'about_us.html')
@login_required
def price(request):
        return render(request,'price.html')
@login_required
def learn_more(request):
        job=jobs.objects.all()
        return render(request,'learn_more.html',{'objs':job})
@login_required
def contact(request):
        return render(request,'contact.html')
@login_required
def show(request,id):
      item=jobs.objects.get(id=id)      
      return render(request,'selected_job.html',{'items':item})


def user_login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method=="POST":
        name1=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=name1, password=password)
        if user is not None:
            login(request,user)
            messages.success(request,"welcome "+name1)
            return redirect('/')
        else:
            messages.error(request,"Enter Correct Credentials!")
            return render(request,'login.html')
    return  render(request,'login.html')
@login_required
def user_logout(request):
    logout(request)
    return redirect('login')