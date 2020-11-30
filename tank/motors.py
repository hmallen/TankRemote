import socket
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GObject

CONTROL_PORT = 8150
DEFAULT_IP = '10.10.1.1'


class Motors(GObject.GObject):
    LEFT = 1
    RIGHT = 2
    CAMERA = 3

    FORWARD = 1
    BACK = 2
    STOP = 0

    def __init__(self, port=CONTROL_PORT):
        GObject.GObject.__init__(self)
        self.is_connected = False
        self.port = port
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

    def init_connection(self, ip):
        print('Connecting to', ip)
        self.connection.connect((ip, self.port))
        self.connection.sendall('t1')
        self.is_connected = True
        self.emit('connected', True)
        print('Connected')

    def command(self, motor, direction):
        try:
            self.connection.sendall('%i%i' % (motor, direction))
        except IOError:
            self.emit('connected', False)
            self.is_connected = False

GObject.type_register(Motors)
GObject.signal_new("connected", Motors, GObject.SignalFlags.RUN_FIRST,
                   GObject.TYPE_NONE, (GObject.TYPE_BOOLEAN, ))
