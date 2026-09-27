import wave
import math
import numpy as np
from mido import MidiFile

print("Converting MIDI to audio...")

midi_file = MidiFile("generated_music.mid")

sample_rate = 44100
audio = []

# Piano-like simple synthesis
def make_note(frequency, duration, volume=0.25):
    samples = int(sample_rate * duration)

    t = np.linspace(
        0,
        duration,
        samples,
        endpoint=False
    )

    # Simple piano-like sound using harmonics
    sound = (
        np.sin(2 * np.pi * frequency * t)
        + 0.5 * np.sin(2 * np.pi * frequency * 2 * t)
        + 0.25 * np.sin(2 * np.pi * frequency * 3 * t)
    )

    # Fade in and fade out
    envelope = np.ones(samples)

    fade = min(
        int(sample_rate * 0.03),
        samples // 2
    )

    if fade > 0:
        envelope[:fade] = np.linspace(0, 1, fade)
        envelope[-fade:] = np.linspace(1, 0, fade)

    return sound * envelope * volume


for track in midi_file.tracks:

    current_time = 0

    for msg in track:

        current_time += msg.time

        if msg.type == "note_on" and msg.velocity > 0:

            frequency = 440 * (
                2 ** ((msg.note - 69) / 12)
            )

            duration = 0.4

            note_audio = make_note(
                frequency,
                duration
            )

            audio.extend(note_audio)


if len(audio) == 0:
    raise ValueError("No playable notes found in MIDI file.")


audio = np.array(audio)

# Normalize audio
audio = audio / np.max(np.abs(audio))

audio = (audio * 32767).astype(np.int16)

with wave.open("generated_music.wav", "wb") as wav_file:

    wav_file.setnchannels(1)
    wav_file.setsampwidth(2)
    wav_file.setframerate(sample_rate)

    wav_file.writeframes(
        audio.tobytes()
    )

print()
print("Audio created successfully!")
print("Saved as generated_music.wav")