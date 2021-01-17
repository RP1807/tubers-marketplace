from django.contrib import messages
from django.shortcuts import render, redirect
from .models import HireTuber


def hiretuber(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        city = request.POST['city']
        phone = request.POST['phone']
        email = request.POST['email']
        state = request.POST['state']
        message = request.POST['message']

        hiretuber = HireTuber(first_name=first_name, last_name=last_name, tuber_id=tuber_id, tuber_name=tuber_name,
                              city=city, phone=phone, email=email, state=state, message=message)
        hiretuber.save()
        messages.success(request=request, message="Thanks for reaching out ")
        return redirect(to='hiretuber')

