from flask import Flask, render_template, request, jsonify
import smtplib

app = Flask(__name__)

sender = 'yourSender@company.com'

host = "192.168.1.1235" # <- HOST IP 
port = 25 # <- HOST PORT
username = "yourUsername@company.com"
password = "yourPassword"

@app.route('/sendEmail', methods=['POST'])
def mail():
    fetch_getEmailContent = request.form['getEmailContent']
    fetch_getEmailReceiver = 'yourReceiver@company.com'  # DEFAULT RECEIVER CHANGE IT TO IF YOU WANT ----> IF YOU WANT TO SET AS DEFAULT OR ONLY ONE ##
    fetch_getEmailSender = request.form['getSenderEmail']
    print(fetch_getEmailReceiver)

    if not fetch_getEmailContent or not fetch_getEmailSender:
        return jsonify(False)
    else:
        sendingEmail(fetch_getEmailReceiver, fetch_getEmailSender, fetch_getEmailContent)
        return jsonify(True)


def sendingEmail(fetch_getEmailReceiver, fetch_getEmailSender, fetch_getEmailContent):
    fromSender = f"<{fetch_getEmailSender}>"
    message = f"""From: {fromSender}
To: {fetch_getEmailReceiver}
Subject: SMTP e-mail test
{fetch_getEmailContent}"""
    try:
        smtpObj = smtplib.SMTP(host, port)
        smtpObj.login(username, password)  # Authenticate with the SMTP server
        smtpObj.sendmail(sender, fetch_getEmailReceiver, message)
        msg = "Successfully sent email"
        print(msg)
        return jsonify(msg=msg)
    except Exception as e:
        msg = f"Error: Unable to send email: {str(e)}"
        print(msg)
        return jsonify(msg=msg)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
