import sys

sys.path.append("/usr/local/lib/python2.7/site-packages/")

from hello import app

if __name__ == "__main__":
    listen_on = "8080"
    app.run(port=listen_on)
