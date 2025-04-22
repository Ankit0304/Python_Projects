import qrcode as qr
from PIL import Image

# img = qr.make("Ankit Baingane")
# img.save("QR_Code.png")

qr1 = qr.QRCode(version=1,
                error_correction=qr.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4
                )

qr1.add_data("https://www.mumbaiindians.com/membership")
qr1.make(fit=True)
img1 = qr1.make_image(fill_color="red", back_color="yellow")
img1.save("MI_Family.png")

