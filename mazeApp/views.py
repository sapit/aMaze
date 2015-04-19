from django.http import HttpResponse
from django.shortcuts import render
from Tkinter import Tk
from tkFileDialog import askopenfilename
from mazeApp.forms import ChallengeForm
from mazeApp.models import Maze
from django.core.mail import EmailMessage
import os

# Create your views here.
from mazeApp.algorithms.astar import aStar
from mazeApp.algorithms.processor import getImageAsString, getImageAsList, getImageWidth, getImageHeight


def index(request):
    return HttpResponse("Welcome")


def challenge(request):
    context_dict = {}

    if request.method == "POST":
        form = ChallengeForm(data=request.POST)

        if form.is_valid():
            form.save()
            context_dict["status"] = "success"
            context_dict["link"] = "127.0.0.1:8000/maze/solve/" + form["name"].value()
            print "info", form
            receivers = [x.strip() for x in form['receivers'].value().split(",")]
            maze_name = form['name'].value()
            email = EmailMessage('Subject', context_dict["link"], 'edward.kalfov@gmail.com', receivers, [],
                                 headers={'Message-ID': 'foo'})
            email.send()
        else:
            context_dict["status"] = "fail"
        return render(request, "mazeApp/share.html", context_dict)
    else:
        form = ChallengeForm()
        Tk().withdraw()
        filename = askopenfilename()
        print getImageAsString(filename)
        context_dict["maze"] = getImageAsString(filename)
        grid = getImageAsList(filename)
        context_dict["isSolvable"] = len(aStar(grid)) != 0
        context_dict["mazeName"] = os.path.splitext(os.path.basename(filename))[0]
        context_dict["width"] = getImageWidth(filename)
        context_dict["height"] = getImageHeight(filename)
        context_dict["form"] = form

    return render(request, "mazeApp/send.html", context_dict)


def solveMaze(request, maze_name):
    context_dict = {}
    maze = Maze.objects.get(name=maze_name)
    context_dict["maze_name"] = maze.name
    context_dict["maze_cells"] = maze.cells
    context_dict["maze_rows"] = maze.height
    context_dict["maze_cols"] = maze.width
    print "dict", context_dict
    return render(request, 'mazeApp/solveMaze.html', context_dict)


def solve(request):
    return HttpResponse("solve")
