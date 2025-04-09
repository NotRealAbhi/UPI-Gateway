from flask import Flask, render_template, request, redirect
import os
from datetime import datetime

app = Flask(__name__)

LOG_FILE = "logs/payments.log"
UPI_ID = "genuine-sellers@ibl"  # Change this to your real UPI ID
NAME = "ABHISHEK BANSHIWAL"       # Change this to your name
AMOUNT = "1"           # Change amount as needed


@app.route("/")
def payment_page():
    qr_link = f"upi://pay?pa={UPI_ID}&pn={NAME}&am={AMOUNT}&cu=INR"
    return render_template("payment.html", upi_id=UPI_ID, name=NAME, amount=AMOUNT, qr_link=qr_link)


@app.route("/verify", methods=["POST"])
def verify_payment():
    utr = request.form.get("utr")

    if not utr:
        return "❌ UTR missing"

    # Simulate simple verification
    verified = utr.startswith("3")  # Replace this with real logic/API/SMS parsing

    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} | UTR: {utr} | VERIFIED: {verified}\n")

    if verified:
        return "✅ Payment Verified! Thank you!"
    else:
        return "❌ UTR Invalid or Payment Not Detected!"


if __name__ == "__main__":
    os.makedirs("logs", exist_ok=True)
    app.run(debug=True, host="0.0.0.0", port=8000)


    
