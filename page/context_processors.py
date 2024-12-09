from .models import Page


def page_menu(request):
	top_menu = Page.objects.filter(page_is_active='yes', page_position='top')
	school_menu = Page.objects.filter(page_is_active='yes', page_position='school')
	footer_menu = Page.objects.filter(page_is_active='yes', page_position='footer')
	context = {
		'top_menu': top_menu,
		'school_menu': school_menu,
		'footer_menu': footer_menu
	}
	return context
