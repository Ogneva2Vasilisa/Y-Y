import sys
import requests
import pytest
import argparse


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
    response = requests.get('https://petstore.swagger.io/v2/user/' +func+ '/'+ username)
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
    p = argparse.ArgumentParser()
    # file system args
    p.add_argument("-post", "--p", nargs=1, help="Rasp for your group. Args: data, id")
    p.add_argument("-get", "--g", nargs=2, help="Rasp in auditore. Args: function, id")
    p.add_argument("-delete", "--d", nargs=1, help="Список всех зданий")
    p.add_argument("-put", "--a", nargs=1, help="Список всех зданий")
    args = p.parse_args()  # массив с аргументами
    print(args)
    if args.g:
        gett(args.g[0], args.g[1])
    if args.p:
        postt(args.p[0], '0')


if __name__ == '__main__':
    main()
