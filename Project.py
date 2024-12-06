import csv
from flask import Flask, render_template, request

app = Flask(__name__)

# Load data from CSV file
with open("Nba.csv", "r") as f:
    reader = csv.DictReader(f)  # Use DictReader to handle columns by name
    rows = list(reader)

# Route for the homepage
@app.route("/", methods=["GET", "POST"])
def home():
    question = None  # Default value for the player
    if request.method == "POST":
        question = request.form.get("player_name")  # Get player name from form input

    # Build a dictionary for player stats: key = player name, value = stats (list of PPG, RPG, APG)
    stats = {row["NAME"]: [row["PPG"], row["RPG"], row["APG"]] for row in rows}

    if question:
        if question in stats:
            player_stats = stats[question]  # Get the stats for the chosen player
            return render_template("home.html", question=question, stats=player_stats)
        else:
            return render_template("home.html", question=question, stats=None)  # Player not found
    else:
        # Return an empty page or instruction if no player is selected
        return render_template("home.html", question=None, stats=None)

if __name__ == "__main__":
    app.run(debug=True)  # Start the Flask application with debugging enabled



