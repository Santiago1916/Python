import qrcode
#URL
input_data = "link"

#Instane of qrcode
qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
qr.add_data(input_data)
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')

img.save('qrcode1.png')
