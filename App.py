from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("payment.html")

@app.route("/verify", methods=["POST"])
def verify():
    utr = request.form.get("utr")
    # Replace this with actual verification logic
    if utr.startswith("3"):
        return "✅ Payment Verified!"
    else:
        return "❌ Invalid UTR or Payment Not Found!"

if __name__ == "__main__":
    app.run(debug=True)
  
