from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/local health services')
def local_health_services():
    return render_template('local_health_services.html')

  
if __name__ == '__main__':
  app.run(host='0.0.0.0',    
      debug=True)