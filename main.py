import qrcode

print('Paste the link for qrcode')
web = input()
image = qrcode.make(web)
image.save('gr.png')
