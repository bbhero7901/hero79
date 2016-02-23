import pygtk
import requests

pygtk.require("2.0")
import gtk
import gtk.glade

class LoginWindow:

    def __init__(self):
        self.glade = gtk.Builder()
        self.glade.add_from_file("coba2.glade")
        self.glade.connect_signals(self)
        self.main_window = self.glade.get_object("main_dialog")
        self.main_window.set_default(self.glade.get_object("btn_login"))
        self.main_window.connect("destroy", gtk.main_quit)
        self.main_window.show_all()

    def btn_login_pressed(self, evt):
        txt_username = self.glade.get_object('txt_username').get_text()
        txt_password =self.glade.get_object('txt_password').get_text()
        print(txt_username, txt_password)

        login_succeded = False
        url = 'http://127.0.0.1:5000/login/{}/{}'.format(txt_username, txt_password)
        r = requests.get(url)
        d = r.json()
        print ('hdgfhgjh', d)
        login_succeded = d['succeded']
        parent = self.main_window
        if login_succeded:
            md = gtk.MessageDialog(parent, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, gtk.BUTTONS_CLOSE, "Login succeed")
            response = md.run()
            if response == gtk.RESPONSE_CLOSE:
                md.destroy()
        else:
            md = gtk.MessageDialog(parent, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE, "Login failed")
            response = md.run()
            if response == gtk.RESPONSE_CLOSE:
                md.destroy()
if __name__ == "__main__":
    try:
        a = LoginWindow()
        gtk.main()
    except KeyboardInterrupt:
        pass