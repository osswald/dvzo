from django.urls import path

from . import views

urlpatterns = [
    path('article/', views.ArticleListView.as_view(), name='article-list'),
    # path('article/hat/add/', views.HatArticleCreateView.as_view(), name='uniforms:article:hat:create'),
    # path('article/shirt/add/', views.ShirtArticleCreateView.as_view(), name='uniforms:article:hat:create'),
    # path('article/vest/add/', views.VestArticleCreateView.as_view(), name='uniforms:article:vest:create'),
    path('article/coat/add/', views.CoatArticleCreateView.as_view(), name='article-coat-create'),
    # path('article/tie/add/', views.TieArticleCreateView.as_view(), name='uniforms:article:tie:create'),
    # path('article/trousers/add/', views.TrousersArticleCreateView.as_view(), name='uniforms:article:trousers:create'),
    # path('article/shoes/add/', views.ShoesArticleCreateView.as_view(), name='uniforms:article:shoes:create'),
    # path('article/misc/add/', views.MiscArticleCreateView.as_view(), name='uniforms:article:misc:create'),
    # path('article/hat/<int:pk>/', views.HatArticleUpdateView.as_view(), name='uniforms:article:hat:update'),
    # path('article/shirt/<int:pk>/', views.ShirtArticleUpdateView.as_view(), name='uniforms:article:hat:update'),
    # path('article/vest/<int:pk>/', views.VestArticleUpdateView.as_view(), name='uniforms:article:vest:update'),
    path('article/coat/<int:pk>/', views.CoatArticleUpdateView.as_view(), name='article-coat-update'),
    # path('article/tie/<int:pk>/', views.TieArticleUpdateView.as_view(), name='uniforms:article:tie:update'),
    # path('article/trousers/<int:pk>/', views.TrousersArticleUpdateView.as_view(),
    #      name='uniforms:article:trousers:update'),
    # path('article/shoes/<int:pk>/', views.ShoesArticleUpdateView.as_view(), name='uniforms:article:shoes:update'),
    # path('article/misc/<int:pk>/', views.MiscArticleUpdateView.as_view(), name='uniforms:article:misc:update'),

    path('renter/', views.RenterListView.as_view(), name='renter-list'),
    path('renter/add/', views.RenterCreateView.as_view(), name='renter-create'),
    path('renter/<int:pk>/', views.RenterDetailView.as_view(), name='renter-detail'),
    path('renter/<int:pk>/edit/', views.RenterUpdateView.as_view(), name='renter-update'),
    path('renter/<int:pk>/delete/', views.RenterDeleteView.as_view(), name='renter-delete'),

    path('rent/', views.RentListView.as_view(), name='rent-list'),
    path('rent/add/', views.RentCreateView.as_view(), name='rent-create'),
    path('rent/<int:pk>/', views.RentDetailView.as_view(), name='rent-detail'),
    path('rent/<int:pk>/edit/', views.RentUpdateView.as_view(), name='rent-update'),
    path('rent/<int:pk>/delete/', views.RentDeleteView.as_view(), name='rent-delete'),
    path('rent/<int:pk>/print/', views.RentPdfView.as_view(template_name="pdf/rent.html"), name='rent-print'),

    path('rent/article/add/<int:pk>', views.ArticleRentCreateView.as_view(), name='rent-article-create'),
    path('rent/article/<int:pk>/', views.ArticleRentUpdateView.as_view(), name='rent-article-update'),
    path('rent/article/<int:pk>/delete/', views.ArticleRentDeleteView.as_view(), name='rent-article-delete'),
    #
    # path('/rent/<int:rent_pk>/print/', views.RentPrintView.as_view(template_name="pdf/rent.html"),
    #      name='uniforms:rent:pdf'),
    #
    # path('let/', views.LetListView.as_view(), name='uniforms:let:list'),
    # path('let/add/', views.LetCreateView.as_view(), name='uniforms:let:create'),
    # path('let/<int:let_pk>/', views.LetDetailView.as_view(), name='uniforms:let:detail'),
    # path('let/<int:let_pk>/edit/', views.LetUpdateView.as_view(), name='uniforms:let:update'),
    # path('let/<int:let_pk>/delete/', views.LetDeleteView.as_view(), name='uniforms:let:delete'),
    #
    # path('let/<int:let_pk>/article/add/', views.LetArticleCreateView.as_view(), name='uniforms:let_article:create'),
    # path('let/<int:let_pk>/article/<int:rent_article_pk>/', views.LetArticleUpdateView.as_view(),
    #      name='uniforms:let_article:update'),
    # path('let/<int:let_pk>/article/<int:rent_article_pk>/delete/', views.LetArticleDeleteView.as_view(),
    #      name='uniforms:let_article:delete'),
    #
    # path('/let/<int:let_pk>/print/', views.LetPrintView.as_view(template_name="pdf/let.html"),
    #      name='uniforms:let:pdf'),
]
