import requests
# URL='http://192.168.1.8:8000/students/'
# URL='http://127.0.0.1:8000/student/4/'
#URL='http://192.168.1.8:8000/fullupdate/1/'
#URL='http://192.168.1.8:8000/delete/3/'
URL='http://192.168.1.8:8000/create/'

data={       
        "roll":199, # roll no should be less than or 200
        "name": "imran",# name should be starts with r
        "email": "vicky@outlook.com"  # UniqueFieldValidator,should be gmail valiator
}
r = requests.post(url=URL,json=data)
# r = requests.put(url=URL,json=data)
# r = requests.get(url=URL)
# r = requests.delete(url=URL)
if r.status_code==200:
    res=r.json()
    print(res)
else:
    print(r.status_code)
