from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

app = Flask(__name__)

sender = 'yourSender@company.com'

host = "192.168.1.12345" # <- HOST IP 
port = 25 # <- HOST PORT
username = "yourUsername@company.com"
password = "yourPassword"

@app.route('/sendEmail', methods=['POST'])
def mail():
    fetch_getEmailContent = request.form['getEmailContent']
    fetch_getEmailReceiver = 'yourReceiver@company.com'  # DEFAULT RECEIVER CHANGE IT TO IF YOU WANT ----> IF YOU WANT TO SET AS DEFAULT OR ONLY ONE ##
    fetch_getEmailSender = request.form['getSenderEmail']
    uploaded_file = request.files['file']  # Access the uploaded file

    if not fetch_getEmailContent or not fetch_getEmailSender:
        return jsonify(False)
    else:
        sendingEmail(fetch_getEmailReceiver, fetch_getEmailSender, fetch_getEmailContent, uploaded_file)
        return jsonify(True)


def sendingEmail(fetch_getEmailReceiver, fetch_getEmailSender, fetch_getEmailContent, uploaded_file):
    fromSender = f"<{fetch_getEmailSender}>"

    msg = MIMEMultipart()
    msg['From'] = fromSender
    msg['To'] = fetch_getEmailReceiver
    msg['Subject'] = 'SMTP e-mail test'

    body = fetch_getEmailContent
    msg.attach(MIMEText(body, 'plain'))

    # Attach the uploaded file
    if uploaded_file:
        filename = uploaded_file.filename
        attachment = MIMEBase('application', 'octet-stream')
        attachment.set_payload(uploaded_file.read())
        encoders.encode_base64(attachment)
        attachment.add_header('Content-Disposition', f'attachment; filename= {filename}')
        msg.attach(attachment)

    try:
        smtpObj = smtplib.SMTP(host, port)
        smtpObj.login(username, password)  # Authenticate with the SMTP server
        smtpObj.sendmail(sender, fetch_getEmailReceiver, msg.as_string())
        
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
