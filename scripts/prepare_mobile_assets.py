import os
from PIL import Image

os.makedirs('assets/mobile', exist_ok=True)

# 1. Everyday Grace
everyday_img_path = "images/Section - 5. 'Everyday Grace - Regular Wear Spotlight.png"
if os.path.exists(everyday_img_path):
    im = Image.open(everyday_img_path)
    w, h = im.size
    print('Everyday Grace size:', w, h)
    # Crop Left card (Mulmul Cotton & Breathable Linen)
    c1 = im.crop((int(0.035 * w), int(0.20 * h), int(0.485 * w), int(0.78 * h)))
    c1.save('assets/mobile/everyday_1.png')
    # Crop Right card (Office Luxe Silk-Linen Co-ords)
    c2 = im.crop((int(0.515 * w), int(0.20 * h), int(0.965 * w), int(0.78 * h)))
    c2.save('assets/mobile/everyday_2.png')
    print('Saved everyday_1 and everyday_2')

# 2. Instagram lookbook images
insta_path = "images/Section - 8. Instagram Luxury Lookbook Feed Gallery.png"
if os.path.exists(insta_path):
    im = Image.open(insta_path)
    w, h = im.size
    # 5 images across width
    # y is roughly from 0.22*h to 0.90*h
    for i in range(5):
        x1 = int((0.0375 + i * 0.1875) * w)
        x2 = int((0.0375 + i * 0.1875 + 0.17) * w)
        crop = im.crop((x1, int(0.22 * h), x2, int(0.92 * h)))
        crop.save(f'assets/mobile/insta_{i+1}.png')
    print('Saved 5 insta lookbook crops')

# 3. Testimonials
test_path = "images/Section - 7. Customer Testimonials & Press Quotes.png"
if os.path.exists(test_path):
    im = Image.open(test_path)
    w, h = im.size
    print('Testimonials size:', w, h)

print('Mobile assets preparation complete!')
