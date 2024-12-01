from flask import Flask, request, render_template, redirect, url_for, flash
from routes import pdf_routes, email_routes, find_routes

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# 注册路由
app.register_blueprint(pdf_routes.bp)
app.register_blueprint(email_routes.bp)
app.register_blueprint(find_routes.bp)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)