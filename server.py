from bottle import route, run, request

@route('/ip')
def get_address():
    """ return the forwarded address """
    req = request.environ.get('HTTP_X_FORWARDED_FOR') or request.environ.get('REMOTE_ADDR')

    return "<center><h1>address: {}</h1></center>".format(req)

run(host='0.0.0.0', port=80, debug=True)
