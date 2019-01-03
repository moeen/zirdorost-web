#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request, render_template, send_file
from random import sample
import os, zirdorost_library

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024
app_root = os.path.dirname(os.path.abspath(__file__))

def fix_sub(sub, orginal_name):
    with open(sub, 'r') as subtitle:
        result = zirdorost_library.fix(subtitle.read())
        fixed_result = result.encode('utf-8')
        fixed_sub_address = os.path.join(app_root, 'static/sub', random_dir(), orginal_name)
        with open(fixed_sub_address, 'w') as new_sub:
            new_sub.write(fixed_result)
            return fixed_sub_address

def random_dir():
    dir_name = random_create(10)
    dir_full_address = os.path.join(app_root, 'static/subs', dir_name)
    os.mkdir(dir_full_address)
    return dir_full_address


def random_create(length):
    alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVXYZ0123456789"
    random = "".join(sample(alpha, length))
    return random

@app.route('/')
def index():
    return render_template("upload.html")

@app.route('/upload', methods=['POST'])
def upload():
    target = os.path.join(app_root, 'static/subs') 
    print(target)
    
    if not os.path.isdir(target):
        os.mkdir(target)
    
    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        random_name = random_create(10)
        destination = "/".join([target, random_name + '.srt'])
        print(destination)
        file.save(destination)
        fixed_sub = fix_sub(destination, filename)
        address_splited = fixed_sub.split('/')
        name = os.path.join('static/subs', address_splited[len(address_splited) - 2], address_splited[len(address_splited) - 1])
        print(name)
        os.remove(destination)

    return render_template("complate.html", address=name)

if __name__ == '__main__':
    app.run()
