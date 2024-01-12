from flask import Flask, render_template, request
import smtplib
import requests


posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()
OWN_EMAIL = "lathass199027@gmail.com"
OWN_PASSWORD = "Latha@199027"

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["subject"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, subject, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage:{message}"
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(OWN_EMAIL, OWN_PASSWORD)
        smtp_server.sendmail(OWN_EMAIL, OWN_PASSWORD, email_message)
        smtp_server.close()
        print("Email sent successfully!")

    except Exception as ex:
        print("Something went wrong….", ex)


if __name__ == "__main__":
    app.run(debug=True)
