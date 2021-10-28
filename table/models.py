from django.db import models


class Day(models.Model):
    title = models.CharField(max_length=20)
    
    def get_sessions(self):
        return self.sessions.order_by('start')
    
    def __str__(self):
        return self.title


class Lecturer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    office = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=255)
    code = models.CharField(max_length=5)
    lecturer = models.ForeignKey(Lecturer, null=True, on_delete=models.SET_NULL)
    credit = models.IntegerField(default=12)
    status = models.CharField(max_length=20, default='Core')
    
    def __str__(self):
        return self.code


class Type(models.Model):
    title = models.CharField(max_length=20)
    
    def __str__(self):
        return self.title


class Session(models.Model):
    day = models.ForeignKey(Day, related_name='sessions', on_delete=models.CASCADE)
    course = models.ForeignKey(Course, related_name='sessions', on_delete=models.CASCADE)
    start = models.TimeField()
    end = models.TimeField()
    venue = models.CharField(max_length=50)
    session_type = models.ForeignKey(Type, related_name='sessions', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.course} on {self.day}'

class Visitor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    session_key = models.CharField(max_length=255)
    ip_addr = models.CharField(max_length=255)
    
    def __str__(self):
        return self.ip_addr
    