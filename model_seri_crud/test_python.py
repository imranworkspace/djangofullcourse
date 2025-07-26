import requests
#URL='http://192.168.1.8:8000/students/'
#URL='http://192.168.1.8:8000/student/3/'
#URL='http://192.168.1.8:8000/fullupdate/2/'
URL='http://192.168.1.8:8000/partial_update/2/'
#URL='http://127.0.0.1:8000/delete/2/'
#URL='http://127.0.0.1:8000/create/'

data={       
        "roll":103, 
        "name": "muskan",
        "email": "irfan@gmail.com"}

# r = requests.post(url=URL,json=data)
# r = requests.get(url=URL)
#r = requests.put(url=URL,json=data)
r = requests.patch(url=URL,json=data)
if r.status_code==200:
    res=r.json()
    print(res)
else:
    print(r.status_code)

