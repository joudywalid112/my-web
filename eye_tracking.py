import sounddevice as sd
import numpy as np
import soundfile as sf

# تحديد مدة التسجيل بالثواني
duration = 60  # 60 ثانية (دقيقة واحدة)
samplerate = 44100  # معدل العينة (Hz)

print("يبدأ التسجيل الآن...")

# تسجيل الصوت
recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=2, dtype=np.int16)
sd.wait()  # الانتظار حتى ينتهي التسجيل

print("تم التسجيل، جاري حفظ الملف...")

# حفظ التسجيل إلى ملف WAV
sf.write("recorded_audio.wav", recording, samplerate)

print("تم حفظ الملف بنجاح!")

