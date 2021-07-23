from django.urls import path
from .views import show_index
from .views import show_our_tools
from .views import show_about
from .views import show_article
from .views import show_articles
from .views import show_service
from .views import show_services
from .views import show_e_commerce_and_1c
from .views import show_work_with_us
from .views import send_contact_form




urlpatterns = [    
    path('', show_index, name='show-index'),
    
    path('service/<int:id>/', show_service, name='show-service-detail'),
    path('services/', show_services, name='show-services'),
    path('article/<int:id>/', show_article, name='show-article-detail'),
    path('articles/', show_articles, name='show-articles'),
    path('our-tools/', show_our_tools, name='show-our-tools'),
    path('about/', show_about, name='show-about'),
    path('work-with-us/', show_work_with_us, name='show-work-with-us'),
    path('e-commerce-and-1c/', show_e_commerce_and_1c, name='show-show_e_commerce_and_1c'),
    path('send-contact-form/', send_contact_form, name='send_contact_form'),
]