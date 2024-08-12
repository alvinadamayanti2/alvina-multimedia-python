from PIL import Image
from PIL import ImageFilter
from pydub import AudioSegment
import simpleaudio as sa


# Memuat gambar
image = Image.open('image.png')

# Menyimpan gambar
image.save('result.jpg')

cropped_image = image.crop((10, 10, 200, 200))
cropped_image.save('cropped_result.jpg')

resized_image = cropped_image.resize((100, 100))
resized_image.save('resized_result.jpg')


filtered_image = resized_image.filter(ImageFilter.BLUR)
filtered_image.save('filtered_result.jpg')



# Memuat file audio
audio = AudioSegment.from_file('audio.mp3')

# Mengonversi ke WAV (opsional, jika formatnya bukan WAV)
audio.export('result.wav', format='wav')

# Memutar audio
wave_obj = sa.WaveObject.from_wave_file('result.wav')
play_obj = wave_obj.play()

# Menunggu sampai audio selesai diputar
play_obj.wait_done()

clipped_audio = audio[:10000]  # Mendapatkan 10 detik pertama
clipped_audio.export('clipped_result.mp3', format='mp3')


combined_audio = audio + clipped_audio
combined_audio.export('combined_result.mp3', format='mp3')


louder_audio = audio + 10  # Meningkatkan volume sebesar 10dB
louder_audio.export('louder_result.mp3', format='mp3')