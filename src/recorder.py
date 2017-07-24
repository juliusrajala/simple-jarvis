"""
Recorder works pretty much as expected,
it records a bit of audio and turns outputs
a wav recording.

Written by Julius Rajala 2017
"""
import wave
import pyaudio

PYA_INST = pyaudio.PyAudio()

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100

def record_frames(recording_length):
    print("Assistant is recording recording speech.")
    frames = []
    stream = PYA_INST.open(format=FORMAT,
                           channels=CHANNELS,
                           rate=RATE,
                           input=True,
                           frames_per_buffer=CHUNK)

    for i in range(0, int(RATE / CHUNK * recording_length)):
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    print("Assistant is done recording.")
    return frames

def output_file(file_name, frames):
    write_file = wave.open(file_name, 'wb')
    write_file.setnchannels(CHANNELS)
    write_file.setsampwidth(PYA_INST.get_sample_size(FORMAT))
    write_file.setframerate(RATE)
    write_file.writeframes(b''.join(frames))
    write_file.close()

if __name__ == "__main__":
    print("Calling main function")
    recording_frames = []
    recording_frames = record_frames(10)
    output_file("output.wav", recording_frames)
    PYA_INST.terminate()
