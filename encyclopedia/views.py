from django.shortcuts import render
from django.http import HttpResponse

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def view_entry(request, entry):
    if util.get_entry(entry) == None:
        return render(request, "encyclopedia/not_found.html", {
            "entry": entry
        })
    return HttpResponse(f"Entry: {entry}")