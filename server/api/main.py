#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/health')
def health():
    return {"status": "Healthy"}


@app.route('/backup')
def backup():
    """
    Perform a backup of the Minecraft Server
    """

    # Get Files



if __name__ == '__main__':
    app.run(debug=True)
