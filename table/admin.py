from django.contrib import admin
from .models import (Day, Lecturer, 
        Course, Type, Session, Visitor
    )

admin.site.register(Day)
admin.site.register(Lecturer)
admin.site.register(Course)
admin.site.register(Type)
admin.site.register(Session)
admin.site.register(Visitor)