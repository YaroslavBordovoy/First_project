from django.http import HttpResponse


def test_func(request):
    return HttpResponse("This test function!")
