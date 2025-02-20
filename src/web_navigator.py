import selenium
import webbrowser

class DarkWeb:
    def __init__(self):
        self.navigator = webbrowser.get()
    
    def osint_framework(self):
        self.navigator.open("https://osintframework.com/")
    
    def mitre_attack(self):
        self.navigator.open("https://attack.mitre.org/")

if __name__ == "__main__":
    DarkWeb().mitre_attack()
