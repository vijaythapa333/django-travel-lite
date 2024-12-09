from .models import Category, Blog



def footer_blog_menu(request):
	recent_blogs = Blog.objects.filter(blog_is_active='yes').order_by('-blog_created_at')[:5]
	context = {
		'recent_blogs': recent_blogs
	}
	return context