from django.shortcuts import render
from .forms import AirportRouteForm, NthNodeForm
from .models import AirportRoute
from .services import find_nth_node


def add_route(request):
    form = AirportRouteForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, "routes/add_route.html", {"form": form})


def nth_node(request):
    form = NthNodeForm(request.POST or None)
    result = None

    if form.is_valid():
        result = find_nth_node(
            form.cleaned_data["root"],
            form.cleaned_data["direction"],
            form.cleaned_data["n"],
        )

    return render(request, "routes/nth_node.html", {"form": form, "result": result})


def longest_route(request):
    route = AirportRoute.objects.order_by("-duration_min").first()
    return render(request, "routes/longest.html", {"route": route})


def shortest_route(request):
    route = AirportRoute.objects.order_by("duration_min").first()
    return render(request, "routes/shortest.html", {"route": route})
