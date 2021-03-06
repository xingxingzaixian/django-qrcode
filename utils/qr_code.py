import os
import time
import qrcode
from PIL import Image
from MyQR import myqr
from QRCode.settings import BASE_DIR


def gen_qrcode(text):
    # 创建qrcode对象
    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=10,
        border=2,
    )

    qr.add_data(text)

    # 创建二维码图片
    img = qr.make_image()

    # 图片转换为RGBA格式
    img = img.convert('RGBA')

    # 返回二维码图片的大小
    img_w, img_h = img.size

    # 打开logo
    logo = Image.open(os.path.join(BASE_DIR, 'static/images/logo.jpeg'))

    # logo大小为二维码的四分之一
    logo_w = img_w // 4
    logo_h = img_w // 4

    # 修改logo图片大小
    logo = logo.resize((logo_w, logo_h), Image.ANTIALIAS)

    # 把logo放置在二维码中间
    w = (img_w - logo_w) // 2
    h = (img_h - logo_h) // 2

    img.paste(logo, (w, h))

    qr_path = 'static/imgcard/%s.png' % time.time()
    img.save(os.path.join(BASE_DIR, qr_path))

    return qr_path


def gen_gif_qrcode(text):
    pic_path = os.path.join(BASE_DIR, 'static/images/background.gif')
    save_name = '%s.gif' % time.time()
    myqr.run(
        words=text,
        version=1,
        level='H',
        picture=pic_path,
        colorized=True,
        contrast=1.0,
        brightness=1.0,
        save_name=save_name,
        save_dir=os.path.join(BASE_DIR, 'static/imgcard')
    )
    return 'static/imgcard/%s' % save_name
