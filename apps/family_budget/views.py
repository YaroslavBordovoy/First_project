from django.http import HttpResponse
from django.shortcuts import render

from .models import Budget


def family_budget(request) -> HttpResponse:
    budget = Budget.objects.all()
    return render(
        request,
        "budget/budget.html",
        {
            "title": "Family budget",
            "family_budget": budget,
        },
    )


def create():
    pass


def read():
    pass


def update():
    pass


def delete():
    pass
