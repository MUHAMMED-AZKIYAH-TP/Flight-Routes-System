from django.shortcuts import render
from .forms import AirportRouteForm, NthNodeForm , LongestRouteForm , ShortestRouteForm
from .services import find_nth_node, find_longest_path, find_shortest_path_from_airport






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
    form = LongestRouteForm(request.POST or None)
    node = None
    duration = None

    if form.is_valid():
        airport = form.cleaned_data["airport"]
        node, duration = find_longest_path(airport)

    return render(
        request,
        "routes/longest.html",
        {
            "form": form,
            "node": node,
            "duration": duration,
        }
    )





def shortest_route(request):
    form = ShortestRouteForm(request.POST or None)
    node = None
    duration = None

    if form.is_valid():
        airport = form.cleaned_data["airport"]
        node, duration = find_shortest_path_from_airport(airport)

    return render(
        request,
        "routes/shortest.html",
        {
            "form": form,
            "node": node,
            "duration": duration,
        }
    )

