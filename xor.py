from PIL import Image
import numpy as np

A = np.array(Image.open("stego.png").convert("RGB"))
B = np.array(Image.open("twin.png").convert("RGB"))

xor0 = (A[:,:,0] ^ B[:,:,0])
xor1 = (A[:,:,1] ^ B[:,:,1])
xor2 = (A[:,:,2] ^ B[:,:,2])
combined = (( (xor0 | xor1 | xor2) & 1 ) * 255).astype('uint8') 
Image.fromarray(combined, 'L').save("secret_key.png")
