from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static

app_name =  'base'
urlpatterns = [
    path('', views.index, name='home'),
    
    path('galeria/',views.galeria,name='galeria'),
    path('galeria/<int:pk>/',views.galeria_get,name='galeria_get'),
    path('galeria/create/',views.galeria_create,name='galeria_create'),
    path('galeria/delete/<int:pk>',views.galeria_delete,name='galeria_delete'),
    #edit -> add img to galery & delete image from galery
    path('galeria/<int:pk>/addImg/',views.galeria_add_img_to_galeria,name='galeria_add_img_to_galeria'),
    path('galeria/<int:page>/delImg/<int:pk>',views.galeria_del_img_to_galeria,name='galeria_del_img_to_galeria'),
    

    path('archiv/new/',views.clanok_create_empty,name='clanok_create_empty'),
    path('archiv/',views.archiv,name='archiv'),
    path('archiv/clanok/<int:pk>/',views.clanok,name='clanok'),
    path('archiv/clanok/create/<int:pk>/',views.clanok_create,name='clanok_create'),
    path('archiv/clanok/create/addImg/<int:pk>/',views.clanok_add_img,name="clanok_add_img"),
    path('archiv/clanok/update/',views.clanok_update,name="clanok_update"),
    path('archiv/clanok/clanok_body_RO/<int:pk>/',views.clanok_body_RO,name="clanok_body_RO"),
    #edit
    #delete

    #post comment
    path('archiv/clanok/add_comment/<int:pk>',views.add_comment,name="add_comment"),

    #oznamy
    path('oznam_add/',views.oznam_add,name="oznam_add"),
    path('oznam_del/',views.oznam_del,name="oznam_del"),
    
    path('login/',views.log_page,name='log_page'),
    path('login-me/', views.login_bk,name='login-me'),
    path('reg_bk/', views.reg_bk,name='reg_bk'),
    path('logout/', views.log_out,name='log_out'),

    path('dashboard/', views.dashboard,name='dashboard'),
    #logout

    path('uploadImgs/', views.uploadImg, name="uploadImg"),

    path('setTopPost/<int:pk>/<int:pk_post>/', views.setTopPost, name="setTopPost"),
    path('delTopPost/<int:pk>/', views.delTopPost, name="delTopPost"),

]


if settings.DEBUG == True:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)