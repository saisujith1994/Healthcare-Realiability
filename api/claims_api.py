from flask import Flask, jsonify,render_template,request

app= Flask(__name__)

claims_data = [
    {
        "claims_id": 1001,
        "patient_id": 123,
        "allowed_amount": 1000.00,
        "primary_paid_amount": 800.00,
        "secondary_paid_amount": 150.00
    },
    {
        "claims_id": 1002,
        "patient_id": 124,
        "allowed_amount": 2000.00,
        "primary_paid_amount": 1500.00,
        "secondary_paid_amount": 300.00
    },
    {
        "claims_id": 1003,
        "patient_id": 125,
        "allowed_amount": 1500.00,
        "primary_paid_amount": 1200.00,
        "secondary_paid_amount": 200.00
    },
    {
        "claims_id": 1004,
        "patient_id": 126,
        "allowed_amount": 2500.00,
        "primary_paid_amount": 2000.00,
        "secondary_paid_amount": 400.00
    }
]

@app.route("/claims",methods=["GET"])
def get_claims():
    patient_filter= request.args.get("patient_id")
    if patient_filter:
        filtered_claims = [claim for claim in claims_data if str(claim["patient_id"]) == patient_filter]
    else:
        filtered_claims = claims_data

    return jsonify(filtered_claims)

@app.route("/")
def home():
    return render_template("index.html")
if __name__ == "__main__":
    app.run(debug=True)