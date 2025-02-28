print("####### NEW RUN ########")
import cv2
import numpy as np
from scipy.io.wavfile import write

# calculate the average color of a frame
def average_color(frame):
    return np.mean(frame, axis=(0, 1))  # gets average colour in RGB

# map intensity to pitch 
def map_intensity_to_pitch(intensity):
    return int(80 + intensity / 5)  # map intensity to pitch range (volume)

# map color to volume (Euclidean norm as volume)
def map_color_to_volume(color):
    return np.linalg.norm(color) / 255  

# generate a sine wave tone based on the frequency (pitch)
def generate_tone(frequency, duration=0.1, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    return wave

# save sound 
def save_sound_from_features(frame_colors):
    sound = []
    for color in frame_colors:
        intensity = np.mean(color)  # get intensity
        pitch = map_intensity_to_pitch(intensity)  # map to pitch
        tone = generate_tone(pitch)
        sound.append(tone)
    final_sound = np.concatenate(sound)
    write("sound9.wav", 44100, final_sound.astype(np.float32))

# put it all together and make sound from video
def generate_sound_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)

    cap.release()

    frame_colors = [average_color(frame) for frame in frames]
    save_sound_from_features(frame_colors)


# call function
path = "/Users/oliviasteed/Desktop/edited_videos/layer9_1.mp4"
generate_sound_from_video(path)
