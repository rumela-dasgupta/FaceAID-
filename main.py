from flask import Flask,request,jsonify
from face_module import train_visitor,recognize_visitor

app=Flask(__name__) #creating our web app
@app.route('/')
def index():
    return "Visitor Management System is Running!"
# Route to register a new visitor
@app.route('/register', methods=['POST'])
def register():
    data = request.json  # Get JSON data from frontend
    result = train_visitor(
        data['Visitor_id'],
        data['Name'],
        data['Contact'],
        data['Height'],
        data['Weight'],
        data['Medical_History']
    )
    return jsonify(result)
# Route to recognize a visitor
@app.route('/recognize', methods=['GET'])
def recognize():
    result = recognize_visitor()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)