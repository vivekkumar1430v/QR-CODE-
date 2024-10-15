import qrcode
from PIL import Image
import qrcode.constants

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=8,)

qr.add_data("https://github.com/vivekkumar1430v/CALCULATOR-PROJECTS/blob/main/FIRST1.py")
qr.make(fit=True)
img=qr.make_image(fill_color="green",back_color="yellow")
img.save("GIT_HUB.png")