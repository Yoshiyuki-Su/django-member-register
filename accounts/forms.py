from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm
)
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label  # placeholderにフィールドのラベルを入れる


class UserCreateForm(UserCreationForm):
    """ユーザー登録用フォーム"""

    class Meta:
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_email(self):
        email = self.cleaned_data['email']
        # 仮登録をしたけど本登録を忘れていて、アクティベーションリンクの期限を超えた場合や、メールアドレスの入力間違いなどがあって、自分のメールアドレスが仮登録済みの場合もあり得ます。
        # その際はもう一度会員登録をするはずですが、「このメールアドレスは使われています」と表示されて登録ができないと良くありません。
        # そこで、clean_email()メソッドは同じメールアドレスで仮登録段階のアカウントを消去しています。
        User.objects.filter(email=email, is_active=False).delete()
        return email


class UserUpdateForm(forms.ModelForm):
    """ユーザー情報更新フォーム"""

    class Meta:
        model = User
        fields = ('last_name', 'first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
