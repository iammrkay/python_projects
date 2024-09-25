from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList , Item
from .forms import CreateNewList 
# Create your views here.
def index(resopnse, id):
    ls = ToDoList.objects.get(id = id)
    if resopnse.method == "POST":
        print(resopnse.POST)
        if resopnse.POST.get("save"):
            for item in ls.item_set.all():
                if resopnse.POST.get("c"+str(item.id))== "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif resopnse.POST.get("newItem"):
            txt = resopnse.POST.get("new")
            if len(txt) > 2:
                ls.item_set.create(text = txt , complete = "False")
            else:
                print("invalid input")

    return render(resopnse,"main/list.html", {"ls":ls})

def home(response):
    return render(response,"main/home.html", {})

def create(response):
    
    if response.method == "POST":
        form = CreateNewList (response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)

        return HttpResponseRedirect("/%i" %t.id)
    else:
        form = CreateNewList
    return render(response, "main/create.html",{"form": form})

def view(response):
    return render(response,"main/view.html",{})