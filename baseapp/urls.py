from django.urls import path
from .views import show_index
from .views import show_our_tools
from .views import show_about
from .views import show_article
from .views import show_articles
from .views import show_service
from .views import show_services
# from .views import show_e_commerce_and_1c
from .views import show_work_with_us
from .views import send_contact_form
from .views import trade_1c
from .views import show_privacy
from .views import show_generator_page
from .views import send_form_success
from .views import send_form_error


urlpatterns = [

    path('', show_index, name='show-index'),
    path('service/<int:id>/', show_service, name='show-service-detail'),
    path('services/', show_services, name='show-services'),
    path('article/<int:id>/', show_article, name='show-article-detail'),
    path('articles/', show_articles, name='show-articles'),
    path('our-tools/', show_our_tools, name='show-our-tools'),
    path('about/', show_about, name='show-about'),
    path('work-with-us/', show_work_with_us, name='show-work-with-us'),
    # path('e-commerce-and-1c/', show_e_commerce_and_1c, name='show_e_commerce_and_1c'),
    path('send-contact-form/', send_contact_form, name='send_contact_form'),
    path('send-form-success/', send_form_success, name='send_form_success'),
    path('send-form-error/', send_form_error, name='send_form_error'),
    path('trade-1c/', trade_1c, name='trade_1c'),
    path('privacy/', show_privacy, name='show_privacy'),
    path('generator/', show_generator_page, name='show_generator_page'),

]