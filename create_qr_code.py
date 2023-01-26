import qrcode

# Create QR code object
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

# Add data to the QR code object
qr.add_data("https://www.nerdybio.com")
qr.make(fit=True)

# Create an image from the QR code object
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to your computer
img.save("nerdybio_qr.png")
