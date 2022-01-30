# Web development with Flask Framework
Flask is a so-called micro-framework, that is exteremely lean and a small library.
[QuickStart Flask](https://flask.palletsprojects.com/en/2.0.x/quickstart/#a-minimal-application)

To add `.css` and `.js` files, refer to `Static Files` section.

## Start the server
```bash
cd web server/Scripts/
activate
set FLASK_ENV=development
flask run
```
## Adding a favicon
```html
<link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}">
```

## Templating Engine with Jinja2
It allows us to use expressions in html files:
```html
<body>
	{{ 4 + 5}}
</body>
```
This gives you power to create dynamic server, for example to show the username.

## Url parameters
You need the following changes in your `server.py` file [source](https://flask.palletsprojects.com/en/2.0.x/quickstart/#variable-rules).
```python
@app.route("/<username>")
def hello_world(username=None):
    return render_template('index.html', name=username)
```
To be able to run the server, you need to give `127.0.0.1:5000`.