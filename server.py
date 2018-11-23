from bottle import route, run, request

@route('/')
def get_address():
    """ return the forwarded address """
    req = request.environ.get('HTTP_X_FORWARDED_FOR') or request.environ.get('REMOTE_ADDR')

    return "address: {}".format(req)

run(host='0.0.0.0', port=8080, debug=True)
