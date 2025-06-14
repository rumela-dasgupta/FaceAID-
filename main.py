from flask import Flask, request, render_template, redirect, url_for, session
from face_module import train_visitor, recognize_visitor

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for session security

@app.route('/')
def home():
    return render_template("faceaidhtml.html")

@app.route('/register-form', methods=['GET'])
def show_register_form():
    return render_template("register.html")

@app.route('/register', methods=['POST'])
def register():
    # Cleanly extract expected fields
    data = {
        'Visitor_id': request.form.get('Visitor_id', ''),
        'Name': request.form.get('Name', ''),
        'Contact': request.form.get('Contact', ''),
        'Height': request.form.get('Height', ''),
        'Weight': request.form.get('Weight', ''),
        'Medical_History': request.form.get('Medical_History', '')
    }

    result = train_visitor(
        data['Visitor_id'],
        data['Name'],
        data['Contact'],
        data['Height'],
        data['Weight'],
        data['Medical_History']
    )

    if result.get("status") == "success":
        session['profile_data'] = data
        return redirect(url_for('profile'))
    else:
        return "<h2>Registration failed. Please try again.<br><a href='/register-form'>Back to Register</a></h2>"

@app.route('/profile')
def profile():
    # Retrieve data from session
    data = session.get('profile_data', {})
    return render_template("profile.html", data=data)

@app.route('/recognize', methods=['POST'])
def recognize():
    result = recognize_visitor()
    if result.get("Status") == "Known":
        return render_template("profile.html", data=result)
    elif result.get("status") == "new":
        return "<h2>Face not recognized. Please register first.<br><a href='/'>Back to Home</a></h2>"
    else:
        return "<h2>Error occurred during recognition.<br><a href='/'>Back to Home</a></h2>"

if __name__ == '__main__':
    app.run(debug=True)
