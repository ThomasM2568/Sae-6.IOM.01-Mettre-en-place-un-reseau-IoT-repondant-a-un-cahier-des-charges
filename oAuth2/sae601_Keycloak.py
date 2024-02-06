'''
import requests

url = "http://192.168.1.106:8080/realms/master/protocol/openid-connect/token"

payload = 'client_id=admin-cli&username=scripts&password=python&grant_type=password'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

'''

import requests

ip="192.168.1.122"
port="8080"


def get_token(ip,port,username,password):
    url = "http://"+ip+":"+port+"/realms/master/protocol/openid-connect/token"
    payload = 'client_id=admin-cli&username='+str(username)+'&password='+str(password)+'&grant_type=password'
    headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    try:
        response = requests.request("POST", url, headers=headers, data=payload)
        return(response.json())
    except:
        return {}
    
a=get_token("192.168.1.122","8080","admin","admin")

def get_user_list(ip,port,token):

    url = "http://"+ip+":"+port+"/admin/realms/master/users/"

    payload = {}
    headers = {
      'Authorization': 'Bearer '+str(token)
    }

    try:
        response = requests.request("GET", url, headers=headers, data=payload)

        return(response.json())
    except:
        return {}



try:
    b=get_user_list(ip,port,a['access_token'])
except:
    print(None)
    
def get_user_groups(ip,port,token,userid):

    url = "http://"+ip+":"+port+"/admin/realms/master/users/"+userid+"/groups"

    print(url)
    payload = {}
    headers = {
      'Authorization': 'Bearer '+token
    }

    try:
        response = requests.request("GET", url, headers=headers, data=payload)

        return(response.json())
    except Exception as e:
        print(e)
        return {}

username="toto"
try:
    print("-----------")
    for dic in b:
        if (dic['username'] == username):
            print(dic['id'])
            print(get_user_groups(ip,port,a['access_token'],dic["id"]))
    print("-----------")
except:
    print(None)