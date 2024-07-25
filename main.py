import sys
import requests
import pytest


def gett(func, *status):
    print(func, status)
    stats = ''
    for u in status:
        stats = stats + u + ','
    stats = stats[:-1]
    print(stats)
    response = requests.get('https://petstore.swagger.io/v2/pet/' + func + '?status=' + stats)
    print(response.status_code, response.reason)
    return [int(response.status_code), response.reason]


def gett2_find(func,username):
    print(func, username)
    print('https://petstore.swagger.io/v2/' +func+ '/'+ username)
    response = requests.get('https://petstore.swagger.io/v2/' +func+ '/'+ username)
    return [int(response.status_code), response.reason]


def postt():
    response = requests.post('https://petstore.swagger.io/v2/user/createWithList', data={"id": 0, "username": "string",
                                                                                         "firstName": "string",
                                                                                         "lastName": "string",
                                                                                         "email": "string",
                                                                                         "password": "string",
                                                                                         "phone": "string",
                                                                                         "userStatus": 0},
                             headers={"Content-Type": "application/json"})
    print(response.json())
    print(response.status_code, response.reason)
    return [int(response.status_code), response.reason]


def main():
    li = gett("findByStatus", '[] ')
    print(li)

if __name__ == '__main__':
    main()
