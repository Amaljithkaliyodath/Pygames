import qrcode
from PIL import Image

def generate_qr_code(text, file_name, image_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)

    # Adding the logo
    logo = Image.open(image_name)
    img_logo = img.resize((int(logo.size[0] * 0.2), int(logo.size[1] * 0.2)))
    img.paste(img_logo, (int((qr.size - img_logo.size[0]) / 2), int((qr.size - img_logo.size[1]) / 2)))
    img.save(file_name)

generate_qr_code("https://github.com/Amaljithkaliyodath", "qr_code.png", "logo.png")