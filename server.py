from flask import Flask, render_template, request
import datetime
import time
from url_analyzer import analyze_url

app = Flask(__name__)

LOG_FILE = "logs.txt"

def log_event(event):
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{datetime.datetime.now()} - {event}\n")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/email-demo")
def email_demo():
    return render_template("email_demo.html")

@app.route("/landing")
def landing():
    # Beležimo vreme na ćirilici
    start_time = time.time()
    log_event("Корисник је отворио страницу (почетак мерења времена)")
    return render_template("landing_page.html", start_time=start_time)

@app.route("/submit", methods=["POST"])
def submit():
    try:
        start_time = float(request.form.get("start_time", 0))
        end_time = time.time()
        duration = round(end_time - start_time, 2)
    except:
        duration = 0

    # Tekst poruke na ćirilici
    log_event(f"Форма послата. Време размишљања: {duration} секунди. (Подаци НИСУ сачувани)")

    return render_template("simulation_result.html", duration=duration)

@app.route("/stats")
def stats():
    logs = []
    try:
        # Обавезно encoding="utf-8" због ћирилице
        with open(LOG_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for line in lines:
                parts = line.split(" - ", 1)
                if len(parts) == 2:
                    logs.append({"time": parts[0], "event": parts[1]})
    except Exception as e:
        logs = [{"time": "-", "event": f"Грешка при читању логова: {e}"}]

    return render_template("stats.html", logs=logs)

@app.route("/url-check", methods=["GET", "POST"])
def url_check():
    result = None
    if request.method == "POST":
        url = request.form["url"]
        result = analyze_url(url)
    return render_template("url_checker.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)