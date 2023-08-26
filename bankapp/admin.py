from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(newbankmodel)
admin.site.register(addamountmodel)
admin.site.register(withdrawamount)