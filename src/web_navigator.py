import webbrowser

class DarkWeb:
    def __init__(self, tor_path = "/opt/tor-browser/Browser/start-tor-browser"):
        webbrowser.register('tor', None, webbrowser.BackgroundBrowser(tor_path))
        self.browser = webbrowser.get('tor')

    def open_breachforums(self):
        self.browser.open("http://breached26tezcofqla4adzyn22notfqwcac7gpbrleg4usehljwkgqd.onion/")

    def open_xss(self):
        self.browser.open("http://breached26tezcofqla4adzyn22notfqwcac7gpbrleg4usehljwkgqd.onion/")

class SurfaceWeb:
    def __init__(self):
        self.navigator = webbrowser.get()

    def osint_framework(self):
        self.navigator.open("https://osintframework.com/")

    def mitre_attack(self):
        self.navigator.open("https://attack.mitre.org/")

DarkWeb().open_breachforums()
