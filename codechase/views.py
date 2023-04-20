from django.http import HttpResponse
from django.shortcuts import render

USERS = []
QUESTIONS = [
    {
        title: "Two states",
        description: "Given an array , return the maximum of the array?",
        testCases: [{input: "[1,2,3,4,5]", output: "5"}],
    }
]
SUBMISSIONS = []


def signup(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        if any(user["email"] == email for user in USER):
            return HttpResponse(status=409)
        USERS.append({"email": email, "password": password, "isadmin": False})
        return HttpResponse(status=200)


def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = None
        for user_dict in USERS:
            if user_dict["email"] == email:
                user = user_dict
        if user:
            if user["password"] == password:
                token = "random_string_token"
                return HttpResponse(token, status=200)
            else:
                return HttpResponse(status=401)
        return HttpResponse(status=401)


def questions(request):
    return HttpResponse(QUESTIONS)


def submissions(request):
    if request.method == "GET":
        return HttpResponse(SUBMISSIONS)
    elif request.method == "POST":
        solution_accepted = True
        SUBMISSIONS.append(request.body)
        return HttpResponse(status=200)


# Create your views here.
