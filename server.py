from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def home_page():
    return render_template('index.html')

def write_to_csv(data):
    with open('database.csv', mode='w', newline='',) as database:
        field_names = ['Email', 'Subject', 'Message']
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.DictWriter(database, fieldnames=field_names, delimiter='|')

        csv_writer.writeheader()
        csv_writer.writerow({'Email': email, 'Subject': subject, 'Message': message})

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return "something went wrong"



if __name__ == '__main__':
    app.run(debug=True)