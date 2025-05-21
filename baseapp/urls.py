from django.urls import path

from baseapp.views import (
    IndexView,
    OurToolsView,
    AboutView,
    WorkWithUsView,
    Sale1CView,
    # PrivacyView,
    GeneratorView,
    ServiceView,
    ArticleView,
    ArticleListView,
    # SendContactFormView,
    # ContactFormErrorView,
    # ContactFormSuccessView
)


urlpatterns = [

    path('', IndexView.as_view(), name='show-index'),
    path('service/<int:id>/', ServiceView.as_view(), name='show-service-detail'),
    path('article/<int:id>/', ArticleView.as_view(), name='show-article-detail'),
    path('articles/', ArticleListView.as_view(), name='show-articles'),
    path('our-tools/', OurToolsView.as_view(), name='show-our-tools'),
    path('about/', AboutView.as_view(), name='show-about'),
    path('work-with-us/', WorkWithUsView.as_view(), name='show-work-with-us'),
    path('trade-1c/', Sale1CView.as_view(), name='trade_1c'),
    # path('privacy/', PrivacyView.as_view(), name='show_privacy'),
    path('generator/', GeneratorView.as_view(), name='show_generator_page'),
    # path('send-contact-form/', SendContactFormView.as_view(), name='send_contact_form'),
    # path('send-form-success/', ContactFormSuccessView.as_view(), name='send_form_success'),
    # path('send-form-error/', ContactFormErrorView.as_view(), name='send_form_error'),

]