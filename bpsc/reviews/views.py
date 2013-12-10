from django.views.generic import ListView
from django.views.generic import TemplateView
from bpsc.reviews.models import Review, EnableUsersToSeeReview
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from bpsc.reviews.forms import ReviewForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib import messages

def reviews(request):
    return render(request, 'reviews.html')

class ReviewListView(ListView):
    template_name = 'reviews_list.html'
    model = Review

    def get_context_data(self, **kwargs):
        context = super(ReviewListView, self).get_context_data(**kwargs)
        context['review_access_enabled'] = EnableUsersToSeeReview.objects.get(id=1).access
        return context

class SubmitReviewListView(TemplateView):
    template_name = 'base_submit_review.html'
    # form_class = ReviewForm
   
    def form_valid(self, form):
        form.submit_review()
        return super(FormView, self).form_valid(form)   

    def get_context_data(self, **kwargs):
        context = super(SubmitReviewListView, self).get_context_data(**kwargs)
        context['review_access_enabled'] = EnableUsersToSeeReview.objects.get(id=1).access
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

