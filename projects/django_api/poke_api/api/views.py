from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from django.views import generic
from .models import Pokemon, Trainers


class IndexView(generic.ListView):
    template_name = "api/index.html"
    context_object_name = "latest_pokemon_list"

    def get_queryset(self):
        return Pokemon.objects.order_by("-pub_date")[:5]
    # render(request, "api/index.html", context)


class DetailView(generic.DetailView):
    model = Pokemon
    template_name = "api/detail.html"


class ResultsView(generic.DetailView):
    model = Pokemon
    template_name = "api/results.html"


def vote(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    try:
        selected_choice = pokemon.trainers_set.get(pk=request.POST["trainer"])
    except (KeyError, Trainers.DoesNotExist):
        return render(
            request,
            "api/detail.html",
            {
                "pokemon": pokemon,
                "error_message": "You didn't select a trainer.",
            }
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
    return HttpResponseRedirect(reverse("api:results", args=(pokemon.id,)))
