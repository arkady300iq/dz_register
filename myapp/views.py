from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myapp.models import Review
from myapp.forms import ReviewForm

def reviews_list(request):
    reviews = Review.objects.all()
    context = {
        "reviews": reviews,
    }
    return render(request, 'reviews_list.html', context)

@login_required
def create_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.save()
            return redirect('some_view_name')  
    else:
        form = ReviewForm()
    return render(request, 'create_review.html', {'form': form})

def some_view(request):
    return render(request, 'some_template.html')
