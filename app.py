import qrcode
from PIL import Image

def create_qr():
    face = Image.open('ticko_for_qr.jpg').crop((30,18,100,100))#.crop((175, 90, 235, 150)) # data/src/lena.jpg

    qr_big = qrcode.QRCode(
        version=10,
        error_correction=qrcode.constants.ERROR_CORRECT_H
        )
    my_text = 'I am Lena'
    qr_big.add_data(my_text)
    qr_big.make()
    img_qr_big = qr_big.make_image().convert('RGB')

    pos = ((img_qr_big.size[0] - face.size[0]) // 2, (img_qr_big.size[1] - face.size[1]) // 2)

    img_qr_big.paste(face, pos)
    my_qr_file = my_text + '.png'
    img_qr_big.save(my_qr_file) # data/dst/qr_lena2.png

if __name__ == '__main__':
    create_qr()
