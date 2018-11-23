from bottle import route, run, request

@route('/hello')
def hello():
    x = request.environ.get('HTTP_X_FORWARDED_FOR') or request.environ.get('REMOTE_ADDR')

    return "Hello World!" +  "EAE" + str(x)

run(host='0.0.0.0', port=8080, debug=True)
