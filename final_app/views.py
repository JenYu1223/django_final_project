from django.shortcuts import render, redirect
from datetime import datetime
from .forms import LoginForm, RegistrationForm
from django.contrib.auth import authenticate, login
from .models import UserProfile
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import PreferencesForm
from django.http import HttpResponse
# Create your views here.

def homepage(request):  # TODO
    return render(request, 'home.html')

def login_page(request):  # TODO
    return render(request, 'login.html')

def register_page(request):  # TODO
    return render(request, 'register.html')


def login_view(request):
    login_form = LoginForm()  # 創建登錄表單的實例

    if request.method == 'POST':  # 如果請求方法是 POST
        if 'login' in request.POST:  # 如果 POST 請求中包含 'login'
            login_form = LoginForm(request.POST)  # 用 POST 數據填充登錄表單
            if login_form.is_valid():  # 如果登錄表單有效
                email = login_form.cleaned_data.get('email')  # 獲取已清理的 email
                password = login_form.cleaned_data.get('password')  # 獲取已清理的 password
                user = authenticate(request, username=email, password=password)  # 認證用戶
                if user is not None:  # 如果用戶存在
                    login(request, user)
                    print("登入成功")  # 登錄用戶
                    return redirect('/')  # 重定向到主頁
                else:
                    print('Login failed: Invalid email or password')  # 打印錯誤信息
                    print(f"Email: {email}, Password: {password}")  # 打印 email 和 password
                    print(f"User found: {user}")  # 打印找到的用戶信息

    return render(request, 'login.html', {'login_form': login_form})  # 渲染登錄頁面，並傳遞表單



def register_view(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            try:
                user = register_form.save(commit=True)
                user.set_password(register_form.cleaned_data.get('password'))
                user.save()
                
                # 確保只有在不存在 UserProfile 時才創建
                if not UserProfile.objects.filter(user=user).exists():
                    UserProfile.objects.create(user=user)
                
                # login(request, user)  # 自動登錄用戶
                return redirect('/')
            except IntegrityError as e:
                print('Registration failed:', str(e))
                # 刪除已創建的用戶以避免不一致
                # user.delete()
        else:
            print('Registration failed:', register_form.errors)
    else:
        register_form = RegistrationForm()
    
    return render(request, 'register.html', {'register_form': register_form})


@login_required
def suggest_course(request):
    return render(request, 'suggest_course.html')


@login_required
def preferences(request):
    if request.method == 'POST':
        default_options = request.POST.getlist('default_options')
        user_defined = request.POST.get('user_defined', '')

        if not default_options and not user_defined:
            error_message = "請選擇至少一個課程種類或輸入其他課程名稱。"
            print("請選擇至少一個課程種類或輸入其他課程名稱")
            return render(request, 'preferences.html', {'error_message': error_message})

        preferences = {
            'default_options': default_options,
            'user_defined': user_defined
        }

        # 更新用戶的 UserProfile
        user_profile, created = UserProfile.objects.get_or_create(user=request.user)
        user_profile.preferences = preferences
        user_profile.save()
        print("Success")
        return HttpResponse(f'Preferences updated: {preferences}')
    else:
        print("GET request & Form Failed")
    
    return render(request, 'preferences.html')


# def preferences(request):
#     return render(request, 'preferences.html')


# @login_required
# def preferences(request):
#     if request.method == 'POST':
#         form = PreferencesForm(request.POST)
        
#         if form.is_valid():
#             default_options = form.cleaned_data['default_options']
#             user_defined = form.cleaned_data['user_defined']
            
#             preferences = {
#                 'default_options': default_options,
#                 'user_defined': user_defined
#             }
            
#             # 更新用戶的 UserProfile
#             user_profile, created = UserProfile.objects.get_or_create(user=request.user)
#             user_profile.preferences = preferences
#             user_profile.save()
#             print("Success")
#             return HttpResponse(f'Preferences updated: {preferences}')
#         else:
#             # 打印表單的錯誤信息
#             print("Form errors:", form.errors)
#             print("Validation failed")
#     else:
#         form = PreferencesForm()
    
#     return render(request, 'preferences.html', {'form': form})


# @login_required
# def item_view(request):
#     if request.method == 'POST':
#         print("GET POST")
#         math_form = MathForm(request.POST, prefix='math')
#         chinese_form = ChineseForm(request.POST, prefix='chinese')
        
#         if math_form.is_valid() and chinese_form.is_valid():
#             math_sub_items = math_form.cleaned_data['sub_items']
#             math_custom_input = math_form.cleaned_data['custom_input']
#             chinese_sub_items = chinese_form.cleaned_data['sub_items']
#             chinese_custom_input = chinese_form.cleaned_data['custom_input']
            
#             preferences = {
#                 'math': {
#                     'sub_items': math_sub_items,
#                     'custom_input': math_custom_input,
#                 },
#                 'chinese': {
#                     'sub_items': chinese_sub_items,
#                     'custom_input': chinese_custom_input,
#                 }
#             }
            
#             # 更新用戶的 UserProfile
#             user_profile, created = UserProfile.objects.get_or_create(user=request.user)
#             user_profile.preferences = preferences
#             user_profile.save()
#             print("Success")
#             return HttpResponse(f'Preferences updated: {preferences}')
#         else:
#             # 打印表單的錯誤信息
#             print("Math form errors:", math_form.errors)
#             print("Chinese form errors:", chinese_form.errors)
#             print("Validation failed")
#     else:
#         print("GET request")
    
#     math_form = MathForm(prefix='math')
#     chinese_form = ChineseForm(prefix='chinese')
#     return render(request, 'item_form.html', {'math_form': math_form, 'chinese_form': chinese_form})