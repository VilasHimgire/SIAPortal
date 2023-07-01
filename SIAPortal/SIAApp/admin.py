from django.contrib import admin
from .models import Student
from .models import Response
from .models import Question
from .models import Notes
from .models import AssignmentResponse
from .models import Assignment

# Register your models here.

admin.site.register(Student)
admin.site.register(Question)
admin.site.register(Response)
admin.site.register(Notes)
admin.site.register(AssignmentResponse)
admin.site.register(Assignment)
