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

အိုကေ ဒီ (၂)​ဖိုင် ရေးပြီးသွားရင် App အပိုင်းမှာ ပြီးပြီ။

ပရောဂျက်နဲ့ app နဲ့ ကို ချိတ်မယ်။

project urls file ဖြစ်တဲ့ ```mysite/urls.py``` မှာ tdl app ကို ထည့်မယ်။

```python
# ဒါက နဂို ရှိတဲ့ url patterns array
urlpatterns = [
    path("admin/", admin.site.urls),
]

# tdl app က url file ကိုထည့်မယ်။
urlpatterns = [
    # tdl လို url မှာ ပါလာရင် tdl folder ထဲက urls.py ကို run ပါ
    path("tdl/", include("tdl.urls")),
    path("admin/", admin.site.urls),
]

# ဒီမှာ include ဆိုတဲ့ function ပါတယ်။ ဒီ include ဆိုတဲ့ function ကို​ django.urls ဆိုတဲ့ module ထဲက import လုပ်ရမယ်။

from django.urls import include

# ဆိုတော့ ဖိုင်နယ်ကုတ်က ဒါမျိုး ဖြစ်မယ်။
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("tdl/", include("tdl.urls")),
    path("admin/", admin.site.urls),
]
```

အချိန် ```python manage.py runserver 0.0.0.0:8080``` လို့ run ပြီး
broswer မှာ 127.0.0.1:8080/tdl/hello လို့ ရိုက်ထည့်လိုက်ရင် "Hello World" လို့ ပေါ်လာပါလိမ့်မယ်။

### Database 

```
python manage.py migrate
```


```log
msd@MSDs-Mac-mini mysite % python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

### Creating Model

Model ဆိုတာက app မှာ သုံးမယ့် data structure ပါပဲ။
ဆိုပါဆို့ အခု tdl (to do list) app မှာ ဆိုရင် ဘယ်လို data မျိုးကို သိမ်ထားမလဲ?
လုပ်စရာရှိတဲ့ အလုပ် (task) ကို သိမ်းကြမယ်။

task တစ်ခုမှာ ဘာတွေသိမ်းကြမလဲ?
- task name  : string ( အလုပ် နာမည် ဉပမာ ။​ စျေးဝယ်ထွက်ရန် )
- task status : boolean ( အလုပ် လက်ရှိ အခြေအနေ ။​ မပြီးသေးဘူး (false) / ပြီးပြီ (true) )

ဒီ (၂)​ခု သိမ်းထာရင် ရပြီ။

အိုကေ Django မှာ ဒါကို ဘယ်လို သိမ်းမလဲ။

```mysite/tdl/models.py``` ဖိုင်မှာ ရေးရမယ်။

```python
from django.db import models
# class တစ်ခု ဆောက်မယ်။
class Task():
    name = models.TextField()
    status = models.BooleanField()

# Django မှာ ဒါမျိုး ကိုယ်သိမ်းချင်တဲ့ Data Structure သတ်မှတ်တာကို models ဆိုတဲ့ module ထဲက function တွေသုံးပြီး သတ်မှတ်ရတယ်။
# အပေါ်က Task class ကို model အနေနဲ့ သတ်မှတ်မယ်ဆိုရင် Task() class မှာ models.Model pass လုပ်ပေးရမယ်။
class Task(models.Model):
    name = models.TextField()
    status = models.BooleanField()

## အိုကေ ဒါဆိုရင် Task တွေ စပြီး သိမ်းလို့ရပြီ။
```

### Activate Models

ဒီ ```tdl`` app ကို ```mysite``` ဆိုတဲ့ project မှာ ထည့်မယ်။

```mysite/setting.py``` က ```INSTALLED_APPS``` ဆိုတဲ့ array မှာ ထည့်ရင် ရပြီ။

```python
INSTALLED_APPS = [
    # tdl folder ထဲက apps.py file မှာ ရေးထားတဲ့ TdlConfig ဆိုတဲ့ Class ကို ယူသုံးပါ။
    "tdl.apps.TdlConfig",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### Project နဲ့ App ချိတ်ပြီးပြီဆိုရင် Migration လုပ်မယ်။

```
python manage.py makemigrations tdl
python manage.py migrate

```

```log
msd@MSDs-Mac-mini mysite % python manage.py makemigrations tdl
Migrations for 'tdl':
  tdl/migrations/0001_initial.py
    - Create model Task

msd@MSDs-Mac-mini mysite % python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions, tdl
Running migrations:
  Applying tdl.0001_initial... OK

```



### Playing with API

activate python sheel
```
python manage.py shell
```
```log
msd@MSDs-Mac-mini mysite % python manage.py shell
Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
```

```python
# tdl folder ထဲက models.py မှာ ကြေညာထားတဲ့ Task Model ကို import လုပ်ပါ။
from tdl.models import Task
# သိမ်းစည်းထားသော Task စာရင်း
Task.objects.all()
# လက်ရှိတော့ တစ်ခုမှ သိမ်းထားတာ မရှိလို့ empty set ပဲ​ ထွက်လာလိမ့်မယ်။
>>> Task.objects.all()
<QuerySet []>

# task အသစ် Create လုပ်မယ်။
task_one = Task(name="Shopping", status = False)
# သိမ်းမယ်
task_one.save()
# ဒါဆိုရင် id ရမလာမယ်။
task_one.id
# name နဲ့ status လည်း ပြန်ကြည့်လို့ရမယ်
task_one.name
task_one.status

# shopping ထွက်ပြီးသွားလို့ task one ရဲ့ status ကို True လို့ပြင်မယ်။
task_one.status  = True
# ပြင်ပြီးတာနဲ့ save မယ်
task_one.save()
# အခုချိန် ပြန်ကြည့်ရင် task one status က True ဖြစ်မယ်
# task စာရင်း ထုတ်ကြည့်ရင်လည်း Task တစ်ခု ရောက်နေတာ တွေ့ရမယ်။
>>> Task.objects.all()
<QuerySet [<Task: Task object (1)>]>
>>> 
ဒါပေမယ့် [<Task: Task object (1)>] ဆိုတာကြီးက ဖတ်ရတာ နားလည်ဖို့ မလွယ်ဘူး။
ဒီတော့ နားလည်လွယ်အောင် ဒါမျိုး ပြင်ကြမယ်။


```

```mysite/tdl/models.py``` က Task Class မှာ method တစ်ခု ထည့်မယ်။
```python
class Task(models.Model):
    # member data
    name = models.TextField()
    status = models.BooleanField()

    # methods
    def __str__(self):
        return self.name
```
```__str__`` ဆိုတဲ့ method တစ်ခု ထည့်လိုက်တယ်။

အခုချိန် python shell ကို ပြန်ဖွင့်ပြီး select all လုပ်ကြည့်ရင် ဒါမျိုး မြင်ရမယ်။
```python
>>> Task.objects.all()
<QuerySet [<Task: Shopping>]>
````


### CRUD Operation in Python Shell

```python
# import Task
from tdl.models import Task
# create 
task_two = Task(name="Gym", status=False)
task_two.save()

# retrieve
Task.objects.all()
>>> Task.objects.all()
<QuerySet [<Task: Shopping>, <Task: Dinner>]>

# update 
task_two.name = "Go to Gym"
task_two.save()

# delete
task_two.delete()
```


