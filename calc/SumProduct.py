from cgi import parse_qs
from Sumtemplate import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]

    if '' not in [a, b]:
        a, b = int(a), int(b)
        x = a+b
        y = a * b

    response_body = html % {
        'Sum' : x,
        'Product' : y,
    }
    start_response('200 OK', [
    ('Content-Type', 'text/html'),
    ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
