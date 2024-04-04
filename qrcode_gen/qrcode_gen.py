import segno

qrcode = segno.make_qr("https://www.xbazzi.com")

qrcode.save(
    "qrcode.png",
    scale=5,
    border=1,
    light="lightgreen",
    dark="darkblue",
    data_dark="black"
)