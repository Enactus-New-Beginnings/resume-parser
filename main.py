from flask import Flask, render_template
import parser

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template("index.html")
  
@app.route("/parse")
def parse_resume():
  sample_text = "Functional Resume Sample John W. Smith 2002 Front Range Way Fort Collins, CO 80525 jwsmith@colostate.edu Career Summary Four years experience in early childhood development with a diverse background in the care of special needs children and adults. Adult Care Experience •  Determined work placement for 150 special needs adult clients. •  Maintained client databases and records. •  Coordinated client contact with local health care professionals on a monthly basis. •  Managed 25 volunteer workers. Childcare Experience •  Coordinated service assignments for 20 part-time counselors and 100 client families. •  Oversaw daily activity and outing planning for 100 clients. •  Assisted families of special needs clients with researching financial assistance and healthcare. •  Assisted teachers with managing daily classroom activities. •  Oversaw daily and special student activities. Employment History 1999-2002   Counseling Supervisor, The Wesley Center, Little Rock, Arkansas. 1997-1999   Client Specialist, Rainbow Special Care Center, Little Rock, Arkansas 1996-1997   Teacher's Assistant, Cowell Elementary, Conway, Arkansas Education University ofArkansas at Little Rock, Little Rock, AR •  BS in Early Childhood Development (1999) •  BA in Elementary Education (1998) •  GPA (4.0 Scale): Early Childhood Development — 3.8, Elementary Education — 3.5, Overall 3.4. •  Dean's List, Chancellor's List"
  return parser.return_resume(sample_text)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)