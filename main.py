from flask import Flask, render_template, request
import parser

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template("index.html")
  
@app.route("/parse")
def parse_resume():
  text = request.args.get('text')
  if text is None:
    return "<p>received an empty request. attach a 'text' parameter with your resume's raw text.</p>"
  return parser.return_resume(text)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)