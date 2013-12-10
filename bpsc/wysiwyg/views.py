from bpsc.wysiwyg.models import Post
from django.views.generic import DetailView

class ResumeResourceView(DetailView):
    model = Post
    context_object_name = 'resource'
    template_name = 'resume_resource.html'

    def get_object(self, **kwargs):
        return Post.objects.get(url='search:employment_resume')

class CoverLetterResourceView(DetailView):
    model = Post
    context_object_name = 'resource'
    template_name = 'cover_letter_resource.html'

    def get_object(self, **kwargs):
        return Post.objects.get(url='search:employment_cover_letter')

class MentalResourceView(DetailView):
    model = Post
    context_object_name = 'resource'
    template_name = 'mental_resource.html'

    def get_object(self, **kwargs):
        return Post.objects.get(url='search:community_mental')

class DentalResourceView(DetailView):
    model = Post
    context_object_name = 'resource'
    template_name = 'dental_resource.html'

    def get_object(self, **kwargs):
        return Post.objects.get(url='search:community_dental')

class MedicalResourceView(DetailView):
    model = Post
    context_object_name = 'resource'
    template_name = 'medical_resource.html'

    def get_object(self, **kwargs):
        return Post.objects.get(url='search:community_medical')



