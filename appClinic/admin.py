from django.contrib import admin

from .models import *

# Register your models here.


admin.site.register(clinic)
admin.site.register(lab)
admin.site.register(labAnalysis)
admin.site.register(hospital)