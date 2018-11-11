from socketIO_client import SocketIO, LoggingNamespace

def handle_code(code):
    print('response:', code)

with SocketIO('localhost', 5000, LoggingNamespace) as socketIO:
    socketIO.emit('code_request')
    socketIO.on('code_send', handle_code)
    socketIO.wait(seconds=1)
