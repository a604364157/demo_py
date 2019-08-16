import datetime

from django.http import HttpResponse
from django.shortcuts import render_to_response

from web.models import Student


def say_hello(requset):
    s = 'Hello 蕊英'
    current_time = datetime.datetime.now()
    html = '<html><head></head><body><h1> %s </h1><p> %s </p></body></html>' % (s, current_time)
    return HttpResponse(html)


def show_students(requset):
    student = [{id: 1, 'name': 'jiangjx', 'age': 20}, {id: 2, 'name': 'wangry', 'age': 18}]
    return render_to_response('student.html', {'students': student})


def show_real_students(request):
    student = Student.objects.all()
    return render_to_response('student.html', {'students': student})