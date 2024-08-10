import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://sarthakdhatrak.com')
qr.make(fit=True)

img = qr.make_image(fill_color="red", back_color="blue")
img.save("qr.png")