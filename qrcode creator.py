import pyqrcode
import png 
def create_qr_code(url, filename):
    qrcode = pyqrcode.create(url, error='H', version=27, mode='binary')
    #qrcode.svg(filename, scale=8)
    qrcode.png(filename, scale=5, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
    print(qrcode.terminal(quiet_zone=1))
    
    
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
filename = "testqrcode.png"
create_qr_code(url, filename)