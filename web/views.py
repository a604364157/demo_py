import datetime

from django.http import HttpResponse
from django.shortcuts import render_to_response

from web.models import Student, TwoColorBall
from web.servive.twoColorball import run_two_colors, run_big_lottos


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


def run_two_color_ball(request):
    times = request.GET.get("times")
    balls = run_two_colors(times)
    return render_to_response('twoColorBall.html', {'balls': balls})


def run_big_lotto(request):
    times = request.GET.get("times")
    balls = run_big_lottos(times)
    return render_to_response('twoColorBall.html', {'balls': balls})