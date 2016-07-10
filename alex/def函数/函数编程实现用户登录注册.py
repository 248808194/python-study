#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Zhoutao

def regiter(u_name,u_passwd):
    with open("userdb","a") as db:
        newuser = "\n"+u_name + ":"   + u_passwd
        db.write(newuser)


def login(u_name,u_passwd):
    with open("userdb","r") as db:
        for line in db:
            line = line.strip().split(':')
            print(line[0],line[1])
            if line[0] == u_name and line[1] == u_passwd:
                print("welcone")
                return True
            else:
                print("worng username or password")
            return False





def main():
    while True:
        inp=input("enter you chose A:/LOGIN;B:/regiter")
        if inp == "A":
            u_name = input("enter you username:")
            u_passwd = input("enter you password:")
            login(u_name,u_passwd)
        elif inp == 'B':
            u_name = input("enter you username:")
            u_passwd = input("enter you password:")
            regiter(u_name,u_passwd)
        else:
            print("worng input ")

main()
