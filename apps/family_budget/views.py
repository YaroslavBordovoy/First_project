from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render

from .forms import BudgetForm
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


def create_post(request):
    if request.method == "POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            form = BudgetForm()
            messages.success(request, "Entry added successfully")
    else:
        form = BudgetForm()
    context = {
        "title": "Add an entry",
        "form": form,
    }
    return render(request, "budget/create_post.html", context=context)


def read_post(request):
    query = request.GET.get('q')
    if query.startswith('0'):
        pass
    else:
        post = Budget.objects.get(pk=query)

    context = {
        "title": "Entry information",
        "post": post,
    }
    return render(request, "budget/post_info.html", context=context)


def update_post(request, id):
    pass


def delete():
    pass


def search_post(request):
    context = {
        "title": "Post search",
    }
    return render(request, "budget/search_post.html", context=context)
