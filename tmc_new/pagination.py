from rest_framework.pagination import PageNumberPagination


class GetHistoryAllPagination(PageNumberPagination):
    page_size = 10
