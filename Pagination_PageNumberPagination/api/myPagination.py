from rest_framework.pagination import PageNumberPagination

class MyPageNumberPagination(PageNumberPagination):
    '''per page records'''
    page_size=2
    '''page is default so I replace 'page' to 'mypage' or 'p'
    http://127.0.0.1:8000/viewall/?mypage=3'''
    page_query_param='p' 
    '''assign power to admin he/she can access multiple records using below scenarios
    http://127.0.0.1:8000/viewall/?p=1&records=9'''
    page_size_query_param='records'
    '''give admin access with some limitation like admin can see maximum 10 records
    http://127.0.0.1:8000/viewall/?p=1&records=11 wont work 
    '''
    max_page_size=10
    '''"last_page" works for see last page records but we can replace this string using below query'''
    last_page_strings='end' # instead 'last_page' we can use 'end'