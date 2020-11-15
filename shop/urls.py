from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('gallery/', views.galleryfunc, name='gallery'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path('checkout/', views.checkout, name='checkout'),
    path('trackorder/', views.trackorder, name='trackorder'),
    path('blog/blogsinglepost/<int:id>/', views.blogsinglepost, name='blogsinglepost'),
    path('gallery/gallerysinglepost/<int:id2>/', views.gallerysinglepost, name='gallerysinglepost'),
    path('shop/shopsingleproduct/<int:id3>/', views.shopsingleproduct, name='shopsingleproduct'),


]
