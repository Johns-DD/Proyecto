import qrcode
Mi_imagen = qrcode.make('https://mx.pinterest.com/pin/385691155608455582/')
type(Mi_imagen)  
Mi_imagen.save("Gorila Grosero.jpg")