#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    
    req = requests.get('https://jsonplaceholder.typicode.com/posts')
    status = req.status_code
    print(f"Status Code: {status}")
    
    if status == 200:
        data = req.json()
        for titles in data:
            print(titles['title'])
    else:
        print("Fail to fetch")

def fetch_and_save_posts():
    
    req = requests.get('https://jsonplaceholder.typicode.com/posts')
    status = req.status_code
    print(f"Status Code: {status}")
    
    if status == 200:
        data = req.json()
        data_list = []
        data_dic = {}

        for dic in data:
            for key, value in dic.items():
                if key in {'id', 'title', 'body'}:
                    data_dic[key] = value
            data_list.append(data_dic)            
    else:
        print("Fail to fetch")
    
    with open('posts.csv','w', newline='', encoding='utf-8') as f:
        fieldnames = ['id', 'title', 'body']
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for row in data_list:
            w.writerow(row)
       
fetch_and_save_posts()