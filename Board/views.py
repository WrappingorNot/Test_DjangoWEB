from django.shortcuts import render, redirect

# Create your views here.
from .forms import *
from .models import *


def board(request):
	if request.method == 'POST':
		title = request.POST['title']
		content = request.POST['content']
		writer = request.POST['writer']


		board = Board(
			title=title,
			content=content,
			writer=writer,
		)
		board.save()
		return redirect('board')
	else:
		boardForm = BoardForm
		board = Board.objects.all()
		content = {
			'boardForm' : boardForm,
			'board' : board,
		}
		return render(request, 'board.html', content)

def boardEdit(request, pk):
	board = Board.objects.get(id = pk)
	if request.method == "POST":
		board.title = request.POST['title']
		board.content = request.POST['content']
		board.writer = request.POST['writer']

		board.save()
		return redirect('board')
	else:
		boardForm = BoardForm
		return render(request, 'update.html', {'boardForm':boardForm})

def boardDelete(request, pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return redirect('board')