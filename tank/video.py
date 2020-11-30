import threading
import urllib
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
gi.require_version('Gdk', '3.0')
from gi.repository import Gdk, GdkPixbuf
from gi.repository import GObject

VIDEO_PORT = 8196


class Video(GObject.GObject):
    '''
    Connect to the MJPEG stream of the tank!
    '''
    def __init__(self, port=VIDEO_PORT):
        GObject.GObject.__init__(self)
        self.port = port
        self.stream = None
        self.thread = None
        self.widget = None

    def init_connection(self, ip):
        print('Connecting to video on', ip)
        self.stream = urllib.urlopen('http://%s:%d/' % (ip, self.port))
        print('Starting video thread')
        self.thread = VideoThread(self, self.widget)
        self.thread.start()
        print('connected')

    def get_raw_frame(self):
        '''
        Parse an MJPEG http stream and yield each frame.

        :return: generator of JPEG images
        '''
        raw_buffer = ''
        while True:
            new = self.stream.read(1034)
            if not new:
                # Connection dropped
                yield None
            raw_buffer += new
            a = raw_buffer.find('\xff\xd8')
            b = raw_buffer.find('\xff\xd9')
            if a != -1 and b != -1:
                frame = raw_buffer[a:b+2]
                raw_buffer = raw_buffer[b+2:]
                yield frame


class VideoThread(threading.Thread):
    '''
    A background thread that takes the MJPEG stream and
    updates the GTK image.
    '''
    def __init__(self, video, widget):
        super(VideoThread, self).__init__()
        self.video = video
        self.widget = widget
        self.quit = False

    def run(self):
        for frame in self.video.get_raw_frame():
            if self.quit or frame is None:
                return
            loader = GdkPixbuf.PixbufLoader('jpeg')
            loader.write(frame)
            loader.close()
            pixbuf = loader.get_pixbuf()
            GObject.idle_add(self.widget.set_from_pixbuf, pixbuf)