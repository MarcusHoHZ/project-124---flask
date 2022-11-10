from flask import Flask,jsonify, request
app = Flask(__name__)

tasks = [
    {"id" : 1, "Name" : "Marcus", "Contact" : 12345678, "status" : True}
]
@app.route("/get-data", methods = ["POST"])
def addtaskapi():
    if not request.json :
        return jsonify({
            "status" : "error",
            "message" : "please provide the data"
        })
    contact = {
        "id" : tasks[-1]["id"] + 1,
        "Name" : request.json["name"],
        "Contact" : request.json.get("Contact", ""),
        "status" : False
    }
    tasks.append(contact)
    return jsonify({
        "status" : "Success",
        "message" : "task added successfully"
    })


if __name__ == "__main__" :
    app.run() 