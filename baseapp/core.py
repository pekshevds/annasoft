from .models import Service
from .models import Article

def get_context():
	
	return {
		'services': Service.objects.all()[:6],
		'articles': Article.objects.all()[:3],		
	}