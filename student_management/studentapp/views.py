from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,logout,login
from.models import Teachernew,Studentnew,user
# Create your views here.
def home(request):
    return render(request,"index.html")
def register(request):
    if request.method=="POST":
        FIRSTNAME=request.POST["FIRSTNAME"]
        LASTNAME=request.POST['LASTNAME']
        EMAIL=request.POST["EMAIL"]
        ADDRESS=request.POST['ADDRESS']
        PHONE_NUM=request.POST['PHONE_NUM']
        USERNAME=request.POST['USERNAME']
        PASSWORD=request.POST['PASSWORD']
        
        new_user=user.objects.create_user(first_name=FIRSTNAME,last_name=LASTNAME,email=EMAIL,username=USERNAME,password=PASSWORD,usertype='student',is_active=False)
        new_user.save()
        # first_name data base le same
        
        x=Studentnew.objects.create(student_id=new_user,address=ADDRESS,phone_num=PHONE_NUM)
        x.save()
        # student_id model
        return redirect(logins)
    else:
        return render(request,"student_register.html")


def logins(request):
    if request.method=="POST":
        USERNAME=request.POST['USERNAME']
        PASSWORD=request.POST['PASSWORD']
        print(USERNAME,PASSWORD)
        userpass=authenticate(request,username=USERNAME,password=PASSWORD)
        if userpass is not None and userpass.is_superuser==1:
            return redirect('admin')
        elif userpass is not None and userpass.is_staff==1:
            login(request,userpass)
            request.session['teach_id']=userpass.id 
            return redirect("teacherhome")
        elif userpass is not None and userpass.is_active==1:
            login(request,userpass)
            request.session['stud_id']=userpass.id 
            return redirect("studenthome")
        else:
            return HttpResponse("invalid") 
    else:
        return render(request,"login.html")       
    

def teacher_register(request):
    if request.method=="POST":
        FIRSTNAME=request.POST["FIRSTNAME"]
        LASTNAME=request.POST['LASTNAME']
     
        EMAIL=request.POST["EMAIL"]
        ADDRESS=request.POST['ADDRESS']
        PHONE_NUM=request.POST['PHONE_NUM']

        USERNAME=request.POST['USERNAME']
        PASSWORD=request.POST['PASSWORD']
        new_user=user.objects.create_user(first_name=FIRSTNAME,last_name=LASTNAME,email=EMAIL,username=USERNAME,password=PASSWORD,usertype='teacher',is_active=True,is_staff=True)
        new_user.save()

        cust= Teachernew.objects.create(teacher_id=new_user,address=ADDRESS,phone_number=PHONE_NUM)
        cust.save()
        return redirect(logins)
    else:
        return render(request,"teacher_register.html")


def admin(request):
    return render(request,"admin.html")
def teacherhome(request):
    return render(request,"teacherhome.html")
def studenthome(request):
    return render(request,"studenthome.html")


def teacher_view(request):
    x=Teachernew.objects.all()
    return render(request,"teacher_view.html",{"data":x})

def view_student(request):
    x=Studentnew.objects.all()
    return render(request,"student_view.html",{"data":x})
def approve(request,id):
    stud=Studentnew.objects.get(id=id)
    stud.student_id.is_active=True
    stud.student_id.save()
    return redirect("view_student")
def delete_student(request,id):
    stud=Studentnew.objects.get(id=id)
    user_id=stud.student_id.id
    stud.delete()
    user.objects.filter(id=user_id).delete()
    return redirect("view_student")



def delete_teacher(request,id):
    teach=Teachernew.objects.get(id=id)
    user_id=teach.teacher_id.id
    user.objects.filter(id=user_id).delete()
    return redirect("teacher_view")
def teacher_view_student(request):
    x=Studentnew.objects.all()
    return render(request,"teacher_view_student.html",{"data":x})
def student_view_teacher(request):
    x=Teachernew.objects.all()
    return render(request,"student_view_teacher.html",{"data":x}) 

def edit_teacher(request):
    teach=request.session.get('teach_id')
    teacher=Teachernew.objects.get(teacher_id_id=teach)
    use=user.objects.get(id=teach)
    return render(request,"update_teach.html",{"view":teacher,"data":use})

def update_teacher(request,id):
    if request.method == "POST":
        tea=Teachernew.objects.get(id=id)
        uid=tea.teacher_id_id
        print(uid)
        use=user.objects.get(id=uid)
        use.first_name=request.POST["first_name"]
        use.last_name=request.POST["last_name"]
        use.email=request.POST['email']
        use.save()
        tea.address=request.POST["address"]
        tea.phone_number=request.POST["phone_num"]
        tea.save()
        return redirect("teacherhome")
    

def edit_student(request):    
    stud=request.session.get('stud_id')
    student=Studentnew.objects.get(student_id_id=stud)
    usd=user.objects.get(id=stud)
    return render(request,"update_stud.html",{"view":student,"data":usd})
    
def update_student(request,id):
    if request.method == "POST":
        stu=Studentnew.objects.get(id=id)
        sid=stu.student_id_id
        use=user.objects.get(id=sid)
        use.first_name=request.POST["first_name"]
        use.last_name=request.POST["last_name"]
        use.email=request.POST['email']
        use.save()
        stu.address=request.POST["address"]
        stu.phone_number=request.POST["phone_num"]
        stu.save()
        return redirect("studenthome")
    
    
def logouts(request):
    logout(request)
    return redirect("home")
def new(request):
    return render(request,"index.html")














    

        
