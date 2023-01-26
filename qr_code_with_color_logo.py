import qrcode
from PIL import Image

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
img = qr.make_image(fill_color="white", back_color="black")

# Open logo image
logo = Image.open("logo.png")

# Change the mode of logo to RGB
logo = logo.convert("RGB")

# Resize logo to appropriate size
logo = logo.resize((50, 50))

# Position logo in the center of QR code
img_w, img_h = img.size
logo_w, logo_h = logo.size
img.paste(logo, ((img_w - logo_w) // 2, (img_h - logo_h) // 2))

# Save the image to your computer
img.save("nerdybio_qr_logo.png")
