from rest_framework.pagination import LimitOffsetPagination

class MyLimitOffsetPagination(LimitOffsetPagination):
    default_limit=3 # http://127.0.0.1:8000/viewall/?limit=2&offset=2
    limit_query_param='mylimit'
    offset_query_param='myoffset' # http://127.0.0.1:8000/viewall/?mylimit=4&myoffset=0
    max_limit=3 # http://127.0.0.1:8000/viewall/?mylimit=4&myoffset=0