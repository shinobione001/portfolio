# import os.path
# from wsgiref import headers
# from favicon import Icon
import requests
# # import favicon
from flask import Flask, render_template, send_from_directory, request, redirect
import csv

app = Flask(__name__)


@app.route('/<page_name>.html')
def page(page_name=None):
    return render_template(f'{page_name}.html')


@app.route('/')
def home():
    return render_template('index.html')

def write_to(data):
    with open('data.csv', mode='a',newline='') as database2:
        email = data['email']
        subject = data['text']
        text = data["massage"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, text])


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to(data)
            return render_template('thank_u.html')
        except:
            return "server did not save your file"
    else:
        return 'try something else'





if '__main__' != __name__:
    pass
else:
    app.run(debug=True)

# def write_to(data):
#     with open('database.txt', mode = 'a') as database:
#         
#         file = database.write(f'{email},{subject},{text}')
