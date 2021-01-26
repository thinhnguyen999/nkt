from django.shortcuts import render, redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm  
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_protect, csrf_exempt
from .forms import *
from .models import *
from django.http import Http404
from django.contrib import messages
import json
import requests
from django.http.response import JsonResponse

@login_required(login_url='signin')
def base_main(request):
    return render(request, 'information_nkt/base_main.html',{'user':request.user})

# ---------- LƯU THÔNG TIN NKT ----------
@login_required(login_url='signin')
def info_NKT(request):
    actual_info = information_NKT()
    # ----- Phân quyền user ---------
    qs_permission = get_object_or_404(Permission,user_rel=request.user.id)
    if qs_permission.can_add or qs_permission.can_view: # ----- Kiểm tra nếu user có quyền thì mới được truy cập vào và thực hiện
        if request.method == 'POST':
            registerForm = RegisterForm(request.POST, instance=actual_info)
            if registerForm.is_valid():
                # registerForm.save()
                # return redirect('/info_NKT/')
                return render(request, 'information_nkt/index.html',{'form_nhap':registerForm})
            else:
                print(registerForm.errors)
        else:
            registerForm = RegisterForm()
            ds_tinh = TinhThanh.objects.all()
            ds_quan= QuanHuyen.objects.all()
            ds_xa = PhuongXa.objects.all()
            return render(request, 'information_nkt/index.html',{'form_nhap':registerForm, 'ds_tinh':ds_tinh,'ds_quan':ds_quan,'ds_xa':ds_xa})
    else:                                   # ----- Còn ngược lại thì thông báo lỗi 
        return render(request, 'information_nkt/404.html')
    return render(request, 'information_nkt/index.html',{'form_nhap':registerForm})
def insertKhuyetTatForm(request):
    actual_info = KhuyetTat()
    resp = {
        "status_code":200,
        "code" : 200,
        "msg":  "success"
    }
    if request.method == 'POST':
        kt_form = KhuyetTatForm(request.POST, instance=actual_info)
        if kt_form.is_valid():
            try:
                kt_form.save()
            except Exception as err:
                resp['code'] = 403
                resp['msg'] = str(err)
    else:
        resp['code'] = 403
        resp['msg'] = "Not allow GET"
    return JsonResponse(resp)

def insertNhuCauForm(request):
    actual_info = NhuCau()
    resp = {
        "status_code":200,
        "code" : 200,
        "msg":  "success"
    }
    if request.method == 'POST':
        kt_form = NhuCauForm(request.POST, instance=actual_info)
        if kt_form.is_valid():
            try:
                kt_form.save()
            except Exception as err:
                resp['code'] = 403
                resp['msg'] = str(err)
    else:
        resp['code'] = 403
        resp['msg'] = "Not allow GET"
    return JsonResponse(resp)

def insertNhuCauDNForm(request):
    actual_info = NhuCauDaNhan()
    resp = {
        "status_code":200,
        "code" : 200,
        "msg":  "success"
    }
    if request.method == 'POST':
        kt_form = NhuCauDaNhanForm(request.POST, instance=actual_info)
        if kt_form.is_valid():
            try:
                kt_form.save()
            except Exception as err:
                resp['code'] = 403
                resp['msg'] = str(err)
    else:
        resp['code'] = 403
        resp['msg'] = "Not allow GET"
    return JsonResponse(resp)
def insertTab1(request):
    resp = {
        "code" : 200,
        "msg":  "success"
    }
    actual_info = information_NKT()
    qs_permission = get_object_or_404(Permission,user_rel=request.user.id)
    if qs_permission.can_add or qs_permission.can_view: # ----- Kiểm tra nếu user có quyền thì mới được truy cập vào và thực hiện
        if request.method == 'POST':
            registerForm = RegisterForm(request.POST, instance=actual_info)
            if registerForm.is_valid():
                registerForm.save()
            else:
                resp['code'] = 403
                resp['msg'] = str(registerForm.errors)
                
        else:
            resp['code'] = 403
            resp['msg'] = "Not allow GET"
    else:    
        resp['code'] = 403
        resp['msg'] = "Permission deny"
    return JsonResponse(resp)
@csrf_exempt 
def removeTTNKT(request):
    resp = {
        "code" : 200,
        "msg":  "success"
    }
    actual_info = information_NKT()
    qs_permission = get_object_or_404(Permission,user_rel=request.user.id)
    if qs_permission.can_add or qs_permission.can_view: # ----- Kiểm tra nếu user có quyền thì mới được truy cập vào và thực hiện
        if request.method == 'POST':
            thongtin = json.loads(request.body)
            sodinhdanh = thongtin.get("sodinhdanh")
            try:
                information_NKT.objects.filter(so_dinh_danh=sodinhdanh).delete()
            except:
                pass
            try:
                KhuyetTat.objects.filter(so_dinh_danh=sodinhdanh).delete()
            except:
                pass
            try:
                NhuCau.objects.filter(so_dinh_danh=sodinhdanh).delete()
            except:
                pass
            try:
                NhuCauDaNhan.objects.filter(so_dinh_danh=sodinhdanh).delete()
            except:
                pass
        else:
            resp['code'] = 403
            resp['msg'] = "Not allow GET"
    else:    
        resp['code'] = 403
        resp['msg'] = "Permission deny"
    return JsonResponse(resp)
# ---------- DANH SÁCH NKT ----------
def ds_NKT(request):
    qs_permission = get_object_or_404(Permission,user_rel=request.user.id)
    if qs_permission.can_view:
        if request.method == 'GET':
            info = information_NKT.objects.all()

            context = {
                'info': info,
                'error': '',
            }
        else:
            print("POST")
        return render(request,'information_nkt/ds_NKT.html', context)
    else:
        return render(request, 'information_nkt/404.html')
# ---------- FORM ĐĂNG NHẬP ----------
def signin(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            #----------- Mã capcha ------------
            captcha_token=request.POST.get("g-recaptcha-response")
            cap_url = 'https://www.google.com/recaptcha/api/siteverify'
            cap_secret = '6LeTnzIaAAAAAIj5Pa_dItGjjHLmunleaRTBrQf7'
            cap_data={"secret":cap_secret,"response":captcha_token}
            cap_server_response=requests.post(url=cap_url,data=cap_data)
            cap_json=json.loads(cap_server_response.text)
            if cap_json['success']==False:
                messages.error(request,"Bạn chưa xác nhận CAPCHA !")
                return HttpResponseRedirect("/")
                

            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('base_main')
            
            else:
                context = {
                    'form': forms,
                    'error': 'Tài khoản hoặc mật khẩu không đúng    ! Mời kiểm tra lại.'
                }
                return render(request, 'account/signin.html', context)
    else:
        context = {
            'form': forms,
            'error': ''
        }
        return render(request, 'account/signin.html', context)
# ---------- FORM ĐĂNG KÝ ----------
def signup(request):
    forms = RegistrationForm()
    if request.method == 'POST':
        forms = RegistrationForm(request.POST)
        if forms.is_valid():
            firstname = forms.cleaned_data['firstname']
            lastname = forms.cleaned_data['lastname']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            confirm_password = forms.cleaned_data['confirm_password']

            if password == confirm_password:
                try:
                    if User.objects.filter(email=email).exists():
                        context = {
                            'form': forms,
                            'error1': 'EMAIL đã tồn tại !', 
                        }
                        return render(request, 'account/signup.html', context)
                    else:
                        # ----- Phân quyền tự động cho user đăng kí tài khoản ---------
                        Permission(user_rel=User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname),
                        can_view=True, can_add=True, can_edit=True, can_delete=False, can_report=False, can_manage_user=False).save()
                        return redirect('signin')
                except:
                    context = {
                        'form': forms,
                        'error': 'USERNAME đã tồn tại !', 
                    }
                    return render(request, 'account/signup.html', context)
    context = {
        'form': forms
    }
    return render(request, 'account/signup.html', context)
# ---------- FORM LOGOUT ----------
def signout(request):
    logout(request)
    return redirect('signin')
# ---------- BÁO CÁO BIỂU ĐỒ DANH SÁCH ----------
def report(request):
    qs_permission = get_object_or_404(Permission,user_rel=request.user.id)
    if qs_permission.can_view:
        if request.method == 'GET':
            report = information_NKT.objects.all()

            context = {
                'report': report,
                'error': '',
            }
        else:
            print("POST")
        return render(request,'information_nkt/report_ds.html', context)
    else:
        return render(request, 'information_nkt/404.html')
# ---------- BÁO CÁO BIỂU ĐỒ THEO CHART ----------
def report_bd(request):
    qs_permission = get_object_or_404(Permission,user_rel=request.user.id)
    if qs_permission.can_delete:
        return render(request,'information_nkt/report_bd.html')
    else:
        return render(request,'information_nkt/404.html')
# --------------XEM THÔNG TIN CHI TIẾT NKT ----------------------
def view_NKT(request):
    if request.method == 'GET':
        view = information_NKT.objects.all()
        context = {
            'view': view,
            'error': '',
        }
    else:
        print("POST")
    return render(request,'information_nkt/ds_NKT.html', context)
# ------------------- XÓA THÔNG TIN NKT -------------------------
def ds_NKT_delete(request):
    if request.method == "GET":
        id = request.GET['id']
        delete = information_NKT.objects.get(id=id).delete()
        context = {
            'delete': delete,
            'error': '',
        }
    else:
        print("POST")
    return render(request,'information_nkt/ds_NKT.html', context)
# ------------------- FORM SỬA THÔNG TIN NKT -------------------------
def repair_info_nkt(request,pk=None):
    if pk:
        actual_info = information_NKT.objects.get(pk=pk)
    else:
        actual_info = information_NKT()
    registerForm1 = RegisterForm( instance=actual_info)
    # ----- Phân quyền user ---------
    qs_permission = get_object_or_404(Permission,user_rel=request.user.id)
    if qs_permission.can_add or qs_permission.can_view: # ----- Kiểm tra nếu user có quyền thì mới được truy cập vào và thực hiện
        if request.method == 'POST':
            registerForm1 = RegisterForm(request.POST, instance=actual_info)
            if registerForm1.is_valid():
                registerForm1.save()
                # print(registerForm1.cleaned_data)
                return redirect('/ds_NKT/')
                # return render(request, 'information_nkt/ds_NKT.html',{'form_sua':registerForm1,'pk':pk})
            else:
                print(registerForm1)

    else:                                
        return render(request, 'information_nkt/404.html')

    return render(request, 'information_nkt/repair_info_nkt.html',{'form_sua':registerForm1,'pk':pk})


# ------------------- PHÊ DUYỆT THÔNG TIN NKT -------------------------
def phe_duyet_thong_tin(request):
    qs_permission = get_object_or_404(Permission,user_rel=request.user.id)
    if qs_permission.can_delete:
        return render(request,'information_nkt/phe_duyet.html')
    else:
        return render(request,'information_nkt/404.html')





