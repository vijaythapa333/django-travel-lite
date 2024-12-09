from .models import AppDetail, SocialMedia



def app_detail(request):
	# this_app = AppDetail.objects.filter(id__lookup=1).latest()
	socialmedias = SocialMedia.objects.filter(socialmedia_is_active='yes')

	context = {
		# 'this_app': this_app,
		'socialmedias': socialmedias
	}
	return context