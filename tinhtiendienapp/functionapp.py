from PIL import Image, ImageDraw, ImageFont
from math import floor
def tinh_tien(dinh_muc, kwh, gia_dien):
    bang_tien_dien = []
    tong_tien = 0
    if gia_dien == 0:
        for dm in dinh_muc:
            kwh_in_dm = 0
            if kwh >= dm.level_start:
                if kwh >= dm.level_end:
                    kwh_in_dm = dm.level_end - dm.level_start
                else:
                    kwh_in_dm = kwh - dm.level_start

            if dm.level_no != 1 and kwh_in_dm != 0:
                kwh_in_dm += 1

            dinh_muc_amt = floor(kwh_in_dm * dm.level_price)
            tong_tien += dinh_muc_amt

            if dinh_muc_amt > 0:
                bang_tien_dien.append([dm.level_no, dm.level_start, dm.level_end, kwh_in_dm, dm.level_price, dinh_muc_amt])
    else:
        tong_tien = kwh * gia_dien
        bang_tien_dien.append([1, 0, kwh, gia_dien, tong_tien])

    return {'bang_tien_dien': bang_tien_dien, 'thanh_tien': tong_tien, 'tieu_thu' : kwh}


def generate_image(cong_suat, gia_dien, thoi_gian, ngay, tuan, thang):
    tieu_thu_nam = thang[0] * 12
    tien_dien_nam = thang[1] * 12
    tpl_img_url = 'media/images/tinh_tien_dien_tpl.png'
    img_url =  'media/images/tinh_tien_dien_{}_{}_{}.png'.format(cong_suat, gia_dien,
                                                                                                thoi_gian)
    try:
        Image.open(img_url)
        return 'tinh_tien_dien_{}_{}_{}.png'.format(cong_suat, gia_dien, thoi_gian)
    except IOError:
        img = Image.open(tpl_img_url)

    fnt = ImageFont.truetype('tinhtiendienapp/Fonts/arial.ttf', 20)
    fntbold = ImageFont.truetype('tinhtiendienapp/Fonts/arialbd.ttf', 20)
    d = ImageDraw.Draw(img)
    d.text((130, 22), "{} (W)".format(cong_suat), font=fntbold, fill=(81, 141, 218))
    d.text((315, 70), "{} (tiếng)".format(thoi_gian), font=fntbold, fill=(81, 141, 218))
    if gia_dien == 0:
        d.text((110, 118), "Theo giá lũy tiến của EVN", font=fntbold, fill=(68, 68, 68))
    else:
        d.text((110, 118), "{} (đồng)".format(gia_dien), font=fntbold, fill=(68, 68, 68))

    d.text((250, 218), "{:,}".format(ngay[0]), font=fnt, fill=(68, 68, 68))
    d.text((440, 218), "{:,}".format(ngay[1]), font=fnt, fill=(68, 68, 68))

    d.text((250, 260), "{:,}".format(tuan[0]), font=fnt, fill=(68, 68, 68))
    d.text((440, 260), "{:,}".format(tuan[1]), font=fnt, fill=(68, 68, 68))

    d.text((250, 307), "{:,}".format(thang[0]), font=fnt, fill=(68, 68, 68))
    d.text((440, 307), "{:,}".format(thang[1]), font=fnt, fill=(68, 68, 68))

    d.text((250, 352), "{:,}".format(tieu_thu_nam), font=fnt, fill=(68, 68, 68))
    d.text((440, 352), "{:,}".format(tien_dien_nam), font=fnt, fill=(68, 68, 68))
    img.save(img_url)

    return 'tinh_tien_dien_{}_{}_{}.png'.format(cong_suat, gia_dien, thoi_gian)


