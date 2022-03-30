import qrcode

''' Easy Way
qr = qrcode.make("Never gonna give you up!")  # information behind the qr code
# qr.save("NGGYU.png")  # saves the qr code
'''

qr = qrcode.QRCode(
    version=1,  # number between 1 and 40; controls the size
    error_correction=qrcode.ERROR_CORRECT_M,  # default
    box_size=15,  # dimension size
    border=10  # thickness of the borders
)

data = "https://www.youtube.com/watch?v=JrdGAcZ8vhs"
qr.add_data(data=data)
qr.make(fit=True)
image = qr.make_image(fill="white", back_color="orange")
image.save("RR.png")