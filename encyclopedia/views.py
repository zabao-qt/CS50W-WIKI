from django.shortcuts import render
from django.http import HttpResponse
import markdown2

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
    
    return render(request, "encyclopedia/entry.html", {
        "entry": entry,
        "content": markdown2.markdown(util.get_entry(entry))
    })