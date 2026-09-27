import json
import os
from music21 import stream, note, chord, instrument, tempo


# =========================================
# GET SETTINGS FROM AI MUSIC STUDIO
# =========================================

# Duration
duration_seconds = int(
    os.environ.get("MUSIC_DURATION", "30")
)

# Mood
selected_mood = os.environ.get(
    "MUSIC_MOOD",
    "Calm"
)

# Tempo
selected_tempo = os.environ.get(
    "MUSIC_TEMPO",
    "Medium"
)

# Instrument
selected_instrument_name = os.environ.get(
    "MUSIC_INSTRUMENT",
    "Piano"
)


print("=========================================")
print("AI MUSIC SETTINGS")
print("=========================================")
print("Duration:", duration_seconds, "seconds")
print("Mood:", selected_mood)
print("Tempo:", selected_tempo)
print("Instrument:", selected_instrument_name)
print("=========================================")


# =========================================
# LOAD GENERATED NOTES
# =========================================

print("Loading generated notes...")

with open("generated_notes.json", "r") as f:
    notes = json.load(f)

print("Total generated items:", len(notes))


# =========================================
# CREATE MUSIC STREAM
# =========================================

music = stream.Stream()


# =========================================
# MOOD TEMPO
# =========================================

if selected_mood == "Calm":

    mood_bpm = 70

elif selected_mood == "Happy":

    mood_bpm = 110

elif selected_mood == "Energetic":

    mood_bpm = 140

elif selected_mood == "Emotional":

    mood_bpm = 80

else:

    # Relaxing
    mood_bpm = 60


# =========================================
# APPLY USER TEMPO
# =========================================

if selected_tempo == "Slow":

    bpm = max(40, mood_bpm - 20)

elif selected_tempo == "Fast":

    bpm = mood_bpm + 20

else:

    # Medium
    bpm = mood_bpm


# Add tempo to music
music.insert(
    0,
    tempo.MetronomeMark(
        number=bpm
    )
)
print("Mood BPM:", mood_bpm)
print("Final BPM:", bpm)


# =========================================
# MATCH MUSIC TO SELECTED DURATION
# =========================================

# Each generated item is approximately
# one beat long.

notes_needed = duration_seconds


if len(notes) < notes_needed:

    # Repeat notes when necessary

    notes = (
        notes *
        ((notes_needed // len(notes)) + 1)
    )[:notes_needed]

else:

    # Trim notes to requested length

    notes = notes[:notes_needed]


print(
    "Notes used for duration:",
    len(notes)
)


# =========================================
# ADD NOTES TO MUSIC
# =========================================

for value in notes:

    value = str(value).strip()

    try:

        # ---------------------------------
        # STANDARD PITCH NAMES
        # Examples:
        # E5
        # B4
        # F#3
        # E-5
        # ---------------------------------

        if any(
            char.isalpha()
            for char in value
        ):

            new_note = note.Note(value)

            new_note.quarterLength = 1

            music.append(new_note)


        # ---------------------------------
        # NUMERIC / CHORD REPRESENTATION
        # Examples:
        # 4.8
        # 9.0
        # 11.1
        # ---------------------------------

        else:

            numbers = value.split(".")


            if len(numbers) > 1:

                chord_notes = []


                for number in numbers:

                    if number.strip().isdigit():

                        midi_number = int(number)

                        # Keep MIDI pitch valid
                        midi_number = max(
                            0,
                            min(127, midi_number)
                        )

                        chord_notes.append(
                            note.Note(
                                midi_number
                            )
                        )


                if chord_notes:

                    new_chord = chord.Chord(
                        chord_notes
                    )

                    new_chord.quarterLength = 1

                    music.append(
                        new_chord
                    )


            else:

                midi_number = int(
                    float(value)
                )

                midi_number = max(
                    0,
                    min(127, midi_number)
                )

                new_note = note.Note(
                    midi_number
                )

                new_note.quarterLength = 1

                music.append(
                    new_note
                )


    except Exception as e:

        print(
            "Skipped:",
            value,
            "| Error:",
            e
        )


# =========================================
# SELECT INSTRUMENT
# =========================================

print()
print(
    "Applying instrument:",
    selected_instrument_name
)


if selected_instrument_name == "Electronic":

    music.insert(
        0,
        instrument.ElectricPiano()
    )


elif selected_instrument_name == "Ambient":

    music.insert(
        0,
        instrument.Flute()
    )


elif selected_instrument_name == "Acoustic Piano":

    music.insert(
        0,
        instrument.Piano()
    )


else:

    music.insert(
        0,
        instrument.Piano()
    )


# =========================================
# WRITE MIDI FILE
# =========================================

music.write(
    "midi",
    fp="generated_music.mid"
)


# =========================================
# FINISHED
# =========================================

print()
print("=========================================")
print("MIDI FILE CREATED SUCCESSFULLY!")
print("=========================================")
print("File: generated_music.mid")
print("Duration:", duration_seconds, "seconds")
print("Mood:", selected_mood)
print("Tempo:", selected_tempo)
print("BPM:", bpm)
print("Instrument:", selected_instrument_name)
print("=========================================")