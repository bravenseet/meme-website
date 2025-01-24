from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def button():
  with open('list.txt', 'r') as f:
      lines = f.readlines()
  link = random.choice(lines)
  return render_template('button.html', img=link)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)
