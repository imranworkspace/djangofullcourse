import requests
#URL='http://192.168.1.8:8000/students/'
URL='http://192.168.1.8:8000/students/3/'


data={       
        "id":3,
        "roll":3, 
        "name": "ishan",
        "email": "ishan123@gmail.com"  
}
# r = requests.post(url=URL,json=data)
# r = requests.get(url=URL)
r = requests.patch(url=URL,json=data)
# r = requests.patch(url=URL,json=data)
if r.status_code==200:
    res=r.json()
    print(res)
else:
    print(r.status_code)
