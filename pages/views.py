from django.shortcuts import render
from .models import Page

# Create your views here.
def page_list(request):
    context = {
        "pages": Page.objects.all()
    }
    return render(request, 'list.html', context)


def page_detail(request, page_id):
    context = {
        "page": Page.objects.get(id=page_id),
    }
    return render(request, 'detail.html', context)

def __str__(self):
	return self.title

def get_absolute_url(self):
	from django.urls import reverse
	return reverse('pages.views.detail', args=[str(self.id)])