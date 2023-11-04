from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def collect_information():
    if request.method == "POST":
        name = request.form["name"]
        class_name = request.form["class"]
        section = request.form["section"]
        location = request.form["location"]

        # Store the collected data in a text file
        with open("collected_data.txt", "a") as file:
            file.write(f" {name}, {class_name}, {section} ,   {location}\n")

        return f"Data collected and stored: Name: {name}, Class: {class_name}, Section:{section} , Location: {location}"

    return render_template("Thar.html")

if __name__ == "__main__":
    app.run(debug=True)
