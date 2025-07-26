import requests
#URL='http://127.0.0.1:8000/students/'
# URL='http://127.0.0.1:8000/student/4/'
#URL='http://192.168.1.8:8000/fullupdate/4/'
#URL='http://127.0.0.1:8000/delete/2/'
URL='http://127.0.0.1:8000/create/'

data={       
        "roll":107, # roll no should be less than or 200
        "name": "rampal",# name should be starts with r
        "email": "imran@gmail.com"  # UniqueFieldValidator,should be gmail valiator
}
r = requests.post(url=URL,json=data)
if r.status_code==200:
    res=r.json()
    print(res)
else:
    print(r.status_code)

'''
URL='http://192.168.1.8:8000/create/'
data={
        "name": "manoj",
        "email": "manojbajpai@gmail.com"
}
r = requests.post(url=URL,json=data)
if r.status_code==200:
    res=r.json()
    print(res)
else:
    print(r.status_code)
'''