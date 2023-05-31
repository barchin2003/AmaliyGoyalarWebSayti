from django.shortcuts import render, redirect
from .models import Idea


# Create your views here.
def main(request):
    if request.method == 'POST':
        title = request.POST['name']
        image = request.FILES['image']
        body = request.POST['message']
        Idea.objects.create(title=title, image=image, body=body)
        return redirect('main')
    context = {
        'ideas': Idea.objects.all(),
    }
    return render(request, 'index.html', context)


def idea_detail(request, id):
    idea = Idea.objects.get(id=id)
    return render(request, 'idea_modal.html', {'idea': idea})
