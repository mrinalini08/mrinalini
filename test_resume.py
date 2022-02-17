
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def gfg():
    if request.method == "POST":
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        highest_qualification = request.form.get("highqual")
        return """We will review it shortly.
        We thoroughly review all resumes we receive against skill and experience requirements for the
        open position. Given the large number of resumes submitted for each position, we are unable to
        respond to every applicant. However, should your qualifications match our needs, we will
        certainly contact you to arrange an interview in the near future.
        Thanks again for your interest.
        Sincerely,
        Balihoo Hiring Team"""
    return render_template("form.html")


if __name__ == '__main__':
    app.run()