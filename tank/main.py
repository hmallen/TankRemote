import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GObject

from tank.motors import Motors
from tank.video import Video
from tank.application import Application


def main():
    #gobject.threads_init()
    GObject.threads_init()
    motors = Motors()
    video = Video()
    app = Application(motors, video)
    Gtk.main()
    if video.thread:
        video.thread.quit = True

if __name__ == '__main__':
    main()
