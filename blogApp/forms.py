#encoding=utf-8
from django import forms
from .models import Category,Tag

class CommentForms(forms.Form):
    name = forms.CharField(label='称呼',max_length=20,error_messages={'required':'请填写称呼','max_length':'称呼过长！'})
    content = forms.CharField(label='评论', widget=forms.Textarea,max_length=200,error_messages={'required':'请填写评论','max_length':'评论过长！'})

class WriteForm(forms.Form):
    title = forms.CharField(label='标题',max_length=50)
    author = forms.CharField(label='作者',max_length=50)
    content = forms.CharField(label='正文',widget=forms.Textarea)
    category = forms.ModelChoiceField(label='类别',queryset= Category.objects.all())
    #tags = forms.ModelChoiceField(label='标签',queryset= Tag.objects.all())

class InfoForm(forms.Form):
    title = forms.CharField(label='标题',max_length = 50)
    author = forms.CharField(label='发布人',max_length=50)
    content = forms.CharField(label='发布消息',widget=forms.Textarea)

class RegisterForm(forms.Form):
    username = forms.CharField(label = '用户名',max_length=50)
    password = forms.CharField(label='密码',max_length=50,widget=forms.PasswordInput)
    email = forms.EmailField(label='电子邮箱')

class LoginForm(forms.Form):
    username = forms.CharField(label = '用户名',max_length=50,widget=forms.TextInput(attrs={'placeholder': '请输入用户名'}))
    password = forms.CharField(label='密码',max_length=50,widget=forms.PasswordInput)




