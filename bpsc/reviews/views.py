from django.views.generic import ListView
from django.views.generic import TemplateView
from bpsc.reviews.models import Review
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from bpsc.reviews.forms import ReviewForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Avg

from django.contrib import messages

def reviews(request):
    return render(request, 'reviews.html')

def clean(result):
        if result is None:
            return 0
        else:
            return int(round(result))

def render_stars(rating):
    result = ""
    for i in range(0, rating):
        result += "<span class='glyphicon glyphicon-star'></span>"
    for i in range(rating, 5):
        result += "<span class='glyphicon glyphicon-star-empty'></span>"
    return result

class ReviewListView(ListView):
    template_name = 'reviews_list.html'
    model = Review



    def get_context_data(self, **kwargs):
        context = super(ReviewListView, self).get_context_data(**kwargs)
        housing_avg_rating = clean(Review.objects.filter(service='Housing').aggregate(Avg('rating'))['rating__avg'])
        context['housing_stars'] = render_stars(housing_avg_rating)
        employment_avg_rating = clean(Review.objects.filter(service='Employment').aggregate(Avg('rating'))['rating__avg'])
        context['employment_stars'] = render_stars(employment_avg_rating)
        community_avg_rating = clean(Review.objects.filter(service='Community Resources').aggregate(Avg('rating'))['rating__avg'])
        context['community_stars'] = render_stars(community_avg_rating)
        legal_avg_rating = clean(Review.objects.filter(service='Legal').aggregate(Avg('rating'))['rating__avg'])
        context['legal_stars'] = render_stars(legal_avg_rating)
        dental_avg_rating = clean(Review.objects.filter(service='Dental').aggregate(Avg('rating'))['rating__avg'])
        context['dental_stars'] = render_stars(dental_avg_rating)
        optometry_avg_rating = clean(Review.objects.filter(service='Optometry').aggregate(Avg('rating'))['rating__avg'])
        context['optometry_stars'] = render_stars(optometry_avg_rating)
        medical_avg_rating = clean(Review.objects.filter(service='Medical').aggregate(Avg('rating'))['rating__avg'])
        context['medical_stars'] = render_stars(medical_avg_rating)
    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(ReviewListView, self).dispatch(*args, **kwargs)
        return context

     

class SubmitReviewListView(TemplateView):
    template_name = 'base_submit_review.html'
    # form_class = ReviewForm
   
    def form_valid(self, form):
        form.submit_review()
        return super(FormView, self).form_valid(form)   

    def get_context_data(self, **kwargs):
        context = super(SubmitReviewListView, self).get_context_data(**kwargs)
        if self.request.method == "GET":
            context['reviewform'] = ReviewForm()
            return context
        else: # POST requests
            context['reviewform'] = ReviewForm(self.request.POST)
            return context

    # THIS FUNCION IS FOR POST VALIDATION
    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        reviewform = context['reviewform']
        if reviewform.is_valid():
            reviewform.save()
            messages.success(request, 'Review was successfully submitted!')
            return redirect('/reviews/reviews')
        else:
            return self.render_to_response(context)

