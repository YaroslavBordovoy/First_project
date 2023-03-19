from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

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
    query = request.GET.get("q")
    post = Budget.objects.get(pk=query)

    context = {
        "title": "Entry information",
        "post": post,
    }
    return render(request, "budget/post_info.html", context=context)


def update_post(request, pk: Budget.pk):
    post = get_object_or_404(Budget, pk=pk)
    if request.method == "POST":
        form = BudgetForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post has been updated successfully.")
            return redirect("family_budget:budget")
        else:
            form = BudgetForm(instance=post)
        context = {"title": "Update User", "form": form}
        return render(request, "budget/update_post.html", context=context)


def delete_post(request, pk: Budget.pk):
    post = get_object_or_404(Budget, pk=pk)
    post.delete()
    messages.success(request, f"User {post.pk} deleted.")
    return redirect("family_budget:budget")


def search_post(request):
    context = {
        "title": "Post search",
    }
    return render(request, "budget/search_post.html", context=context)
