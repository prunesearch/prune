import flask, os, time

app = flask.Flask(__name__)
app.config['EXPLAIN_TEMPLATE_LOADING'] = True

@app.route("/")
def index():
    # Set the Content-Type header to HTML
    response = app.make_response(flask.render_template('index.html'))
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

@app.route("/search", methods=['GET'])
def search():
    response = app.make_response(flask.render_template('search.html'))
    if flask.request.args.get('q', '') == '':
        return 'Please provide a search query. - Prune'
    # Set the Content-Type header to HTML
    response.headers['Content-Type'] = 'text/html; charset=utf-8'
    return response

@app.errorhandler(404)

# inbuilt function which takes error as parameter
def not_found(e):

# defining function
  return flask.render_template("404.html")

def pid():
    return os.getpid()
def unixtime():
    return time.time()
def query():
    return flask.request.args.get('q', None)
def results():
    return '<b>bold</b>'

app.jinja_env.globals.update(pid=pid)
app.jinja_env.globals.update(unixtime=unixtime)
app.jinja_env.globals.update(query=query)
app.jinja_env.globals.update(results=results)

if __name__ == "__main__":
    app.run(debug=True)
