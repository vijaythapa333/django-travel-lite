from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, TemplateView, DetailView, ListView
from .models import Blog

# Create your views here.


class BlogListView(ListView):
	template_name = 'blog/all_blogs.html'
	model = Blog
	context_object_name = 'blogs'
	paginate_by = 6



class BlogDetailView(DetailView):
	template_name = 'blog/blog_detail.html'
	model = Blog
	slug_url_kwarg = 'blog_slug'
	slug_field = 'blog_slug'
	context_object_name = 'blog'


	def get_context_data(self, **kwargs):
		current_blog = get_object_or_404(Blog, blog_slug=self.kwargs.get('blog_slug'))
		similar_blogs = Blog.objects.filter(blog_is_active='yes', blog_category__in=current_blog.blog_category.all()).exclude(blog_slug=self.kwargs.get('blog_slug')).order_by('-blog_created_at')[:3]
		other_blogs = Blog.objects.filter(blog_is_active='yes').order_by('-blog_created_at')[:3]

		context = super().get_context_data(**kwargs)
		context['similar_blogs'] = similar_blogs
		context['other_blogs'] = other_blogs
		return context
