from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
authorizer=DummyAuthorizer()
authorizer.add_user('zhanghao','mima','.',perm='elradfmw')
handler=FTPHandler
handler.authorizer=authorizer
server=FTPServer(('ip',21),handler)
server.serve_forever()