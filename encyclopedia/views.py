from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
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

def search(request):
    # print ("request: " + str(request))
    # print ("request.GET: " + str(request.GET))
    if 'q' in request.GET:
        originQuery = request.GET['q']
        query = originQuery
        if ' ' in originQuery:
            query = originQuery.replace(" ", "")

        entries = [entry for entry in util.list_entries() if query in entry.lower()]
        return render(request, 'encyclopedia/search.html', {
            "entries": entries,
            "query": originQuery,
        })
    else:
        # return redirect('index')
        return HttpResponse("No query provided")
    
def create(request):
    if request.method == "POST":
        print ("request.POST: " + str(request.POST))
        form = request.POST
        title = form['title']
        content = form['content']
        if title in util.list_entries():
            return render(request, "encyclopedia/create.html", {
                "error": True
            })
        util.save_entry(title, content)
        return HttpResponseRedirect(reverse("view_entry", args=[title]))
    return render(request, "encyclopedia/create.html")

def edit(request, entry):
    return HttpResponse("Edit page for " + entry)