from django import forms
from . import models
from rooms import models as room_models


class LoginForm(forms.Form):

    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        print(self.cleaned_data)
        # print(email, password)
        try:
            user = models.User.objects.get(email=email)
            print(user)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("email", forms.ValidationError("User does not exist"))


class SignUpForm(forms.Form):

    email = forms.EmailField(label="E-mail")
    first_name = forms.CharField(max_length=30, label="이름")
    last_name = forms.CharField(max_length=50, label="성")
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "비밀번호"},
        ),
        label="비밀번호",
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "비밀번호 확인"}), label="비밀번호확인"
    )
    nation = forms.ModelChoiceField(
        required=False, queryset=room_models.Nation.objects.all(), label="국가"
    )
    brand = forms.ModelChoiceField(
        required=False, queryset=room_models.Brand.objects.all(), label="브랜드"
    )
    category = forms.ModelChoiceField(
        required=False, queryset=room_models.Category.objects.all(), label="카테고리"
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("같은 계정의 사용자가 이미 있습니다.")
        except models.User.DoesNotExist:
            return email

    def clean_password1(
        self,
    ):  # if clean_password(self) , then it could not work cleaning password1 only password
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password == password1:
            return password
        else:
            raise forms.ValidationError("비밀번호를 확인해보세요.")

    def save(self):
        email = self.cleaned_data.get("email")
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        nation = self.cleaned_data.get("nation")
        brand = self.cleaned_data.get("brand")
        category = self.cleaned_data.get("category")
        print(email, nation, brand, category)
        user = models.User.objects.create_user(email, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.nation = nation
        user.brand = brand
        user.categories = category
        user.save()
