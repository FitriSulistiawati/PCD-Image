import imageio
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt

# Baca gambar menggunakan imageio
image = imageio.imread('C:\\Users\\Lenovo\\Pictures\\Screenshots\\g_5___5_kelakuan_unik_ritsuki_si_bocah_ora_eling_keturunan_jepang_-_tulungagung_idola_para_auncle_online_p_ritsuki_ueno-20240707-001-non_fotografer_kly.jpg')

# Konversi gambar ke skala abu-abu
gray_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

# Terapkan Gaussian filter
blurred_image = ndimage.gaussian_filter(gray_image, sigma=3)

# Tampilkan hasil gambar asli dan gambar hasil blur
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(gray_image, cmap='gray')
ax[0].set_title("Gambar Skala Abu-Abu")
ax[0].axis('off')
ax[1].imshow(blurred_image, cmap='gray')
ax[1].set_title("Gambar Setelah Gaussian Blur")
ax[1].axis('off')
plt.show()

