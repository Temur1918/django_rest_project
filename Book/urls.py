from django.urls import path
from rest_framework.routers import SimpleRouter
from Book.views import BookListApiView, book_list_view, BookUpdateApiView, BookCreateApiView, \
    BookDetailApiView, BookDeleteApiView, BookListCreateApiView, BookDetailUpdateDeleteApiView, \
    BookViewSet


router = SimpleRouter()
router.register('book', BookViewSet, basename='book')


urlpatterns = [
#     path('', BookListApiView.as_view(), ),
#     path('function/', book_list_view, ),
#     path('book/update/<int:pk>', BookUpdateApiView.as_view(), ),
#     path('book/delete/<int:pk>', BookDeleteApiView.as_view(), ),
#     path('book/detail/<int:pk>', BookDetailApiView.as_view(), ),
#     path('book/create/', BookCreateApiView.as_view(), ),
#     path('book/list-create/', BookListCreateApiView.as_view(), ),
#     path('book/detail-update-delete/<int:pk>/', BookDetailUpdateDeleteApiView.as_view(), ),
 ]


urlpatterns = urlpatterns + router.urls