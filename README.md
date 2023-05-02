# To Do List using Django



## How To

### Add new app to project

```bash
python manage.py startapp tdl
```


### Hello World

```mysite/tdl/views.py```
```python
# function တစ်ခု ကြေညာမယ်
# ်function name ကို အဆင်ပြေတာတစ်ခုပေးမယ်။​ ဉပမာ index
def index():
    return "Hello World"

# function မှာ parameter တစ်ခု ထည့်ပေးဖို့လိုတယ်။​ဒါက Django က တောင်းဆိုထားလို့။
# parameter နာမည်က request 
def index(request):
    return "Hello World"

# function က return မှာ String ပြန်လို့မရပဲ​ Http Response ပြန်ရမယ်။
def index(request):
    return HttpResponse("Hello World.")

# HttpResonse ဆိုတဲ့ function ကို django.http ဆိုတဲ့ module ထဲက import လုပ်ရမယ်။
from django.http import HttpResponse

# ဒီတော့ views.py ရဲံ ကုတ်အပြည့်အစုံက ဒါမျိုးဖြစ်သွားမယ်
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Hello World")

# ဒီ​ ကုတ် (၄)​ ကြောင်းကို ကြည့်ရင် index ဆိုတဲ့ function တစ်ခု ကြေညာထားတာလို့ပဲ နားလည်ရင် ရပြီ။
# ဒီ ဖိုင်ကို run ကြည့်ရင်လည်း ဘာ result မှ ပြမှာ မဟုတ်သေးဘူး
# ဒါက function ကြေညာထားရုံပဲ ရှိသေးတယ်၊​ function call မခေါ်သေးဘူး။
```

Hello World လို့ ပေါ်မယ့် function တစ်ခုတော့ ရေးပြီးသွားပြီ။ အဲ့ function ကို ဘယ်လိုခေါ်မလဲ?

ဒီအတွက် ```urls.py``` ဖိုင်မှာ ရေးရမယ်။ ```mysite/tdl``` folder မှာ ```urls.py``` ဖိုင် မရှိသေးရင် ဖိုင်အသစ်ဆောက်လိုက်။

```mysite/tdl/urls.py```
```py
# ဒီဖိုင်မှာ array တစ်ခုပဲ ရေးဖို့လိုမယ်
urlpatterns = [
    path("/hello", views.index),
]
# ဆိုလိုတာက /hello ဆိုပြီး browser မှာ ရေးလိုက်ရင် views.py မှာ ရေးထားတဲ့ index function ကို call ခေါ်မယ်
# path function ကို django.urls module က import လုပ်မယ်။
from django.urls import path
# views.py ထဲက function တွေကိုလည်း import လုပ်ရမယ်။
from . import views
# ဆိုတော့ကာ urls.py ဖိုင်ရဲ့ ဖိုင်နယ်ကုတ်က ဒါမျိုး ဖြစ်မယ်။
from django.urls import path

from . import views

urlpatterns = [
    path("/hello", views.index),
]
```