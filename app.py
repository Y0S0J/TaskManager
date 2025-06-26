from flask import Flask, render_template
from routes.user_routes import user_bp
from routes.task_routes import task_bp


app = Flask(__name__)

# --- Url for both user and tasks have their personal prefix, using flask blueprint ---

app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(task_bp, url_prefix='/tasks')

@app.route('/')
def index():
    return render_template('home.html')


if __name__ == '__main__':     
    app.run(debug=True)        # --- All updates can be done live ---

